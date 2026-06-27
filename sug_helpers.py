import streamlit as st

def calculate_cgpa(courses):
    total_points = 0
    total_units = 0
    for course in courses:
        # Assuming grade points: A=5, B=4, C=3, D=2, E=1, F=0
        points = course['grade'] * course['units']
        total_points += points
        total_units += course['units']
    
    return total_points / total_units if total_units > 0 else 0

def render_calculator():
    st.subheader("📊 Cosmas @ SUG CGPA Calculator")
    
    # Simple form to add courses
    with st.form("cgpa_form"):
        num_courses = st.number_input("Number of Courses", min_value=1, max_value=15, value=5)
        courses = []
        for i in range(num_courses):
            col1, col2 = st.columns(2)
            with col1:
                units = st.number_input(f"Units {i+1}", min_value=1, max_value=6, key=f"u{i}")
            with col2:
                grade = st.selectbox(f"Grade {i+1}", [5, 4, 3, 2, 1, 0], format_func=lambda x: ["A", "B", "C", "D", "E", "F"][5-x], key=f"g{i}")
            courses.append({"units": units, "grade": grade})
        
        submitted = st.form_submit_button("Calculate CGPA")
        
    if submitted:
        result = calculate_cgpa(courses)
        st.success(f"Your calculated GPA is: {result:.2f}")
