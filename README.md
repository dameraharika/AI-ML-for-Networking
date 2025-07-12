
# 🧠 AI/ML for Networking - Cyberattack Detection Web App

This project is a **Machine Learning-powered web application** that identifies whether a given network-related text input (such as a log message or activity description) is likely to indicate a cyberattack. It uses a trained **text classification model** built with **TF-IDF vectorization** and is deployed via a **Flask web server**.

---

## 📂 Project Structure

```
AI-ML-for-Networking-main/
│
├── app.py                      # Main Flask web application
├── attack_detection_model.pkl # Trained ML model (e.g., Logistic Regression, SVM, etc.)
├── tfidf_vectorizer.pkl       # Pre-fitted TF-IDF Vectorizer
├── templates/
│   └── index.html              # HTML template for the web interface
```

---

## ⚙️ Prerequisites

Make sure you have **Python 3.7+** installed.

### 🧪 Python Libraries Required

Install them using `pip`:

```bash
pip install flask joblib
```

---

## 🚀 Getting Started

### 1. Clone or Download the Repository

```bash
git clone https://github.com/yourusername/AI-ML-for-Networking-main.git
cd AI-ML-for-Networking-main
```

### 2. Run the Web Application

Simply execute the following command:

```bash
python app.py
```

You should see output like:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### 3. Open the App in Your Browser

Visit:

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

- When the user submits a text query:
  1. The app loads a **TF-IDF vectorizer** to transform the text into numeric form.
  2. This transformed data is passed to the **ML model** (`attack_detection_model.pkl`).
  3. The model predicts whether the input text suggests a **cyberattack or normal activity**.
  4. The result is displayed on the webpage.

---

## 💻 Code Overview

### `app.py`

```python
from flask import Flask, render_template, request
import joblib

# Load the pre-trained model and vectorizer
model = joblib.load("attack_detection_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        query = request.form["query"]
        vec = vectorizer.transform([query])
        result = model.predict(vec)[0]
        prediction = f"Prediction: {result}"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
```

### `templates/index.html`

A minimal HTML form that accepts input and shows prediction.

---

## 📈 Model Training (Not Included)

This project only includes the **inference part** of the system. The following files are assumed to be pre-trained:

- `attack_detection_model.pkl`: Machine learning classification model.
- `tfidf_vectorizer.pkl`: Vectorizer trained on network-related text data.

To train your own models, you'd typically use:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Sample code outline:
X = [...]  # List of text inputs
y = [...]  # Labels: 'Attack' or 'Normal'

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

# Save model and vectorizer
joblib.dump(model, 'attack_detection_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
```

---

## 📌 Use Cases

- Intrusion Detection Systems (IDS)
- Log Monitoring Tools
- Network Security Dashboards
- Educational ML Projects

---

## ✅ Example Inputs

| Input Message                            | Predicted Output   |
|------------------------------------------|--------------------|
| "Multiple failed login attempts"         | Attack             |
| "User successfully authenticated"        | Normal             |
| "Unusual outbound traffic detected"      | Attack             |
| "Ping request from internal machine"     | Normal             |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♀️ Maintainer

**Damera Harika**  
Feel free to connect or raise issues for any suggestions or improvements.
