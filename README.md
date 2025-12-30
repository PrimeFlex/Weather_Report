# 🌩️ --- Local Weather Event Report ---

A lightweight backend service that aggregates public weather
and storm event data for a given location and date.

This project demonstrates backend system design, API integration,
environment variable management, and deployment practices.
---

## 📌 Use Case

> “What weather events were recorded near a given location on a specific date?”

This service aggregates publicly available data sources to provide
contextual weather and storm information, such as:

- Local weather conditions
- Reported storm events (hail, wind, etc.)
- Time and location alignment

The output is intended for **informational and technical demonstration purposes only**.
---

## 🧠 How It Works

1. User provides:
   - ZIP code
   - Date of storm
   - Latitude/Longitude (optional for accuracy)

2. The system fetches:
   - 📍 Live or recent weather data from **OpenWeatherMap**
   - 📄 Storm events from **NOAA CSV logs** (e.g. hail, wind)

3. It outputs:
   - A structured summary of weather conditions
   - A list of nearby storm events for the specified date**
   - 📄 To save this report, use 'Print to PDF' or copy and paste.")

---

## 📁 File Structure

```
local-weather-event-report/
├── main.py                 # Main runner
├── openweather.py          # OWM API logic
├── noaa_parser.py          # NOAA CSV scanner
├── generate_report.py      # Formats final report
├── weather_report.txt
├── emails_collected.txt    # (optional extension)
└── sample_noaa_data.csv    # Downloaded from NOAA site
```

---

## 🔧 Setup Instructions

1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Set your OpenWeatherMap API key as an environment variable:
   ```bash
   export OPENWEATHER_API_KEY=your_key_here
3. Download NOAA data for your state:
   - Visit [NOAA FTP: Storm Events](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/)
   - Filter by state, year, and unzip locally
4. Rename your NOAA file to `sample_noaa_data.csv`
5. Run the tool in Replit or locally:
   ```bash
   python main.py
   ```

---

## 📄 Sample Output

```
📍 Location: ZIP 45231
📆 Date of Damage: 2024-04-20

🔹 OpenWeather Data
Condition: Thunderstorm
Temp: 62.3°F
Wind Speed: 27.9 mph

🔹 NOAA Storm Reports
- Hail reported in Hamilton, OHIO on 4/19/2024, Magnitude: 1.25

🧠 Summary
✔️ Weather and storm activity recorded near the specified location and date..

print--- Weather Report ---
print(report)

print("\n📄 To save this report, use 'Print to PDF' or copy and paste.")

```

---

## 🔄 Future Enhancements

- 🔁 Auto-fetch NOAA data via FTP
- 🛰️ Hail size overlays via premium storm data APIs
- Improved data visualization

---

## ⚖️ Disclaimer

This project provides informational weather data only.
It does not provide insurance, legal, or professional advice.

---


