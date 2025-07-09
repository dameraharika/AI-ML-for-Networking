from flask import Flask, render_template, request
import joblib

# Load model and vectorizer
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
