# Student-Performance-Prediction-using-Machine-Learning

This project aims to predict a student’s **final grade (G3)** using various socio-demographic, academic, and behavioral attributes from the UCI Student Performance Dataset.

---

## 📂 Dataset

We use the dataset from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Student+Performance) which contains information about students’ academic performance in two Portuguese schools.

- `student-mat.csv` – Math course student data  
- `student-por.csv` – Portuguese language course student data

Each row includes 30+ features such as:
- Age, Address, Study Time
- Failures, Alcohol Consumption, Going Out Frequency
- First & Second Period Grades (G1, G2)
- Final Grade (G3 - Target)

📁 Dataset paths used:
D:/ML PROJECTS/Student Performance Prediction using ML/student-mat.csv

yaml
Copy
Edit

---

## 🧠 Problem Statement

> Predict a student’s **final exam grade (G3)** based on:
- Academic performance (G1, G2)
- Personal and social background
- Lifestyle and behavioral factors

---

## 🛠️ Workflow

1. 📊 **Data Preprocessing**
   - Handle categorical & numerical variables
   - Label Encoding
   - Feature Selection

2. 📈 **Exploratory Data Analysis (EDA)**  
   - Distribution of G3
     ![image](https://github.com/user-attachments/assets/f9c61f1d-1d72-41ee-9dc4-6c0b836b7c64)

   - Correlation heatmap
     ![image](https://github.com/user-attachments/assets/b3a1c08e-c9e6-4d08-b954-48e75cf92517)

  ![image](https://github.com/user-attachments/assets/3370f996-7f87-4dee-8794-5297e2a6c365)



yaml
Copy
Edit

3. 🤖 **Model Training**
- Algorithm: `RandomForestRegressor`
- Target: G3 (Final Grade)
- Evaluation Metrics: MAE, RMSE, R²

---

## ✅ Model Performance

| Metric   | Score  |
|----------|--------|
| MAE      | 1.11   |
| RMSE     | 1.87   |
| R² Score | 0.83   |

📋 Interpretation:
- On average, predictions deviate by ~1.1 points from the actual grade.
- The model explains **83%** of the variance in student performance.

---

## 💻 Streamlit Web App

We’ve built a user-friendly **Streamlit UI** where you can input a student’s academic details and get a **predicted final grade**.

📌 Launch the app:

```bash
streamlit run "student_app.py"

![image](https://github.com/user-attachments/assets/08413874-d2aa-4b59-9c9a-426e53d69bc0)

css
Copy
Edit
![image](https://github.com/user-attachments/assets/e33bac59-8dc8-45cc-b57f-7ffa632ecacb)

🗂️ File Structure
Copy
Edit
├── student-mat.csv
├── student_model.pkl
├── student_app.py
├── README.md
🔍 Future Improvements
Add separate models for classification (pass/fail) and regression (score)

Incorporate feature engineering like weighted G1/G2 influence

Experiment with other algorithms: XGBoost, GradientBoost, etc.

Add more user interactivity to the frontend

📚 References
UCI Student Dataset

Streamlit Docs

Scikit-learn

🧑‍💻 Author
Developed by Yuvan Krishnan
