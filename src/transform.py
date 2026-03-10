import json
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def load_and_transform_data():
    """Transforms raw JSON data into aggregated daily pandas DataFrames."""
    try:
        with open(DATA_DIR / "weather.json", encoding="utf-8") as file:
            data = json.load(file)

        if "hourly" not in data:
            raise ValueError("JSON does not contain 'hourly' data.")

        df = pd.DataFrame({
            "timestamp": data["hourly"]["time"],
            "temperature": data["hourly"]["temperature_2m"],
            "humidity": data["hourly"]["relative_humidity_2m"]
        })

        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["date"] = df["timestamp"].dt.date

        daily_summary = df.groupby("date").agg(
            avg_temperature=("temperature", "mean"),
            max_temperature=("temperature", "max"),
            min_temperature=("temperature", "min"),
            avg_humidity=("humidity", "mean")
        ).reset_index()

        print("\n=== Basic Weather Statistics ===")
        print(df.describe())
        
        return df, daily_summary

    except FileNotFoundError:
        print("Error: weather.json not found. Run extraction first.")
        return None, None
    except Exception as error:
        print(f"Transformation error: {error}")
        return None, None