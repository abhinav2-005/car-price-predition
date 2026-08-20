from fastapi import FastAPI
from valiadations import Valiadations
from model import predict_price

app = FastAPI(title="car-price-prediction")

@app.get("/",response_model=str)
def home():
    return "welcome to car-price-prediction"

@app.post("/predict")
def prediction(features:Valiadations):

    pridected_price = predict_price(features.model_dump())

    return pridected_price