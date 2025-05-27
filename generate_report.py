# main.py
from openweather import get_weather_summary
from noaa_parser import search_noaa_storms
from generate_report import create_weather_report

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

# --- Output to Screen ---
print("\n--- PrimeFlex Weather Report ---")
print(report)
print("\n📄 To save this report, use 'Print to PDF' or copy and paste.")
