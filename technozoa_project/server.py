from flask import Flask, jsonify
import cv2
import time
import os   
import math
import threading
from ultralytics import YOLO

app = Flask(__name__)

# ==============================
# SETTINGS
# ==============================
SNAPSHOT_TIMES = [10, 30, 60, 180, 300, 420, 600]  # seconds
DISTANCE_THRESHOLD = 150  # pixels for close proximity
CROWD_THRESHOLD = 2       # people close together = crowd

# Create folder if not exists
if not os.path.exists("snapshots"):
    os.makedirs("snapshots")

# Load YOLO model
model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

# Global variables
person_timers = {}
person_snapshot_times = {}
alerts = []
people_count = 0
crowd_detected = False

# ==============================
# YOLO Thread
# ==============================
def run_yolo():
    global people_count, crowd_detected, alerts

    print("✅ AI Surveillance Started")

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        current_time = time.time()
        results = model.track(frame, persist=True)

        centers = []
        ids = []

        # Process each detected object
        for r in results:
            if r.boxes is None or r.boxes.id is None:
                continue

            for box, track_id, cls in zip(r.boxes.xyxy, r.boxes.id, r.boxes.cls):
                if int(cls) != 0:
                    continue  # only person

                track_id = int(track_id)
                x1, y1, x2, y2 = map(int, box)
                x1, y1 = max(0, x1), max(0, y1)
                x2, y2 = min(frame.shape[1], x2), min(frame.shape[0], y2)

                cx = (x1 + x2)//2
                cy = (y1 + y2)//2
                centers.append((cx, cy))
                ids.append(track_id)

                # Timer + snapshots
                if track_id not in person_timers:
                    person_timers[track_id] = current_time
                    person_snapshot_times[track_id] = set()

                elapsed = int(current_time - person_timers[track_id])

                for milestone in SNAPSHOT_TIMES:
                    if milestone not in person_snapshot_times[track_id] and elapsed >= milestone:
                        person_crop = frame[y1:y2, x1:x2]
                        if person_crop.size == 0:
                            continue
                        timestamp = time.strftime("%Y%m%d_%H%M%S")
                        filename = f"snapshots/person_{track_id}{milestone}s{timestamp}.jpg"
                        if cv2.imwrite(filename, person_crop):
                            print(f"📸 Saved: {filename}")
                            person_snapshot_times[track_id].add(milestone)
                            alerts.append({
                                "type": "SNAPSHOT",
                                "person_id": track_id,
                                "time": milestone,
                                "file": filename,
                                "timestamp": timestamp
                            })

                # Draw bounding box + timer
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(frame,
                            f"ID {track_id}: {elapsed}s",
                            (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (255,0,0), 2)

        # Update counts
        people_count = len(ids)
        close_pairs = 0

        # Distance lines
        for i in range(len(centers)):
            for j in range(i+1, len(centers)):
                x1c, y1c = centers[i]
                x2c, y2c = centers[j]
                distance = math.sqrt((x2c - x1c)*2 + (y2c - y1c)*2)
                color = (0,0,255) if distance < DISTANCE_THRESHOLD else (255,255,0)
                cv2.line(frame, centers[i], centers[j], color, 2)
                if distance < DISTANCE_THRESHOLD:
                    close_pairs += 1

        crowd_detected = close_pairs >= 1

        # Display people count + crowd
        cv2.putText(frame,
                    f"People Count: {people_count}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0,255,255), 3)
        if crowd_detected:
            cv2.putText(frame,
                        "CROWD DETECTED!",
                        (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0,0,255), 3)

        # Show live frame
        cv2.imshow("AI Surveillance", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# Start YOLO thread
threading.Thread(target=run_yolo, daemon=True).start()

# ==============================
# API
# ==============================
@app.route("/status")
def status():
    return jsonify({
        "people_count": people_count,
        "crowd_detected": crowd_detected,
        "alerts_count": len(alerts)
    })

@app.route("/alerts")
def get_alerts():
    return jsonify(alerts)

# ==============================
# Run server
# ==============================
if __name__ == "__main__":
    # Use your laptop IP so phone can connect
    app.run(host="0.0.0.0", port=5000)