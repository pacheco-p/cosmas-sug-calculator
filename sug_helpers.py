import streamlit as st
import pandas as pd

def classify_result(cgpa):
    if cgpa >= 4.50: return "🏆 First Class"
    if cgpa >= 3.50: return "🎖️ Second Class Upper"
    if cgpa >= 2.40: return "🥈 Second Class Lower"
    if cgpa >= 1.50: return "Third Class"
    return "Probation"

def render_calculator():
    st.subheader("📊 Cumulative CGPA Calculator")
    # ... (form code remains similar)
    if submitted:
        # Calculate points and units
        df = pd.DataFrame(courses)
        total_units = df['units'].sum()
        total_points = (df['grade'] * df['units']).sum()
        gpa = total_points / total_units
        
        # Display Polished Table
        st.table(df)
        st.metric("GPA for this semester", f"{gpa:.2f}")
        st.success(f"Classification: {classify_result(gpa)}")
        
        # Download Button
        report = f"CGPA Report\nGPA: {gpa:.2f}\nClass: {classify_result(gpa)}"
        st.download_button("Download Report", report, "result.txt")
