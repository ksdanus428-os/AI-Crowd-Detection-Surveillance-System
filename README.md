AI SURVEILLANCE SYSTEM FOR CROWD DETECTION

An AI-powered surveillance system designed for real-time person detection, person tracking, crowd detection, presence monitoring, and automated snapshot alerts.

This project combines a Python-based computer vision backend with a React Native mobile application. The Python backend processes camera input using YOLO and OpenCV, while Flask provides REST API endpoints for communication with the mobile dashboard.

--------------------------------------------------
1. PROJECT OVERVIEW
--------------------------------------------------

The AI Surveillance System for Crowd Detection is designed to monitor people through a camera and identify crowding conditions based on the proximity between detected individuals.

The system performs the following major operations:

1. Captures live video from a camera.
2. Detects people using the YOLO object detection model.
3. Tracks detected people using unique tracking IDs.
4. Calculates the distance between detected individuals.
5. Detects crowding when people are within the configured proximity.
6. Tracks the presence duration of detected individuals.
7. Generates snapshots at configured intervals.
8. Provides surveillance information through a Flask REST API.
9. Displays surveillance information through a React Native mobile dashboard.

--------------------------------------------------
2. FEATURES
--------------------------------------------------

PERSON DETECTION

- Detects people from a live camera feed.
- Uses the YOLO object detection model.
- Processes video frames using OpenCV.

PERSON TRACKING

- Assigns tracking IDs to detected individuals.
- Maintains tracking information while individuals remain visible.

CROWD DETECTION

- Calculates the distance between detected people.
- Checks whether individuals are within the configured proximity.
- Updates the crowd detection status when a crowding condition is detected.

PRESENCE MONITORING

- Tracks the presence duration of detected individuals.
- Maintains information for individual tracking IDs.

SNAPSHOT GENERATION

- Generates snapshots based on configured surveillance conditions.
- Stores generated snapshots locally.
- The snapshots directory is excluded from Git.

FLASK REST API

- Provides surveillance information through REST API endpoints.
- Allows the mobile application to retrieve the current system status.
- Provides access to generated alerts.

MOBILE DASHBOARD

The React Native mobile application displays:

- Number of people detected.
- Crowd detection status.
- Surveillance information.
- Snapshot alerts.

REAL-TIME MONITORING

- The mobile application communicates with the Flask backend.
- The dashboard retrieves the latest surveillance information from the backend.

--------------------------------------------------
3. SYSTEM WORKFLOW
--------------------------------------------------

Camera Feed → Frame Capture → YOLOv8 Person Detection → Person Tracking → Distance Calculation → Crowd Detection → Alert Generation → Flask API → React Native Dashboard

--------------------------------------------------
4. SYSTEM COMPONENTS
--------------------------------------------------

The project consists of two main components.

BACKEND

The Python backend is responsible for:

- Camera input.
- Video processing.
- Person detection.
- Person tracking.
- Crowd detection.
- Presence monitoring.
- Snapshot generation.
- REST API communication.

FRONTEND

The React Native application is responsible for:

- Communicating with the Flask backend.
- Displaying the number of detected people.
- Displaying crowd detection status.
- Displaying surveillance alerts.
- Monitoring snapshot alerts.

--------------------------------------------------
5. TECHNOLOGIES USED
--------------------------------------------------

ARTIFICIAL INTELLIGENCE AND COMPUTER VISION

- Python
- YOLO
- Ultralytics
- OpenCV

BACKEND

- Flask
- Python REST API

MOBILE APPLICATION

- React Native
- Expo
- JavaScript

DEVELOPMENT TOOLS

- Visual Studio Code
- Git
- GitHub
- npm
- pip

--------------------------------------------------
6. YOLO MODEL
--------------------------------------------------

The project uses the following YOLO model:

yolov8n.pt

The model is included in the repository.

Model location:

technozoa_project/yolov8n.pt

The Python backend loads the YOLO model from the project directory.

--------------------------------------------------
7. PROJECT STRUCTURE
--------------------------------------------------

AI-Surveillance-System-for-Crowd-Detection/

    .gitignore
    README.md
    requirements.md
    App.js
    app.json
    eslint.config.js
    package.json
    package-lock.json
    run_all.bat
    tsconfig.json

    app/
        (tabs)/
        _layout.tsx
        modal.tsx

    assets/
        images/

    components/

    constants/

    hooks/

    scripts/

    technozoa_project/
        main.py
        server.py
        yolov8n.pt

--------------------------------------------------
8. REQUIREMENTS
--------------------------------------------------

The following software is required to run the project:

- Windows or another compatible operating system.
- Python.
- Node.js.
- npm.
- Expo.
- React Native.
- Required Python packages.
- Required JavaScript packages.
- A working camera.
- Android device or another compatible Expo environment.
- Computer and mobile device connected to the same network.

Detailed installation and dependency information can be provided in requirements.md.

--------------------------------------------------
9. INSTALLATION
--------------------------------------------------

STEP 1: CLONE THE REPOSITORY

Clone the project from GitHub:

git clone https://github.com/ksdanus428-os/AI-Surveillance-System-for-Crowd-Detection.git

STEP 2: ENTER THE PROJECT DIRECTORY

cd AI-Surveillance-System-for-Crowd-Detection

STEP 3: INSTALL JAVASCRIPT DEPENDENCIES

Run:

npm install

This installs the dependencies required by the React Native and Expo application.

STEP 4: INSTALL PYTHON DEPENDENCIES

Navigate to the backend directory:

cd technozoa_project

Install the required Python packages:

pip install -r requirements.txt

