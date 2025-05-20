from flask import Flask, render_template, request
import pickle

# Load the model and vectorizer
with open("stress_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        user_input = request.form["comment"]
        vect_input = vectorizer.transform([user_input])
        pred = model.predict(vect_input)[0]
        result = "🚨 Stress Detected" if pred == 1 else "✅ No Stress"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
