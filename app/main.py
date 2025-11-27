from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pickle
import numpy as np
import os

# Load model
model = pickle.load(open("model/model.pkl", "rb"))

app = FastAPI()

# Templates
templates = Jinja2Templates(directory="app/templates")

# API endpoints
class House(BaseModel):
    area: float
    bedrooms: int
    age: float

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict_form", response_class=HTMLResponse)
def predict_form(request: Request,
                 area: float = Form(...),
                 bedrooms: int = Form(...),
                 age: float = Form(...)):
    features = np.array([[area, bedrooms, age]])
    prediction = model.predict(features)[0]
    return templates.TemplateResponse("index.html", {"request": request, "prediction": round(float(prediction), 2)})

@app.post("/predict")
def predict_house(data: House):
    features = np.array([[data.area, data.bedrooms, data.age]])
    prediction = model.predict(features)[0]
    return {"prediction": float(prediction)}

