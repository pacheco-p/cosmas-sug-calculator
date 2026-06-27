import streamlit as st
import sug_db

st.set_page_config(page_title="Cosmas @ SUG")

# Dashboard UI
st.title(f"👋 Welcome, {st.session_state.get('user', {}).get('username', 'Student').capitalize()}")
col1, col2 = st.columns(2)
col1.metric("Latest CGPA", "4.63")
col2.metric("Account Status", "Active")
st.write("Last Updated: Today")

# Campaign Info Sidebar
st.sidebar.title("🏛️ COSMAS FOR SUG")
st.sidebar.markdown("""
### Vision
• Academic Excellence
• Student Welfare
• Transparency
• Effective Representation
""")
