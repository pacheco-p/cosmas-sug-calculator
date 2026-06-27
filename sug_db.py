import sqlite3
import hashlib
import os

# Secure pepper from your environment variables to protect student data
PEPPER = os.environ.get("PCA_PEPPER", "DEFAULT_SECURE_KEY")

def init_db():
    """Initializes the database and creates the students table."""
    conn = sqlite3.connect("sug_portal.db")
    c = conn.cursor()
    # Table stores username, hashed password, and the latest CGPA
    c.execute('''CREATE TABLE IF NOT EXISTS students 
                 (username TEXT PRIMARY KEY, password TEXT, cgpa REAL)''')
    conn.commit()
    conn.close()

def save_cgpa(username, cgpa):
    """Updates the CGPA for a specific student in the database."""
    conn = sqlite3.connect("sug_portal.db")
    c = conn.cursor()
    c.execute("UPDATE students SET cgpa = ? WHERE username = ?", (cgpa, username))
    conn.commit()
    conn.close()

def hash_password(password):
    """Hashes passwords using the PCA_PEPPER for security."""
    salted_pass = password + PEPPER
    return hashlib.sha256(salted_pass.encode()).hexdigest()