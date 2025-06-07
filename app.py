from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load("model/churn_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        age = float(request.form["age"])
        tenure = float(request.form["tenure"])
        bill = float(request.form["bill"])
        usage = float(request.form["usage"])

        features = np.array([[age, tenure, bill, usage]])
        prediction = model.predict(features)[0]
        return render_template("index.html", prediction=prediction)
    except:
        return "Invalid Input"

if __name__ == "__main__":
    app.run(debug=True)
