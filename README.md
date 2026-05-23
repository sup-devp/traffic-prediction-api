# 🚦 Traffic Volume Prediction API

A machine learning REST API built with Flask and scikit-learn that predicts road traffic volume based on time, day, and weather conditions. Trained on 2 years of real UK motorway data from the National Highways WebTRIS API.

---

## 🚀 Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core language |
| Flask | REST API framework |
| scikit-learn | Machine learning (Random Forest) |
| pandas & NumPy | Data processing |
| joblib | Model serialisation |
| Open-Meteo API | Historical weather data |
| WebTRIS API | Real UK traffic data |

---

## 📋 Features

- ✅ Predicts traffic volume given time and weather conditions
- ✅ Trained on 2 years of real UK motorway data (2022–2023)
- ✅ Random Forest model achieving R² score of 0.97
- ✅ REST API endpoint accepting JSON input
- ✅ Returns predicted vehicle count per interval

---

## 🧠 Model Details

The Random Forest model was selected after benchmarking 5 models:

| Model | R² Score |
|---|---|
| Linear Regression | ~0.86 |
| Support Vector Regression | ~0.88 |
| Neural Network (MLP) | ~0.91 |
| Gradient Boosting | ~0.95 |
| **Random Forest** | **~0.97** |

### Features Used
- Hour of day (with cyclic sin/cos encoding)
- Day of week
- Is weekend flag
- Lag features (previous traffic volumes)
- Temperature (°C)
- Precipitation (mm)
- Wind speed (km/h)

---

## 🔧 How to Run

### Prerequisites
- Python 3.9+
- pip

### Steps

1. Clone the repository
```bash
git clone https://github.com/sup-devp/traffic-prediction-api.git
cd traffic-prediction-api
```

2. Install dependencies
```bash
pip install flask scikit-learn pandas numpy joblib
```

3. Add your trained model files to the project folder:
```
traffic_model.pkl
scaler.pkl
```

4. Run the API
```bash
python3 app.py
```

5. Server starts at:
```
http://127.0.0.1:5000
```

---

## 📡 API Endpoints

### Check API Status
```
GET /
```
Response:
```json
{
    "message": "Traffic Prediction API",
    "status": "running",
    "endpoint": "POST /predict"
}
```

---

### Predict Traffic Volume
```
POST /predict
```
Request Body:
```json
{
    "hour_of_day": 8,
    "day_of_week": 1,
    "is_weekend": 0,
    "hour_sin": 1.0,
    "hour_cos": 0.0,
    "target_lag1": 1200,
    "target_lag2": 1100,
    "temperature_2m": 15.0,
    "precipitation": 0.0,
    "wind_speed_10m": 10.0
}
```
Response:
```json
{
    "predicted_traffic_volume": 286.89,
    "input_features": { ... }
}
```

---

## 💡 How It Works

1. Client sends a POST request with time and weather conditions
2. Flask receives the request and extracts the features
3. Features are scaled using the same StandardScaler used during training
4. The Random Forest model predicts traffic volume
5. Prediction is returned as JSON

---

## 🔗 Relevance to Industry

This project demonstrates end-to-end ML deployment — a critical skill for ML Engineer and Data Scientist roles. Key skills demonstrated:
- Training and evaluating multiple ML models
- Feature engineering (cyclic encoding, lag features)
- Model serialisation and loading
- Deploying ML models as REST APIs
- Working with real-world public APIs

---

## 👩‍💻 Author

**Supraja** — Previously Software Developer at Barclays (2023–2025)
