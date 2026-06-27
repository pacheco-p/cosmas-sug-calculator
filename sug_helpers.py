import streamlit as st
import sug_db

def calculate_cgpa(courses):
    """Calculates CGPA based on unit weights and grade points."""
    total_points = 0
    total_units = 0
    for course in courses:
        # course['grade'] is the point value (5, 4, 3, 2, 1, 0)
        points = course['grade'] * course['units']
        total_points += points
        total_units += course['units']
    
    return total_points / total_units if total_units > 0 else 0

def render_calculator():
    """Renders the interactive calculator UI."""
    st.subheader("📊 Cosmas @ SUG CGPA Calculator")
    
    with st.form("cgpa_form"):
        num_courses = st.number_input("Number of Courses", min_value=1, max_value=15, value=5)
        courses = []
        
        for i in range(num_courses):
            col1, col2 = st.columns(2)
            with col1:
                units = st.number_input(f"Units {i+1}", min_value=1, max_value=6, value=3, key=f"u{i}")
            with col2:
                # Grade mapping for the user
                grade_map = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}
                grade_char = st.selectbox(f"Grade {i+1}", list(grade_map.keys()), key=f"g{i}")
                grade_val = grade_map[grade_char]
            courses.append({"units": units, "grade": grade_val})
        
        submitted = st.form_submit_button("Calculate & Save Result")
        
    if submitted:
        result = calculate_cgpa(courses)
        st.success(f"Your calculated CGPA is: {result:.2f}")
        
        # Save to database if user is logged in
        if st.session_state["user"]:
            sug_db.save_cgpa(st.session_state["user"]["username"], result)
            st.info("Result saved to your profile!")