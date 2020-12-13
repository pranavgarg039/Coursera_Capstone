# -*- coding: utf-8 -*-

import numpy as np 
import pickle
import pandas as pd
import streamlit as st
from sklearn.ensemble import GradientBoostingRegressor


st.write("""
         #Distance Predictor
""")

def inp_features():
    Heartbeat = st.sidebar.slider('heartbeat', 50,190,100)
    Cadence = st.sidebar.slider('Cadence', 100,250, 130)
    Speed = st.sidebar.slider('Speed', 2,36,10)
    
    inp = [Heartbeat, Cadence, Speed]
    return inp

df = inp_features()
st.write(df)
model = pickle.load(open('model.pkl', 'rb'))
ans = model.predict([df])
st.write(ans)

        
    

