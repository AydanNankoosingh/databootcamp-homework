# Import dependencies
import os
from flask import Flask, jsonify, render_template, request
import pandas as pd
import numpy as np
import json
from joblib import dump, load

# Import models & set default model input
model = load('model.joblib')
neigh = load('neigh.joblib')

base_input = [2009, 2.6, 120000] + [0]*20 # needs []
manufacturers = ['manufacturer_bmw',
       'manufacturer_cadillac', 'manufacturer_chevrolet',
       'manufacturer_datsun', 'manufacturer_dodge', 'manufacturer_ford',
       'manufacturer_gmc', 'manufacturer_harley-davidson',
       'manufacturer_honda', 'manufacturer_jeep', 'manufacturer_lincoln',
       'manufacturer_mazda', 'manufacturer_mercedes-benz',
       'manufacturer_mitsubishi', 'manufacturer_nissan', 'manufacturer_ram',
       'manufacturer_subaru', 'manufacturer_toyota', 'manufacturer_volkswagen',
       'manufacturer_volvo']

# Bins for KNN
bins = [500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 
        20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000,
        70000, 75000, 80000]



# Convert condition to numeric value
def conv_condition(val):
    if val == 'new':
        return 5
    elif val == 'like new':
        return 4
    elif val == 'excellent':
        return 3
    elif val == 'good':
        return 2
    elif val == 'fair':
        return 1
    else:
        return 0

# Format input for model
def input_builder(y, c, o, m):
    X = base_input
    cond = conv_condition(c)
    ind = manufacturers.index('manufacturer_' + m)
    X[ind + 3] = 1
    X[0] = y
    X[1] = cond
    X[2] = o

    return X



# Flask set up
app = Flask(__name__)

# Index route w/ form
@app.route("/")
def index():
    return render_template('index.html')

# Results route
@app.route("/get_data", methods=['POST'])
def results():

    # Recieve input from form
    year = int(request.form['year'])
    manufacturer = request.form['manufacturer'].lower()
    mod = request.form['model'].lower()
    condition = request.form['condition'].lower()
    odometer = int(request.form['odometer'])
    tool = request.form['tool']

    # Price evaluation
    if tool == 'Regression':
        price = round(model.predict([input_builder(year, condition, odometer, manufacturer)])[0], 2)
    else:
        price = bins[neigh.predict([input_builder(year, condition, odometer, manufacturer)])[0]]



    return render_template('results.html',
        year=year,
        manufacturer=manufacturer.title(),
        model=mod.title(),
        condition=condition.title(),
        odometer=odometer,
        price=price)



if __name__=="__main__":
    app.run(debug=True)
