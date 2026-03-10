from extract import fetch_weather_data
from transform import load_and_transform_data
from load import load_to_postgresql
from plot import generate_plots

def run_pipeline():
    """Orchestrates the ETL pipeline."""
    fetch_weather_data()
    
    hourly_df, daily_summary_df = load_and_transform_data()
    
    if hourly_df is not None and daily_summary_df is not None:
        generate_plots(hourly_df)
        load_to_postgresql(daily_summary_df, "daily_weather_summary")

if __name__ == "__main__":
    run_pipeline()