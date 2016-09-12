from os import path
from flask import render_template

from app import app
from app.forms import WeatherForm
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/current", methods=["GET", "POST"])
def current_weather():
    weather_form = WeatherForm()
    return render_template("current.html", weather_form=weather_form)

@app.route("/forecast")
def forecast_weather():
    return render_template("forecast.html")
