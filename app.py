import streamlit as st
import pandas as pd
import joblib

# Page settings
st.set_page_config(
    page_title="Student Attendance Prediction",
    page_icon="🎓",
    layout="wide"
)

# Load trained model
model = joblib.load("attendance_prediction_model.pkl")

# Title
st.title("🎓 Student Attendance Prediction System")
st.write(
    "AI-based system to predict student attendance "
    "and identify attendance risk."
)

st.divider()

# Student inputs
st.header("📋 Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=15, max_value=30, value=20)

    semester = st.number_input(
        "Semester",
        min_value=1,
        max_value=8,
        value=5
    )

    total_classes = st.number_input(
        "Total Classes",
        min_value=1,
        value=100
    )

    classes_attended = st.number_input(
        "Classes Attended",
        min_value=0,
        value=75
    )

    previous_month_attendance = st.number_input(
        "Previous Month Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=75.0
    )

    assignment_submission = st.number_input(
        "Assignment Submission (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0
    )

with col2:
    internal_marks = st.number_input(
        "Internal Marks",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

    practical_attendance = st.number_input(
        "Practical Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0
    )

    medical_leave = st.number_input(
        "Medical Leave",
        min_value=0,
        value=2
    )

    extracurricular_hours = st.number_input(
        "Extracurricular Hours",
        min_value=0.0,
        value=5.0
    )

    commute_time = st.number_input(
        "Commute Time (minutes)",
        min_value=0,
        value=30
    )

st.divider()

# Prediction button
if st.button("🔮 Predict Attendance", use_container_width=True):

    # Prepare input data
    input_data = pd.DataFrame({
        "Age": [age],
        "Semester": [semester],
        "Total_Classes": [total_classes],
        "Classes_Attended": [classes_attended],
        "Previous_Month_Attendance": [previous_month_attendance],
        "Assignment_Submission": [assignment_submission],
        "Internal_Marks": [internal_marks],
        "Practical_Attendance": [practical_attendance],
        "Medical_Leave": [medical_leave],
        "Extracurricular_Hours": [extracurricular_hours],
        "Commute_Time_Min": [commute_time]
    })

    # Predict attendance
    prediction = model.predict(input_data)[0]

    # Keep prediction between 0 and 100
    prediction = max(0, min(100, prediction))

    # Risk classification
    if prediction < 60:
        risk = "High Risk 🔴"
    elif prediction < 75:
        risk = "Medium Risk 🟠"
    else:
        risk = "Low Risk 🟢"

    # Current attendance
    current_attendance = (
        classes_attended / total_classes
    ) * 100

    # Display results
    st.subheader("📊 Prediction Result")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Predicted Attendance",
        f"{prediction:.2f}%"
    )

    col2.metric(
        "Risk Level",
        risk
    )

    col3.metric(
        "Current Attendance",
        f"{current_attendance:.2f}%"
    )

    # Required classes calculation
    if current_attendance < 75:

        required_classes = 0

        while (
            (classes_attended + required_classes)
            / (total_classes + required_classes)
        ) * 100 < 75:

            required_classes += 1

        st.info(
            f"📚 You need to attend approximately "
            f"{required_classes} consecutive classes "
            f"to reach 75% attendance."
        )

    else:
        st.success(
            "🎉 Current attendance is already above 75%."
        )