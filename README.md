# Password Manager

## Overview
This project is a secure password manager application designed to store and manage passwords safely. It uses encryption to protect sensitive data and provides utilities for password generation and management.

## Features
- **Secure Storage**: Passwords are stored in an encrypted database.
- **Key Management**: A key file is used for encryption and decryption.
- **Password Generation**: Generate strong and secure passwords.
- **Cross-Platform**: Compatible with Linux and other operating systems.

## Project Structure
```
crypto_utils.py       # Handles encryption and decryption
password_utils.py     # Utilities for password generation and validation
db.py                 # Database operations
main.py               # Entry point of the application
requirements.txt      # Python dependencies
passwords.db          # Encrypted database file
keyfile.key           # Encryption key file
build/                # PyInstaller build artifacts
__pycache__/          # Python bytecode cache
```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd pass_manager
   ```
3. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   python main.py
   ```
2. Follow the prompts to manage your passwords.

## Notes
- Ensure the `keyfile.key` is kept secure and backed up.
- The `passwords.db` file contains encrypted data and should not be shared.

## Development
To build the application using PyInstaller:
```bash
pyinstaller --onefile main.py
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
