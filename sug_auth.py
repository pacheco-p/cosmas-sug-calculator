import streamlit as st
import sug_db
import sqlite3

def verify_user(username, password):
    """Verifies credentials against the database."""
    conn = sqlite3.connect("sug_portal.db")
    c = conn.cursor()
    hashed_pw = sug_db.hash_password(password)
    c.execute("SELECT * FROM students WHERE username = ? AND password = ?", (username, hashed_pw))
    user = c.fetchone()
    conn.close()
    return user

def register_user(username, password):
    """Registers a new user in the database."""
    conn = sqlite3.connect("sug_portal.db")
    c = conn.cursor()
    hashed_pw = sug_db.hash_password(password)
    try:
        c.execute("INSERT INTO students (username, password, cgpa) VALUES (?, ?, ?)", (username, hashed_pw, 0.0))
        conn.commit()
        success = True
    except sqlite3.IntegrityError:
        success = False
    conn.close()
    return success

def render_login():
    """Displays the Login form."""
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        if submit:
            user = verify_user(username, password)
            if user:
                st.session_state["user"] = {"username": username}
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")

def render_signup():
    """Displays the Sign Up form."""
    with st.form("signup_form"):
        username = st.text_input("Choose Username")
        password = st.text_input("Choose Password", type="password")
        submit = st.form_submit_button("Sign Up")
        if submit:
            if register_user(username, password):
                st.success("Account created! Please login.")
            else:
                st.error("Username already exists.")