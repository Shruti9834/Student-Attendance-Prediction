# AI-Based Student Attendance Prediction and Risk Analysis System

## 📌 Project Overview

This project is an AI-based Student Attendance Prediction and Risk Analysis System developed using Machine Learning.

The system predicts a student's future attendance percentage based on academic and attendance-related factors. It also identifies the student's attendance risk level and calculates the number of classes required to reach 75% attendance.

## 🎯 Objectives

* Predict future student attendance percentage.
* Identify attendance risk as Low, Medium, or High.
* Calculate the number of classes required to reach 75% attendance.
* Help students monitor and improve their attendance.
* Provide a simple and user-friendly web interface.

## 🤖 Machine Learning Model

**Random Forest Regressor** is used to predict future attendance percentage.

### Input Features

* Age
* Semester
* Total Classes
* Classes Attended
* Previous Month Attendance
* Assignment Submission
* Internal Marks
* Practical Attendance
* Medical Leave
* Extracurricular Hours
* Commute Time

### Output

* Predicted Future Attendance Percentage
* Attendance Risk Level
* Required Classes to Reach 75%

## 📊 Model Performance

* **MAE:** 4.52
* **MSE:** 33.27
* **R² Score:** 0.69

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit

## 📁 Project Files

* `app.py` – Streamlit web application
* `attendance_prediction_model.pkl` – Trained Machine Learning model
* `student_attendance_prediction_dataset.csv` – Dataset
* `Student_Attendance_Prediction.ipynb` – Google Colab/Jupyter Notebook
* `requirements.txt` – Required Python libraries
* `README.md` – Project documentation

## 🚀 How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 👩‍💻 Project

**Student Attendance Prediction and Risk Analysis System**

Developed as an academic Machine Learning project.
# Student-Attendance-Prediction
