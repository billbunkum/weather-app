import requests

class OpenWeatherAPI():
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.base_payload = {
            "appid": self.api_key,
            "units": "imperial",
        }

    def get_payload(self, **kwargs):
        payload = {}
        for key, value in self.base_payload.items():
            payload[key] = value

        for key, value in kwargs.items():
            payload[key] = value

        return payload

    def get_current_weather(self, city, country_code=""):
        q = ""
        if country_code:
            q = "{},{}".format(city, country_code)
        else:
            q = city

        payload = self.get_payload(q=q)
        url = "{}{}".format(self.base_url, "/weather")
        r = requests.get(url, params=payload)
        return weather_items_or_error(r.json())

    def get_daily_weather(self, city, country_code="", num_days=16):
        q = ""
        if country_code:
            q = "{},{}".format(city, country_code)
        else:
            q = city

        payload = self.get_payload(q=q, cnt=num_days)
        url = "{}{}".format(self.base_url, "/forecast/daily")
        r = requests.get(url, params=payload)

        return weather_items_or_error(r.json())

def weather_items_or_error(weather_items):
    if str(weather_items.get("cod")) != "200":
        raise ValueError("Not a valid city")

    return weather_items