import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def generate_plots(df):
    """Generates and saves analytical plots based on weather data."""
    print("\n=== Generating analytical plots... ===")

    plt.figure(figsize=(12, 6))
    plt.plot(df["timestamp"], df["temperature"], label="Temperature (°C)", color="red")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Variation Over Time")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(DATA_DIR / "temperature_plot.png")
    plt.close()

    plt.figure(figsize=(12, 6))
    plt.plot(df["timestamp"], df["humidity"], label="Humidity (%)", color="blue")
    plt.xlabel("Time")
    plt.ylabel("Relative Humidity (%)")
    plt.title("Humidity Variation Over Time")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(DATA_DIR / "humidity_plot.png")
    plt.close()

    plt.figure(figsize=(8, 6))
    plt.scatter(df["temperature"], df["humidity"], alpha=0.6, color="green")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Humidity (%)")
    plt.title("Temperature vs Humidity Relationship")
    plt.tight_layout()
    plt.savefig(DATA_DIR / "temp_humidity_scatter.png")
    plt.close()