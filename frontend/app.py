import streamlit as st
import joblib
import pandas as pd

ml_model = joblib.load("../models/pkl_files/model.pkl")
scaler = joblib.load("../models/pkl_files/scaler.pkl")
columns = joblib.load("../models/pkl_files/colums.pkl")


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


if st.button("Predict price"):
    data_frame = pd.DataFrame(0,index=[0],columns=columns)    
    data_frame.loc[0] = 0

    data_frame.at[0,'year'] = year
    data_frame.at[0,'mileage'] = mileage
    data_frame.at[0,'tax'] = tax
    data_frame.at[0,'mpg'] = mpg

    data_frame.at[0,f"model_{model}"] = 1
    data_frame.at[0,f"fuelType_{fuelType}"] = 1
    data_frame.at[0,f"transmission_{transmission}"] = 1
    data_frame.at[0,f"engineSize_{engineSize}"] = 1


    data_frame = data_frame.reindex(columns=columns,fill_value=0)

    cols = ['year','tax','mpg','mileage']

    data_frame[cols] = scaler.transform(data_frame[cols])

    # print(data_frame.isna().sum())

    prediction = ml_model.predict(data_frame)[0]

    st.write(f"{prediction:,.2f}")