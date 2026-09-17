@echo off
echo Starting AI Surveillance System...

REM ---- Start Flask Server ----
start cmd /k "cd technozoa_project && python server.py"

REM ---- Small Delay ----
timeout /t 3 >nul

REM ---- Start Expo App ----
start cmd /k "npx expo start"

echo Both Server and Expo are starting...