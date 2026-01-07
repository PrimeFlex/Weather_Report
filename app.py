# app.py
from flask import Flask, request, jsonify
from openweather import get_weather_summary
from noaa_parser import search_noaa_storms
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>Local Weather Report</title>
      <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
    <div class="container">
      <h2>Local Weather Event Report</h2>
      
      <form action="/weather-report" method="get">
        <label>
          ZIP Code
          <input name="zip" required>
        </label>

        <label>
          Date of Storm
          <input name="date" type="date" required>
        </label>

        <label>
          Latitude
          <input name="lat" required>
        </label>

        <label>
          Longitude
          <input name="lon" required>
        </label>

        <button type="submit">Generate Report</button>
      </form>

    </div>
    </body>
    </html>
    '''

@app.route('/weather-report', methods=['GET'])
def weather_report():
    try:
        zip_code = request.args.get('zip')
        date_of_storm = request.args.get('date')
        lat = float(request.args.get('lat'))
        lon = float(request.args.get('lon'))
        api_key = os.getenv("OPENWEATHER_API_KEY")

        if not api_key:
            return jsonify({"error": "OPENWEATHER_API_KEY not set"}), 500

        if not all([zip_code, date_of_storm, lat, lon, api_key]):
            return jsonify({"error": "Missing required request parameters"}), 400

        weather = get_weather_summary(lat, lon, date_of_storm, api_key)
        storms = search_noaa_storms(zip_code, date_of_storm)

        return jsonify({
            "zip": zip_code,
            "date_of_storm": date_of_storm,
            "weather": weather,
            "storms": storms
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
