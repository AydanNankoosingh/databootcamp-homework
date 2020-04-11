# Import dependencies
import os
from flask import Flask, jsonify, render_template, request
import pandas as pd
import numpy as np
import json
from joblib import dump, load

# Import models & set default model input
model = load('model2.joblib')
neigh = load('neigh2.joblib')

base_input = [2009, 2.6, 120000, 6] + [0]*23
manufacturers = ['manufacturer_bmw',
       'manufacturer_cadillac', 'manufacturer_chevrolet',
       'manufacturer_datsun', 'manufacturer_dodge', 'manufacturer_ford',
       'manufacturer_gmc', 'manufacturer_harley-davidson',
       'manufacturer_honda', 'manufacturer_jeep', 'manufacturer_lincoln',
       'manufacturer_mazda', 'manufacturer_mercedes-benz',
       'manufacturer_mitsubishi', 'manufacturer_nissan', 'manufacturer_ram',
       'manufacturer_subaru', 'manufacturer_toyota', 'manufacturer_volkswagen',
       'manufacturer_volvo']
drives = ['drive_4wd', 'drive_fwd', 'drive_rwd']

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
def input_builder(y, co, cy, o, d, m):
    X = base_input
    cond = conv_condition(co)
    X[0] = y
    X[1] = cond
    X[2] = o
    X[3] = cy
    if f'drive_{d}' in drives:
        ind1 = drives.index('drive_' + d)
        X[ind1 + 4]
    if f'manufacturer_{m}' in manufacturers:
        ind2 = manufacturers.index('manufacturer_' + m)
        X[ind2 + 7] = 1

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
    year = int(request.form['year'].strip())
    manufacturer = request.form['manufacturer'].lower().strip()
    mod = request.form['model'].lower()
    condition = request.form['condition'].lower().strip()
    cylinders = int(request.form['cylinders'].lower().strip())
    odometer = int(request.form['odometer'].strip())
    drive = request.form['drive'].lower().strip()
    tool = request.form['tool']

    # Price evaluation
    if tool == 'Regression':
        price = round(model.predict([input_builder(year, condition, cylinders, odometer, drive, manufacturer)])[0], 2)
    else:
        ind = neigh.predict([input_builder(year, condition, cylinders, odometer, drive, manufacturer)])[0]
        if ind > 0:
            price = f'{bins[ind - 1]} - {bins[ind]}'
        else:
            price = bins[ind]



    return render_template('results.html',
        year=year,
        manufacturer=manufacturer.title(),
        model=mod.title(),
        cylinders=cylinders,
        condition=condition.title(),
        odometer=odometer,
        drive=drive.upper(),
        price=price)



if __name__=="__main__":
    app.run(debug=True)
