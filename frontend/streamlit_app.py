import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv("API_URL")

st.title("Ford car prediction")

model = st.selectbox(label = "Model",options =["Fiesta",
 "Focus",        
 "Kuga",                     
 "EcoSport",                 
 "C-MAX",                   
 "Ka+",                  
 "Mondeo",                  
 "B-MAX",
 "S-MAX ",                
 "Grand C-MAX",             
 "Galaxy",              
 "Edge",             
 "KA",            
 "Puma",         
 "Tourneo Custom",     
 "Grand Tourneo Connect",    
 "Mustang",    
 "Tourneo Connect",   
 "Fusion",   
 "Streetka",    
 "Ranger",   
 "Escort",  
 "Transit Tourneo",            
"Focus"])

year = st.number_input(label="Manufatured Year",min_value = 0,max_value=10000)

transmission = st.selectbox(label = "Transmission",options = ["Manual","Automatic","Semi-Auto"])

mileage = st.number_input(label="Mileage",min_value=0,max_value=1000000)

fuelType = st.selectbox(label = "FuelType",options=["Petrol","Diesel","Hybrid","Electric","Other"])

tax = st.number_input(label = "Tax",min_value=0,max_value=100000)

mpg = st.number_input(label = "mpg",min_value=0.0,max_value=100000.0,step=0.1)

engineSize = st.selectbox(label = "EngineSize",options=[1.0,
1.5 ,
2.0,
1.2,
1.6,
1.1,
1.4,
2.3,
0.0,
5.0,
1.8,
2.2,
2.5,
1.3,
3.2,
1.7])

input_data = {
    "year" : int(year),
    "transmission" : str(transmission),
    "mileage" : str(mileage),
    "tax" : int(tax),
    "mpg" : float(mpg),
    "engineSize" : float(engineSize),
    "model" : str(model),
    "transmission" : str(transmission),
    "fuelType" : str(fuelType)
}

if st.button("Predict price"):
    try:
        res = requests.post(url=api_url,json=input_data,timeout=20)

        if res.status_code == 200:
            predtion = res.json()
            if predtion:
               st.success(f"Predicted Price: {predtion:,.2f}")
            else:
                st.error("API connected, key error")

    except Exception as e:
        st.error("Api connection failed")
        st.code(str(e))

