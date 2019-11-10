# WeatherPy

An analysis of world weather data looking at the relationship between weather characteristics and latitude.

## Description

Using Python code organized in a Jupyter Notebook and the OpenWeatherMap API, live weather data is gathered from over 500 random cities across the world by longitude and latitude. CitiPy is used to select the cities. The OpenWeatherMap JSON is then formatted using Pandas and visualized using PyPlot to determine if there are observable relationships between latitude and temperature, humidity, wind speed and cloud cover.

## Packages Used 
```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
from datetime import date
import citipy
```

## Contributors
- Aydan Nankoosingh

## 
This project was part of a certificate in Data Analytics from the University of Toronto School of Continuing Studies.

#

## Links
[CitiPy](https://pypi.org/project/citipy/)

[OpenWeatherMap](https://openweathermap.org/current)
