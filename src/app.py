from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "API is running 🚀"

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    steps = data.get("steps", 5)

    holiday = data.get("Holiday", [0]*steps)
    discount = data.get("Discount", [0]*steps)

    forecast = model.get_forecast(steps=steps)
    pred = np.exp(forecast.predicted_mean)

    return jsonify({
        "forecast": pred.tolist()
    })

if __name__ == "__main__":
    app.run(debug=True)