import sqlite3
import bcrypt # Using bcrypt for superior security

def init_db():
    conn = sqlite3.connect("sug_portal.db")
    c = conn.cursor()
    # Storing cumulative totals for proper CGPA tracking
    c.execute('''CREATE TABLE IF NOT EXISTS students 
                 (username TEXT PRIMARY KEY, password TEXT, total_units REAL, total_points REAL)''')
    conn.commit()
    conn.close()

def update_academic_record(username, new_units, new_points):
    conn = sqlite3.connect("sug_portal.db")
    c = conn.cursor()
    c.execute("SELECT total_units, total_points FROM students WHERE username = ?", (username,))
    row = c.fetchone()
    
    # Calculate cumulative values
    curr_u, curr_p = row if row else (0, 0)
    c.execute("INSERT OR REPLACE INTO students VALUES (?, ?, ?, ?)", 
              (username, "EXISTING_HASH", curr_u + new_units, curr_p + new_points))
    conn.commit()
    conn.close()
