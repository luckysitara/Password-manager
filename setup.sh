#!/bin/bash

# Define the rockyou.txt URL and Python script file
ROCKYOU_URL="https://github.com/danielmiessler/SecLists/raw/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz"
ROCKYOU_FILE="rockyou.txt"
PYTHON_SCRIPT="python_script.py"

# Check if rockyou.txt exists in the current directory
if [ -f "$ROCKYOU_FILE" ]; then
    echo "rockyou.txt already exists."
else
    echo "rockyou.txt not found. Downloading it..."
    wget $ROCKYOU_URL -O rockyou.txt.tar.gz

    if [ $? -eq 0 ]; then
        echo "Download complete. Extracting rockyou.txt..."
        tar -xzf rockyou.txt.tar.gz
        rm rockyou.txt.tar.gz  # Clean up the compressed file
        echo "rockyou.txt extracted."
    else
        echo "Failed to download rockyou.txt. Please check your connection or the URL."
        exit 1
    fi
fi

# Check if the Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Python script $PYTHON_SCRIPT not found."
    exit 1
fi

#Installing requirements.txt
pip install -r requirements.txt
# Make the Python script executable
echo "Making $PYTHON_SCRIPT executable..."
chmod +x $PYTHON_SCRIPT

# Execute the Python script
echo "Running $PYTHON_SCRIPT..."
./$PYTHON_SCRIPT
