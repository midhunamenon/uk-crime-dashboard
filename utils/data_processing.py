import os
import pandas as pd

RAW_DATA_PATH = "data/raw"
OUTPUT_PATH = "data/processed/Combined_crime_data.csv"

def load_and_merge_csvs():
    # Step 1: List all CSV files in the raw data folder
    files = [f for f in os.listdir(RAW_DATA_PATH) if f.endswith(".csv")]
    all_data = []

    for file in files:
        path = os.path.join(RAW_DATA_PATH, file)
        df = pd.read_csv(path)
        all_data.append(df)

    # Combine all dataframes into one
    combined = pd.concat(all_data, ignore_index=True)
    
    # Clean and process the combined dataframe
    combined = combined.dropna(subset=["Longitude", "Latitude"])

    # Convert 'Month' to datetime and extract month name and day of the week
    combined["Month"] = pd.to_datetime(combined["Month"])
    combined["Month_Name"] = combined["Month"].dt.strftime("%B")
    combined["Day_of_Week"] = pd.to_datetime(combined["Month"]).dt.day_name()
    
    # Save the processed data to the output path
    combined.to_csv(OUTPUT_PATH, index=False)
    print(f"Combined data saved to {OUTPUT_PATH} - {len(combined)} rows")
    
    return combined
        
combined_df = load_and_merge_csvs()
        