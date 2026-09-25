
from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
with open("heart_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        age = float(request.form["age"])
        sex = float(request.form["sex"])
        cp = float(request.form["cp"])
        trestbps = float(request.form["trestbps"])
        chol = float(request.form["chol"])
        fbs = float(request.form["fbs"])
        restecg = float(request.form["restecg"])
        thalach = float(request.form["thalach"])
        exang = float(request.form["exang"])
        oldpeak = float(request.form["oldpeak"])
        slope = float(request.form["slope"])
        ca = float(request.form["ca"])
        thal = float(request.form["thal"])

        data = np.array([[
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        ]])

        prediction = model.predict(data)[0]

        if prediction == 1:
            result = "Heart disease detected by the model"
        else:
            result = "Heart disease not detected by the model"

        return render_template(
            "index.html",
            prediction_text=result
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)