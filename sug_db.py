import sqlite3
import streamlit as st
import hashlib
import os

# Secure pepper from your environment variables
PEPPER = os.environ.get("PCA_PEPPER", "DEFAULT_SECURE_KEY")

def init_db():
    conn = sqlite3.connect("sug_portal.db")
    c = conn.cursor()
    # Create table for students
    c.execute('''CREATE TABLE IF NOT EXISTS students 
                 (username TEXT PRIMARY KEY, password TEXT, cgpa REAL)''')
    conn.commit()
    conn.close()

def save_cgpa(username, cgpa):
    conn = sqlite3.connect("sug_portal.db")
    c = conn.cursor()
    c.execute("UPDATE students SET cgpa = ? WHERE username = ?", (cgpa, username))
    conn.commit()
    conn.close()

def hash_password(password):
    # Using your PCA_PEPPER for an extra layer of security
    salted_pass = password + PEPPER
    return hashlib.sha256(salted_pass.encode()).hexdigest()
