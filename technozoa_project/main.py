import cv2
import time
import os
import math
from ultralytics import YOLO

# ==============================
# SETTINGS
# ==============================
SNAPSHOT_TIMES = [10, 30, 60, 180, 300, 420, 600]  # seconds
DISTANCE_THRESHOLD = 150  # pixels for close proximity
CROWD_THRESHOLD = 2       # number of people to consider as a crowd

# Create folder if not exists
if not os.path.exists("snapshots"):
    os.makedirs("snapshots")

# Load YOLO model
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

person_timers = {}
person_snapshot_times = {}

print("✅ AI Surveillance Started")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()

    # 🔥 TRACKING
    results = model.track(frame, persist=True)

    centers = []
    ids = []

    for r in results:
        if r.boxes is None or r.boxes.id is None:
            continue

        for box, track_id, cls in zip(r.boxes.xyxy, r.boxes.id, r.boxes.cls):
            # Only person class (COCO = 0)
            if int(cls) != 0:
                continue

            track_id = int(track_id)
            x1, y1, x2, y2 = map(int, box)

            # Safety clamp
            x1 = max(0, x1)
            y1 = max(0, y1)
            x2 = min(frame.shape[1], x2)
            y2 = min(frame.shape[0], y2)

            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            centers.append((cx, cy))
            ids.append(track_id)

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

            # ==============================
            # TIMER (NO RESET)
            # ==============================
            if track_id not in person_timers:
                person_timers[track_id] = current_time
                person_snapshot_times[track_id] = set()

            elapsed = int(current_time - person_timers[track_id])

            cv2.putText(frame,
                        f"ID {track_id}: {elapsed}s",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (255,0,0), 2)

            # ==============================
            # SNAPSHOT PER PERSON
            # ==============================
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

    # ==============================
    # PEOPLE COUNT
    # ==============================
    people_count = len(ids)

    # ==============================
    # DISTANCE CALCULATION & CROWD DETECTION
    # ==============================
    crowd_detected = False
    close_pairs = 0

    for i in range(len(centers)):
        for j in range(i+1, len(centers)):
            x1, y1 = centers[i]
            x2, y2 = centers[j]

            # Corrected distance formula
            distance = math.sqrt(((x2 - x1)*2 )+ ((y2 - y1)*2))

            # Draw line: red if too close, blue otherwise
            color = (0,0,255) if distance < DISTANCE_THRESHOLD else (255,255,0)
            cv2.line(frame, centers[i], centers[j], color, 2)

            # Count close pairs
            if distance < DISTANCE_THRESHOLD:
                close_pairs += 1

    if close_pairs >= 1:  # at least 2 people close
        crowd_detected = True

    # ==============================
    # DISPLAY COUNT + CROWD ALERT
    # ==============================
    cv2.putText(frame,
                f"People Count: {people_count}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,255),
                3)

    if crowd_detected:
        cv2.putText(frame,
                    "CROWD DETECTED!",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    3)

    # ==============================
    # SHOW FRAME
    # ==============================
    cv2.imshow("AI Surveillance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()