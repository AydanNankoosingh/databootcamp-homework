# Truck Appraisal App 

This Truck Appraisal App uses Machine Learning to estimate the value of a truck based on details inputted by the user. 

The user fills out the form on the home screen, then data is passed through a machine learning model using a Flask app to get a price estimate. The price is then displayed on the results page, along with a Leaflet map that shows 100 trucks from the same manufacturer that were being sold on Craigslist.

## Python Imports

```python
# data exploration and analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
# machine learning preprocessing and model training
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
# importing and exporting models
from joblib import dump, load

```

## Javascript CDN's

[Bootstrap](https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css) \
[Leaflet](https://unpkg.com/leaflet@1.6.0/dist/leaflet.js)

## Data
The [data](https://www.kaggle.com/austinreese/craigslist-carstrucks-data) was in CSV format, from Kaggle, scraped by Austin Reese. It was used to train the models, as well as to build the Leaflet plot.
