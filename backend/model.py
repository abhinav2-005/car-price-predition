import joblib
import pandas as pd


ml_model = joblib.load("../models/pkl_files/model.pkl")
scaler = joblib.load("../models/pkl_files/scaler.pkl")
columns = joblib.load("../models/pkl_files/colums.pkl")


def load_models(test_data : dict) -> pd.DataFrame:
    data_frame = pd.DataFrame([test_data])
    print(data_frame.head(1))
    catagorial_vals = ["model","transmission","fuelType","engineSize"]
    scaler_vals = ['year','tax','mpg','mileage']

    df_encoded = pd.get_dummies(data_frame, columns=catagorial_vals, drop_first=True)

    df_encoded[scaler_vals] = scaler.transform(df_encoded[scaler_vals])
    df_encoded = df_encoded.reindex(columns=columns,fill_value=0)

    return df_encoded

def predict_price(info : dict) -> float:
    x = load_models(info)
    predicted_price = ml_model.predict(x)[0]

    return float(predicted_price)
