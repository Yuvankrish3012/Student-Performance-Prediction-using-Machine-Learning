import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("D:/ML PROJECTS/Student Performance Prediction using ML/student_model.pkl", "rb"))

st.set_page_config(page_title="📘 Student Grade Predictor")
st.title("🎓 Student Final Grade Prediction App")

st.markdown("Fill out the following student information to predict the **final exam score (G3)**.")

# Input widgets for user
age = st.slider("Age", 15, 22, 17)
studytime = st.selectbox("Weekly Study Time", options=[1, 2, 3, 4], format_func=lambda x: f"{x} - {'<2h' if x==1 else '2-5h' if x==2 else '5-10h' if x==3 else '>10h'}")
failures = st.slider("Past Class Failures", 0, 3, 0)
absences = st.slider("Number of Absences", 0, 50, 5)
goout = st.slider("Going Out with Friends (1-5)", 1, 5, 3)
Dalc = st.slider("Workday Alcohol Consumption (1-5)", 1, 5, 1)
Walc = st.slider("Weekend Alcohol Consumption (1-5)", 1, 5, 2)
G1 = st.slider("First Period Grade (0-20)", 0, 20, 10)
G2 = st.slider("Second Period Grade (0-20)", 0, 20, 12)

# Model expects 32 inputs, so we fill dummy values (or you can redesign your model)
input_data = np.array([age, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, studytime, failures, 1, 1, 1, 1, 1, 1,
                       1, 1, 1, goout, Dalc, Walc, 1, 1, absences, 1, G1, G2]).reshape(1, -1)

if st.button("Predict Final Grade (G3)"):
    prediction = model.predict(input_data)[0]
    st.success(f"🎯 Predicted Final Grade: **{round(prediction, 2)} / 20**")
