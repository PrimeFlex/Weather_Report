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
        <h2>PrimeFlex Weather Report</h2>
        <form action="/weather-report" method="get">
            ZIP Code: <input name="zip" required><br>
            Date of Loss: <input name="date" type="date" required><br>
            Latitude: <input name="lat" required><br>
            Longitude: <input name="lon" required><br><br>
            <input type="submit" value="Generate Report">
        </form>
    '''

@app.route('/weather-report', methods=['GET'])
def weather_report():
    try:
        zip_code = request.args.get('zip')
        date_of_loss = request.args.get('date')
        lat = float(request.args.get('lat'))
        lon = float(request.args.get('lon'))
        api_key = os.getenv("OPENWEATHER_API_KEY")

        if not all([zip_code, date_of_loss, lat, lon, api_key]):
            return jsonify({"error": "Missing parameters or API key"}), 400

        weather = get_weather_summary(lat, lon, date_of_loss, api_key)
        storms = search_noaa_storms(zip_code, date_of_loss)

        return jsonify({
            "zip": zip_code,
            "date_of_loss": date_of_loss,
            "weather": weather,
            "storms": storms
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
