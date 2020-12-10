# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 03:26:36 2020

@author: Pranav
"""

  
import requests

url = 'http://localhost:5000/distanceprediction'
r = requests.post(url,json={'Heartbeat': 100, 'Cadence': 100, 'Speed':10})

print(r.json())
