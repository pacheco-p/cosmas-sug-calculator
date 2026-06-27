import streamlit as st
import sug_db
import sug_auth
import sug_helpers

# Page Configuration
st.set_page_config(page_title="Cosmas @ SUG Portal", page_icon="🏛️", layout="centered")

# Initialize Database
sug_db.init_db()

# Premium Campaign CSS (Branding: 1003117546.jpg)
st.markdown("""
<style>
    .stApp { background-color: #0b1c34; }
    h1 { color: #e0f2ff; text-align: center; font-weight: 800; margin-bottom: 5px; }
    .sug-motto { text-align: center; color: #b0c4de; font-style: italic; font-size: 18px; margin-bottom: 30px; }
    .main-container { background-color: #ffffff; padding: 30px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>COSMAS AT SUG TOP SEAT</h1>", unsafe_allow_html=True)
st.markdown("<p class='sug-motto'>Support, Pray, Canvass!</p>", unsafe_allow_html=True)

# Authentication State
if "user" not in st.session_state: st.session_state["user"] = None

# Main Logic
if st.session_state["user"] is None:
    # Login/Signup Gateway
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    with tab1: sug_auth.render_login()
    with tab2: sug_auth.render_signup()
else:
    # Authenticated Portal
    with st.sidebar:
        st.title("Navigation")
        menu = st.radio("Go to", ["Dashboard", "CGPA Calculator", "Campaign Info"])
        if st.button("Logout"):
            st.session_state["user"] = None
            st.rerun()

    if menu == "Dashboard":
        st.subheader("Welcome to the Portal")
        st.write(f"Logged in as: {st.session_state['user']}")
    elif menu == "CGPA Calculator":
        sug_helpers.render_calculator()
    elif menu == "Campaign Info":
        st.subheader("About the Movement")
        st.markdown("**Support, Pray, Canvass!** - Ensuring academic excellence for EKSU.")