from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
from utils.data_processing import combined_df

#Load and prepare the dataset
#df = pd.read_csv("data/processed/Combined_crime_data.csv")
#crime_time_series = get_crime_trend_by_type(df)

crime_types = sorted(combined_df["Crime type"].dropna().unique())
crime_type_options = ["All Crimes"] + list(crime_types)

#Dash layout for the time series chart
time_series_layout = html.Div([
    html.H3("Crime Trends Over Time (Area Chart)"),
    dcc.Dropdown(
        id="time-series-crime-type-dropdown",
        options=[{"label": ct, "value": ct} for ct in crime_type_options],
        value="All Crimes",  # Default to 'All Crimes'
        clearable=False,
    ),
    dcc.Graph(id="time-series-chart")    
])

# Dash callback to update area chart
@callback(
        Output("time-series-chart", "figure"),
        Input("time-series-crime-type-dropdown", "value")
)
def update_time_series_chart(selected_crime):
    if selected_crime == "All Crimes":
        # Aggregate total crimes by month
        monthly_data = (
            combined_df.groupby("Month")
            .size()
            .reset_index(name="Count")
        )
        monthly_data["Crime type"] = "All Crimes"
    else:
        # Filter and aggregate by crime type and month
        monthly_data = (
            combined_df[combined_df["Crime type"] == selected_crime]
            .groupby("Month")
            .size()
            .reset_index(name="Count")
        )
        monthly_data["Crime type"] = selected_crime
            
    fig = px.area(
        monthly_data,
        x="Month",
        y="Count",
        color="Crime type",
        title=f"Crime Trends Over Time - {selected_crime}"
    )
    fig.update_layout(xaxis_title="Month", yaxis_title="Crime Count")
    fig.update_layout(showlegend=False)
    return fig

