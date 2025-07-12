# 🧠 AI/ML for Networking - Cyberattack Detection Web App

This project is a Machine Learning-powered web application that identifies whether a given network-related text input (such as a log message or activity description) is likely to indicate a cyberattack. It uses a trained text classification model built with TF-IDF vectorization and is deployed via a Flask web server.

---

## 📂 Project Structure

AI-ML-for-Networking-main/
├── app.py                      → Main Flask web application  
├── attack_detection_model.pkl → Trained ML model  
├── tfidf_vectorizer.pkl       → Pre-fitted TF-IDF Vectorizer  
└── templates/
    └── index.html              → HTML template for the web interface

---

## ⚙️ Prerequisites

- Python 3.7 or higher  
- Flask library  
- Joblib for loading model and vectorizer  

---

## 🚀 Getting Started

1. Clone or download the repository  
2. Install required libraries using pip (Flask and Joblib)  
3. Run the web app using the Python file  
4. Open the provided local server URL in your browser to use the interface  

---

## 🧠 How It Works

- The user submits a network-related text input through a simple web form  
- The application uses a pre-trained TF-IDF vectorizer to convert the input into a numerical format  
- This vectorized input is passed to a trained ML model to make a prediction  
- The prediction indicates whether the input suggests an attack or not  
- The result is then displayed back to the user on the same page  

---

## 📈 Model Training (Not Included in Repository)

This repository includes only the pre-trained model and vectorizer. If you wish to train your own model, you can use a dataset containing network-related text inputs labeled as "attack" or "normal" and apply text vectorization and classification techniques.

---

## ✅ Example Inputs and Outputs

| Example Text Input                      | Predicted Label |
|----------------------------------------|------------------|
| Multiple failed login attempts         | Attack           |
| User successfully authenticated        | Normal           |
| Unusual outbound traffic detected      | Attack           |
| Ping request from internal machine     | Normal           |

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🙋‍♀️ Maintainer

**Damera Harika, Dasapalli Pravallika, Manchala Dinesh Kumar**  
Feel free to connect or raise issues for any suggestions or improvements.
