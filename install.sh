#!/bin/bash

# A.R.Y.A Installation Script
# Automated Railway Reservation System

echo "================================"
echo "A.R.Y.A Installation Script"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip."
    exit 1
fi

echo "✓ pip found: $(pip3 --version)"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Dependencies installed successfully!"
    echo ""
    echo "You can now run the application with:"
    echo "  python3 main.py"
    echo ""
else
    echo "❌ Failed to install dependencies"
    exit 1
fi
