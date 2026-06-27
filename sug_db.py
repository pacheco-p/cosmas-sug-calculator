import sqlite3
import bcrypt

def init_db():
    conn = sqlite3.connect("sug_portal.db")
    c = conn.cursor()
    # Storing student data
    c.execute('''CREATE TABLE IF NOT EXISTS students 
                 (username TEXT PRIMARY KEY, password TEXT, total_units REAL, total_points REAL)''')
    conn.commit()
    conn.close()
