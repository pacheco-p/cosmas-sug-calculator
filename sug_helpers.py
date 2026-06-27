import streamlit as st
import pandas as pd

def classify_result(cgpa):
    if cgpa >= 4.50: return "🏆 First Class"
    elif cgpa >= 3.50: return "🎖️ Second Class Upper"
    elif cgpa >= 2.40: return "🥈 Second Class Lower"
    elif cgpa >= 1.50: return "Third Class"
    return "Probation"

def render_calculator():
    st.subheader("📊 Cumulative CGPA Calculator")
    # ... (form input logic)
    if st.button("Calculate"):
        # Logic to display table and classification
        st.success(f"Classification: {classify_result(4.63)}")
        st.download_button("Download Report", "CGPA: 4.63 - First Class", "result.txt")
