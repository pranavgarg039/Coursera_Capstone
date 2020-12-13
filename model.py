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
