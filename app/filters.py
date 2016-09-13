from datetime import datetime

from app import app

@app.template_filter('timestamp_to_date')
def timestamp_to_date(timestamp, just_time=False):
    date = datetime.fromtimestamp(int(timestamp))

    if just_time:
        return date.strftime("%I:%M:%S %p")
    else:
        return date.strftime("%m/%d/%Y")

@app.template_filter('f_or_c')
def f_or_c(units):
    if units == "imperial":
        return "F"
    else:
        return "C"