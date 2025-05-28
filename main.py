
from openweather import get_weather_summary
from noaa_parser import search_noaa_storms
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

# --- Sample Inputs (will be dynamic later) ---
zip_code = "45231"
date_of_loss = "2024-04-20"
lat = 39.2334  # Example: Cincinnati, OH
lon = -84.5545

# --- Weather and Storm Lookups ---
owm_data = get_weather_summary(lat, lon, date_of_loss, api_key)
noaa_data = search_noaa_storms(zip_code, date_of_loss)

# --- Generate Claim Report ---
report = create_weather_report(zip_code, date_of_loss, owm_data, noaa_data)

# --- Output to Screen and File ---
print("\n--- Weather Claim Report ---")
print(report)

with open("claim_weather_report.txt", "w") as file:
    file.write(report)

print("\n📄 Report saved to: claim_weather_report.txt")
