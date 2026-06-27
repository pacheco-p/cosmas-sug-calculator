import streamlit as st
import sug_db

# 1. Setup
st.set_page_config(page_title="Cosmas @ SUG", layout="wide")
sug_db.init_db()

# 2. Session State Initialization
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

# 3. Logic
if not st.session_state.logged_in:
    st.title("🔐 Login to Cosmas Portal")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if user:  # Basic check
            st.session_state.logged_in = True
            st.session_state.username = user
            st.rerun()
else:
    # Dashboard
    st.title(f"👋 Welcome, {st.session_state.username.capitalize()}")
    st.metric("Latest CGPA", "4.63")
    
    # Sidebar
    st.sidebar.title("🏛️ COSMAS FOR SUG")
    st.sidebar.markdown("### Vision\n• Academic Excellence\n• Student Welfare")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
