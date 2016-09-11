from os import path
from flask import render_template

from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/current")
def current_weather():
    return render_template("current.html")

@app.route("/forecast")
def forecast_weather():
    return render_template("forecast.html")
