from fastapi import FastAPI
from valiadations import Valiadations
from model import predict_price
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="car-price-prediction")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later you can restrict to your streamlit domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",response_model=str)
def home():
    return "welcome to car-price-prediction"

@app.post("/predict")
def prediction(features:Valiadations):

    pridected_price = predict_price(features.model_dump())

    return pridected_price