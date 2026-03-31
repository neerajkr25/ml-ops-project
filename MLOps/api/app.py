from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(features: list):
    prediction = model.predict([features])
    return {"prediction": prediction[0]}
