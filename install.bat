@echo off
REM A.R.Y.A Installation Script for Windows
REM Automated Railway Reservation System

title A.R.Y.A Installation
cls

echo ================================
echo A.R.Y.A Installation Script
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python 3.8 or higher from https://www.python.org
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo OK Python found

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: pip is not installed.
    echo Please install Python properly.
    pause
    exit /b 1
)

echo OK pip found

REM Install dependencies
echo.
echo Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

cls
echo ======================================
echo Installation completed successfully!
echo ======================================
echo.
echo You can now run the application:
echo   python main.py
echo.
pause
