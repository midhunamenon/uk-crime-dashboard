import pandas as pd

# Function to get crime counts by month
# This function takes a DataFrame with a 'Month' column and returns a DataFrame with
# the count of crimes for each month.
# It converts the 'Month' column to datetime format if it is not already.
def get_crime_counts_by_month(df: pd.DataFrame) -> pd.DataFrame:
    df["Month"] = pd.to_datetime(df["Month"])
    return df.groupby("Month")["Crime ID"].count().reset_index()

# Return time series data split by crime type
def get_crime_trend_by_type(df: pd.DataFrame) -> pd.DataFrame:
    df["Month"] = pd.to_datetime(df["Month"])
    return df.groupby(["Month", "Crime type"])["Crime ID"].count().reset_index()

# Function to get crime counts by type for a specific month
def get_crime_counts_by_type(df: pd.DataFrame, month: str) -> pd.DataFrame:
    filtered = df[df["Month"] == month]
    crime_counts = filtered["Crime type"].value_counts().reset_index()
    crime_counts.columns = ["Crime Type", "Count"] #Explicitly set column names
    return crime_counts

# Function to get the most common crime types
def top_n_crime_types(df: pd.DataFrame, n: int = 5) -> list:
    return df["Crime type"].value_counts().head(n).index.tolist()

# Function to get geospatial data for a specific month
def get_geospatial_data(df: pd.DataFrame, month: str) -> pd.DataFrame:
    """Returns lat/lon and crume type for a selected month (NaNs removed)."""
    #filtered = df[df["Month"] == month].copy()
    return df[df["Month_Name"] == month].dropna(subset=["Latitude", "Longitude"])

