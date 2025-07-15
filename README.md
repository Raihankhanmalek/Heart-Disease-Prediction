# ❤️ Heart Disease Prediction Web App

A simple, interactive web application built with **Streamlit** that predicts the risk of heart disease based on patient data using a **Logistic Regression model** trained on the UCI Heart Disease dataset.

<div align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--learn-blue?logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Web%20App-Streamlit-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/Made%20with-Python-blue?logo=python" />
</div>

---

## 🚀 Demo

🔗 **Live App**: [Click here to try it out](https://your-app-name.streamlit.app)

---

## 🧠 Features

- Interactive UI for user input
- Predicts risk of heart disease (low / high)
- Shows probability of prediction
- Uses Logistic Regression model
- Clean 2-column layout with emoji-enhanced labels
- Deployable on **Streamlit Cloud**

---

## 📊 Input Features

| Feature           | Description                            |
|------------------|----------------------------------------|
| Age              | Age of the person                      |
| Sex              | 0 = Female, 1 = Male                   |
| Chest Pain Type  | 0–3 (4 types of chest pain)            |
| Resting BP       | Resting blood pressure                 |
| Cholesterol      | Serum cholesterol in mg/dl             |
| Fasting Sugar    | >120 mg/dl (0 = No, 1 = Yes)           |
| ECG              | Resting electrocardiographic results   |
| Max Heart Rate   | Maximum heart rate achieved            |
| Exercise Angina  | Exercise-induced angina (0 = No, 1 = Yes) |
| ST Depression    | ST depression induced by exercise      |
| Slope            | Slope of peak exercise ST segment      |
| CA               | Major vessels colored by fluoroscopy   |
| Thal             | 0–3 (0 = normal, 1 = fixed, 2 = reversible) |

---

## 🧰 Tech Stack

- Python 3.x
- Pandas, NumPy
- Scikit-learn (Logistic Regression)
- Streamlit (for UI)
- Joblib (to save/load models)

---

## 📁 Folder Structure

```
heart-disease-predictor/
├── streamlit_app.py           # Streamlit web app UI
├── heart_disease_model.pkl    # Trained machine learning model
├── scaler.pkl                 # StandardScaler for preprocessing
├── requirements.txt           # List of Python dependencies
└── README.md                  # Project documentation (this file)
```

---

## ⚙️ Installation (Run Locally)

```bash
# Clone the repo
git clone https://github.com/your-username/heart-disease-predictor.git

# Navigate into the folder
cd heart-disease-predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

---

## ☁️ Deployment

This app is deployed using [Streamlit Cloud](https://streamlit.io/cloud):

1. Push your project to a GitHub repo
2. Create an account on Streamlit Cloud
3. Click "Deploy an app", connect GitHub, and select this repo
4. Set `streamlit_app.py` as the main file
5. Done! 🚀

---

## 📬 Contact

Made with ❤️ by [Raihankhan Malek](https://www.linkedin.com/in/raihankhanmalek)  
📫 Email: raihankhanmalek@gmail.com

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
