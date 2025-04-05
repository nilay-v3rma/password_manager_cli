import sqlite3
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
DB_FILE = os.getenv('DB_FILE')

def initialize_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            service TEXT NOT NULL,
            username TEXT,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_password(service, username, encrypted_password):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
        (service, username, encrypted_password),
    )
    conn.commit()
    conn.close()

def get_password(service):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM passwords WHERE service = ?", (service,))
    results = cursor.fetchall() 
    conn.close()
    return results

def delete_password(service, username):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE service = ? AND username = ?", (service, username))
    conn.commit()
    conn.close()

def get_all_passwords():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT service, username, password FROM passwords")
    results = cursor.fetchall()
    conn.close()
    return results

def delete_all_passwords():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords")
    conn.commit()
    conn.close()



