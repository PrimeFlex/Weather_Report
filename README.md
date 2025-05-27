# 🌩️ PrimeFlex Weather Verifier

A smart backend module that helps validate insurance claims by cross-referencing **real-time weather data** (via OpenWeatherMap) with **official NOAA storm reports**. Designed for use by adjusters, policyholders, or carriers to justify or contest storm-related property claims.

---

## 📌 Use Case

> “Was there a storm on the date this homeowner is filing a claim?”

This tool helps confirm or dispute that question using trusted public sources — making it ideal for:
- ✅ Pre-claim evaluations
- ✅ Supplement justifications
- ✅ Dispute resolution
- ✅ Field adjuster tools

---

## 🧠 How It Works

1. User provides:
   - ZIP code
   - Date of loss
   - Latitude/Longitude (optional for accuracy)

2. The system fetches:
   - 📍 Live or recent weather data from **OpenWeatherMap**
   - 📄 Storm events from **NOAA CSV logs** (e.g. hail, wind)

3. It outputs:
   - A human-readable **summary report**
   - Claim validity **recommendation**
   - Saved `.txt` file for use in documentation

---

## 📁 File Structure

```
primeflex-weather-verifier/
├── main.py                 # Main runner
├── openweather.py          # OWM API logic
├── noaa_parser.py          # NOAA CSV scanner
├── generate_report.py      # Formats final report
├── claim_weather_report.txt
├── emails_collected.txt    # (optional extension)
└── sample_noaa_data.csv    # Downloaded from NOAA site
```

---

## 🔧 Setup Instructions

1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Replace `YOUR_OPENWEATHER_API_KEY` in `main.py`
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

🧠 Claim Justification Summary
✔️ Storm activity aligns with the reported date and location. Claim likely valid.

📄 Report saved to: claim_weather_report.txt
```

---

## 🔄 Future Enhancements

- 🔁 Auto-fetch NOAA data via FTP
- 🧠 AI-generated justification summary
- 🛰️ Hail size overlays via premium storm data APIs
- 🔗 Bubble.io or Google Sites integration

---

## ⚖️ Disclaimer

This tool is intended for educational and operational guidance only. Always verify final claim decisions with your carrier, public adjuster, or legal team.

---

## 👷 Created by PrimeFlex Adjusters  
[www.primeflexclaims.com](https://www.primeflexclaims.com)  
Custom-built by adjusters for adjusters.
