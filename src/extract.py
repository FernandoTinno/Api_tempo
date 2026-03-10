import json
from pathlib import Path
import requests

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(exist_ok=True)

def fetch_weather_data():
    """Fetches hourly weather data from Open-Meteo API."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": -23.55,
        "longitude": -46.63,
        "hourly": "temperature_2m,relative_humidity_2m"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        file_path = DATA_DIR / "weather.json"
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
            
        print(f"Data successfully extracted and saved to {file_path}")

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")