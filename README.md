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
   - Date 
   - Latitude/Longitude (optional for accuracy)

2. The system fetches:
   - 📍 Live or recent weather data from **OpenWeatherMap**
   - 📄 Storm events from **NOAA CSV logs** (e.g. hail, wind)

3. It outputs:
   - A structured summary of weather conditions.
   - A list of nearby storm events for the specified date.
   - 📄 To save this report, use 'Print to PDF' or copy and paste.

---

## 📁 File Structure

```
local-weather-event-report/
├── app.py                 # Main runner
├── openweather.py          # OWM API logic
├── noaa_parser.py          # NOAA CSV scanner
├── generate_report.py      # Formats final report
├── weather_report.txt
├── emails_collected.txt    # (optional extension)
└── sample_noaa_data.csv    # Downloaded from NOAA site
```

---

## 🔧 Setup Instructions

### 1. Get an OpenWeatherMap API Key
  Create a free account at:
  https://openweathermap.org/api

  ---

### 2. Set the API Key as an Environment Variable

  On macOS / Linux:
  ```bash
  export OPENWEATHER_API_KEY=your_api_key_here
  ```
  On Windows (PowerShell):
  ```bash
  setx OPENWEATHER_API_KEY "your_api_key_here"
  ```
  When deploying, set the OPENWEATHER_API_KEY in the platform’s environment variable settings.
  
  ---
  
### 3. Prepare NOAA Storm Event Data (Local Use)
  This project uses NOAA storm event CSV files for historical storm data.
   - Download data from:
     ```bash
     https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/
     ```
   - Filter by state, year, and unzip locally

     ---
     
### 4. Unzip & Rename your NOAA file to:
   ```bash
   sample_noaa_data.csv
   ```
   - Place the file in the root directory.
   - Note: NOAA data is not auto-fetched and must be provided manually.

   ---
   
### 5. Run the Application Locally:
   ```bash
   python app.py
   ```
   - Open your browser at:
     ```bash
     http://localhost:10000
     ```

---

## 📄 Sample Output

```
📍 Location: ZIP 45231
📆 Date: 2024-04-20

🔹 OpenWeather Data
Condition: Thunderstorm
Temp: 62.3°F
Wind Speed: 27.9 mph

🔹 NOAA Storm Reports
- Hail reported in Hamilton, OH on 4/19/2024, Magnitude: 1.25

🧠 Summary
✔️ Weather and storm activity recorded near the specified location and date.


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


