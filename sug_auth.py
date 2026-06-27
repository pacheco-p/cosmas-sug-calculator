import streamlit as st
import sug_db

def render_login():
    st.subheader("Login to your SUG Account")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            # Here you would verify the hash against the database
            hashed_pw = sug_db.hash_password(password)
            st.success("Login logic triggered for: " + username)
            # You would add your database validation check here

def render_signup():
    st.subheader("Create a New Account")
    with st.form("signup_form"):
        username = st.text_input("Choose Username")
        password = st.text_input("Choose Password", type="password")
        submit = st.form_submit_button("Sign Up")
        
        if submit:
            hashed_pw = sug_db.hash_password(password)
            st.success("Account created for: " + username)
            # You would add your database insertion logic here
