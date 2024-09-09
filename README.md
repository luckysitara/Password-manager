# Password Manager

## Overview

The Password Manager is a simple command-line tool that allows users to generate strong passwords and check the strength of existing passwords. It incorporates the RockYou wordlist for checking against common passwords and uses a password policy to ensure strength. Additionally, it estimates the brute-force attack time for given passwords.

## Features

- Generate passwords with various character combinations.
- Check password strength against a predefined policy and the RockYou wordlist.
- Estimate brute-force attack time.
- User-friendly command-line interface with a menu for ease of use.

## Requirements

- Python 3.x
- `password-strength` library
- `pyfiglet` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/password-manager.git
    cd password-manager
    ```

2. **Install Python dependencies:**

    Create a `requirements.txt` file with the following content:

    ```
    password-strength==0.9.0
    pyfiglet==0.8.post1
    ```

    Then, install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

3. **Download and set up the RockYou wordlist:**

    ```bash
    ./setup.sh
    ```

    Ensure `setup.sh` contains the necessary script to download and extract `rockyou.txt`. Example:

    ```bash
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

    # Installing requirements.txt
    pip install -r requirements.txt

    # Make the Python script executable
    echo "Making $PYTHON_SCRIPT executable..."
    chmod +x $PYTHON_SCRIPT

    # Execute the Python script
    echo "Running $PYTHON_SCRIPT..."
    ./$PYTHON_SCRIPT
    ```

## Usage

1. **Run the Python script:**

    ```bash
    python python_script.py
    ```

2. **Interact with the menu:**

    - **Check password strength:** Enter the password you want to check. The tool will provide feedback on its strength.
    - **Generate a strong password:** Choose the type and length of the password you want to generate.
    - **Exit:** Choose this option to exit the program.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [RockYou wordlist](https://github.com/danielmiessler/SecLists) for common passwords.
- [pyfiglet](https://pypi.org/project/pyfiglet/) for ASCII art in the command-line interface.
- [password-strength](https://pypi.org/project/password-strength/) for password policy enforcement.

## Contact

For any questions or issues, please contact [bughackerjanaan@gmail.com](mailto:bughackerjanaan@gmail.com)
