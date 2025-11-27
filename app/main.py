from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

model = pickle.load(open("model/model.pkl", "rb"))

app = FastAPI()

class House(BaseModel):
    area: float
    bedrooms: int
    age: float

@app.get("/")
def home():
    return {"msg": "ML Model API Running..."}

@app.post("/predict")
def predict_house(data: House):
    features = np.array([[data.area, data.bedrooms, data.age]])
    prediction = model.predict(features)[0]
    return {"prediction": float(prediction)}

