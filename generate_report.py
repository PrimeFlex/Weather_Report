# generate_report.py
def create_weather_report(zip_code, date_of_loss, owm_data, noaa_events):
    lines = []
    lines.append(f"📍 Location: ZIP {zip_code}")
    lines.append(f"📆 Date of Damage: {date_of_loss}")
    lines.append("")

    lines.append("🔹 OpenWeather Data")
    lines.append(f"Condition: {owm_data['condition']}")
    lines.append(f"Temp: {owm_data['temp']}°F")
    lines.append(f"Wind Speed: {owm_data['wind_speed']} mph")

    lines.append("\n🔹 NOAA Storm Reports")
    if noaa_events:
        for event in noaa_events:
            lines.append(f"- {event['EVENT_TYPE']} reported in {event['CZ_NAME']}, {event['STATE']} on {event['BEGIN_DATE_TIME']}, Magnitude: {event['MAGNITUDE']}")
    else:
        lines.append("No matching storm events found in NOAA report.")

    lines.append("\n🧠 Claim Justification Summary")
    if noaa_events:
        lines.append("✔️ Storm activity aligns with the reported date and location. Claim likely valid.")
    else:
        lines.append("⚠️ No official storm data found. Additional documentation may be required.")

    return "\n".join(lines)
