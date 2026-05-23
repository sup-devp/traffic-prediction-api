from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('traffic_model.pkl')
scaler = joblib.load('scaler.pkl')

feature_cols = [
    "hour_of_day", "day_of_week", "is_weekend",
    "hour_sin", "hour_cos", "target_lag1", "target_lag2",
    "temperature_2m", "precipitation", "wind_speed_10m"
]

@app.route('/')
def home():
    return jsonify({
        "message": "Traffic Prediction API",
        "status": "running",
        "endpoint": "POST /predict"
    })

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract features in correct order
    features = [data.get(col, 0) for col in feature_cols]
    features_array = np.array(features).reshape(1, -1)

    # Scale and predict
    features_scaled = scaler.transform(features_array)
    prediction = model.predict(features_scaled)[0]

    return jsonify({
        "predicted_traffic_volume": round(float(prediction), 2),
        "input_features": data
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)