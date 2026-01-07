# noaa_parser.py
import csv
from datetime import datetime

def search_noaa_storms(zip_code, date_str):
    try:
        with open("sample_noaa_data.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            matched_events = []
            target_date = datetime.strptime(date_str, "%Y-%m-%d")

            for row in reader:
                event_date = datetime.strptime(row["BEGIN_DATE_TIME"].split()[0], "%m/%d/%Y")
                if row["CZ_NAME"] and row["EVENT_TYPE"] in ["Hail", "Thunderstorm Wind"]:
                    if abs((event_date - target_date).days) <= 2 and row["STATE"] == "OHIO":
                        matched_events.append(row)

            return matched_events
    except Exception as e:
        print("Error reading NOAA data:", e)
        return []
