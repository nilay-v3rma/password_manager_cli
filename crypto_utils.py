from cryptography.fernet import Fernet
import os

def generate_master_key(filename="keyfile.key"):
    if not os.path.exists(filename):
        key = Fernet.generate_key()
        with open(filename, "wb") as file:
            file.write(key)
    else:
        with open(filename, "rb") as file:
            key = file.read()
    return Fernet(key)

def encrypt_data(data, cipher):
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(data, cipher):
    return cipher.decrypt(data.encode()).decode()
