from datetime import datetime, timedelta
from flask import Flask, request, render_template
import requests
from cache import Cache
import logging

logging.basicConfig(filename='/var/log/record.log', level=logging.DEBUG)
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        location = request.form['location']
        if location:
            data = get_weather(location)
            return render_template('index.html', data=data, location=location)
        else:
            app.logger.info("can't find location in form")
    return render_template('index.html')


def get_weather(location):
    cache = Cache()
    cache_data = cache.load_cache()
    print("Cache data: ", cache_data)

    if location in cache_data:
        timestamp = datetime.fromisoformat(cache_data[location]["timestamp"])
        if datetime.now() - timestamp < timedelta(hours=2):
            return cache_data[location]["data"]
    
    response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/next6days?key=H9FPEN7ABD6HV6NPJSCRYWTJY&include=days,datetime&elements=rdatetime,datetime,humidity,tempmin,tempmax&unitGroup=metric&lang=en")
    if response.status_code == 200:
        json_data = response.json()
        days = json_data["days"]
        forecast = []
        for data in days:
            forecast.append({
                "date": data.get("datetime"),
                "max_temp": data.get("tempmax"),
                "min_temp": data.get("tempmin"),
                "humidity": data.get("humidity")
            })
        cache.save_to_cache(location, forecast)
        return forecast
    return {'error': 'not found'}


if __name__ == '__main__':
        app.run(host='127.0.0.1', port=5000, debug=True)

