from os import path
from flask import render_template, request, flash

from app import app
from app.forms import WeatherForm
from app.open_weather_api import OpenWeatherAPI

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/current", methods=["GET", "POST"])
def current_weather():
    weather_form = WeatherForm(request.form)
    weather_item = None
    city = ""
    country_code = ""

    if request.method == "POST" and weather_form.validate():
        # do stuff if form is valid
        city = weather_form.city.data
        country_code = weather_form.country_code.data

        try:
            api = OpenWeatherAPI(app.config["OPEN_WEATHER_API_KEY"])
            weather_item = api.get_current_weather(city, country_code)
        except ValueError:
            flash("City Not Found")

    return render_template("current.html",
        weather_form=weather_form,
        weather_item=weather_item,
        city=city,
        country_code=country_code)

@app.route("/forecast", methods=["GET", "POST"])
def forecast_weather():
    weather_form = WeatherForm(request.form)
    weather_list = None
    city = ""
    country_code = ""

    if request.method == "POST" and weather_form.validate():
        # do stuff if form is valid
        city = weather_form.city.data
        country_code = weather_form.country_code.data

        try:
            api = OpenWeatherAPI(app.config["OPEN_WEATHER_API_KEY"])
            weather_list = api.get_daily_weather(city, country_code)
        except ValueError:
            weather_list = None
            flash("City Not Found")

    return render_template("forecast.html",
        weather_form=weather_form,
        weather_list=weather_list,
        city=city,
        country_code=country_code)