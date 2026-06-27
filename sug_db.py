import sqlite3
import bcrypt

def init_db():
    conn = sqlite3.connect("sug_portal.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students 
                 (username TEXT PRIMARY KEY, password TEXT, total_units REAL, total_points REAL)''')
    conn.commit()
    conn.close()

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)
