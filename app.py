# -*- coding: utf-8 -*-

import numpy as np 
import pickle
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    fet = [float(x) for x in request.form.values()]
    fet_f = np.array([fet])
    output = model.predict(fet_f)
    output = round(output[0], 2)
    return render_template('index.html', prediction_text = f'Distance covered = {output}km.')

if (__name__ == '__main__') :
    app.run(debug = True)