--------------------------------------------------
10. RUNNING THE PROJECT
--------------------------------------------------

The project requires both the Python backend and the React Native application to run.

BACKEND

Navigate to:

technozoa_project/

Run:

python server.py

The Flask server will start and provide the surveillance API.

FRONTEND

Open another terminal in the main project directory:

npx expo start

Expo will start the development server.

The application can then be opened on a compatible mobile device.

--------------------------------------------------
11. RUNNING USING run_all.bat
--------------------------------------------------

The project contains a batch file:

run_all.bat

This file can be used to start the backend and Expo development server.

Run:

run_all.bat

The script starts:

1. Python Flask server.
2. Expo development server.

--------------------------------------------------
12. NETWORK CONFIGURATION
--------------------------------------------------

The mobile application communicates with the Flask server through the local network.

The computer running the Flask server and the mobile device must be connected to the same network.

The server IP address configured in App.js must match the current local IP address of the computer running the Flask server.

Example:

const SERVER_IP = "192.168.1.103";

Replace the example IP address with the current IP address of the computer.

--------------------------------------------------
13. API ENDPOINTS
--------------------------------------------------

STATUS API

Method:

GET

Endpoint:

/status

Purpose:

Returns the current surveillance status.

The response contains information such as:

- Number of detected people.
- Crowd detection status.

Example response:

{
    "people_count": 0,
    "crowd_detected": false
}

--------------------------------------------------

ALERTS API

Method:

GET

Endpoint:

/alerts

Purpose:

Returns surveillance alerts generated by the system.

The React Native application uses this endpoint to retrieve alert information.

--------------------------------------------------
14. CROWD DETECTION
--------------------------------------------------

The system determines crowding based on the distance between detected individuals.

The backend obtains the positions of detected people and calculates the distance between them.

When individuals are detected within the configured proximity, the crowd detection status is updated.

The configured detection conditions can be modified in the Python backend according to the requirements of the project.

--------------------------------------------------
15. PERSON TRACKING
--------------------------------------------------

The system assigns tracking IDs to detected people.

Tracking allows the system to maintain information about individuals across multiple video frames.

The tracking information can be used for:

- Identifying individual detections.
- Monitoring presence duration.
- Supporting crowd analysis.
- Generating surveillance information.

--------------------------------------------------
16. SNAPSHOTS
--------------------------------------------------

The system can generate snapshots during surveillance.

Generated snapshots are stored locally in:

snapshots/

The snapshots directory is excluded from Git using .gitignore.

This prevents generated surveillance images from being uploaded to the public GitHub repository.

--------------------------------------------------
17. MOBILE DASHBOARD
--------------------------------------------------

The React Native mobile application provides a mobile interface for monitoring the surveillance system.

The dashboard can display:

- Current number of detected people.
- Current crowd detection status.
- Surveillance alerts.
- Snapshot alert information.

The application communicates with the Flask backend using HTTP requests.

--------------------------------------------------
18. SECURITY AND PRIVACY
--------------------------------------------------

This project processes camera input and may generate images containing people.

When using this system:

- Do not upload private camera footage.
- Do not upload personal photographs.
- Do not upload passwords.
- Do not upload API keys.
- Do not upload authentication tokens.
- Do not upload private configuration files.
- Do not upload .env files containing secrets.
- Do not upload confidential information.

The project .gitignore file is configured to exclude common temporary, generated, and sensitive files.

Users should operate the system responsibly and follow applicable laws, regulations, and institutional policies.

--------------------------------------------------
19. DEVELOPMENT
--------------------------------------------------

This project is intended for development, experimentation, and educational purposes.

The system can be extended with additional computer vision, analytics, monitoring, and mobile application features.

Possible future improvements include:

- Improved crowd analysis.
- Improved person tracking.
- Advanced alert management.
- Historical surveillance statistics.
- Additional analytics.
- Improved mobile dashboard.
- Multiple camera support.
- Database integration.
- User authentication.
- Cloud deployment.
- Advanced reporting.

--------------------------------------------------
20. PROJECT STATUS
--------------------------------------------------

Project Status:

ACTIVE DEVELOPMENT

Current functionality includes:

- Person detection.
- Person tracking.
- Crowd detection.
- Presence monitoring.
- Snapshot generation.
- Flask REST API.
- React Native mobile dashboard.

Additional features may be added in future versions.

--------------------------------------------------
21. TEAM MEMBERS
--------------------------------------------------

Project Team:

- Danus K S
- MANOJ KUMAR M K S
- SAGAR M
- SUNDARABALAN S P

Additional contributors can be added as the project develops.

--------------------------------------------------
22. GITHUB REPOSITORY
--------------------------------------------------

Repository:

https://github.com/ksdanus428-os/AI-Surveillance-System-for-Crowd-Detection

The repository contains the source code, YOLO model, mobile application, backend, configuration files, and project documentation.

--------------------------------------------------
23. ACKNOWLEDGEMENTS
--------------------------------------------------

This project uses open-source technologies and libraries including:

- Python
- YOLO
- Ultralytics
- OpenCV
- Flask
- React Native
- Expo

--------------------------------------------------
24. LICENSE
--------------------------------------------------

This project is currently provided for educational and development purposes.

A formal open-source license can be added to the repository in the future if the project is released under a specific license.

--------------------------------------------------
25. CONTACT
--------------------------------------------------

For questions, suggestions, issues, or collaboration, use the GitHub repository's issue and collaboration features.

--------------------------------------------------

AI SURVEILLANCE SYSTEM FOR CROWD DETECTION

Built using Python, YOLO, OpenCV, Flask, React Native, and Expo.
