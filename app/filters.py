from datetime import datetime

from app import app

@app.template_filter('timestamp_to_date')
def timestamp_to_date(timestamp, just_time=False):
    date = datetime.fromtimestamp(int(timestamp))

    if just_time:
        return date.strftime("%I:%M:%S %p")
    else:
        return date.strftime("%m/%d/%Y") 