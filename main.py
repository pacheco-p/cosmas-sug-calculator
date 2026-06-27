import streamlit as st
import sug_db
import sug_auth
import sug_helpers

st.set_page_config(page_title="Cosmas @ SUG Portal", page_icon="🏛️", layout="wide")

# SUG Theme CSS
st.markdown("""
<style>
    h1 { color: #006400; text-align: center; } /* Dark Green for SUG */
    .sug-banner { background: #f0f8ff; padding: 20px; border-radius: 10px; border: 2px solid #006400; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🏛️ Cosmas @ SUG | Academic Progress Portal</h1>", unsafe_allow_html=True)

# Entry logic
if "user" not in st.session_state:
    st.session_state["user"] = None

if st.session_state["user"] is None:
    sug_auth.render_login()
else:
    sug_helpers.render_dashboard()
