# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 00:45:02 2020

@author: Pranav
"""


import numpy as np 
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import pickle

df = pd.read_excel('Book1.xlsx')
model1 = GradientBoostingRegressor(alpha = 0.75,ccp_alpha = 0.3, learning_rate = 0.4)
Y = df.Distance
df.drop(columns = ['Distance'], inplace = True)
model1.fit(df,Y)

pickle.dump(model1, open('model.pkl', 'wb'))

pickle.load(open('model.pkl','rb'))
print(model1.predict([[100,100,10]]))