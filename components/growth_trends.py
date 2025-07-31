import pandas as pd
import plotly.graph_objects as go
from utils.data_processing import combined_df
from dash import html, dcc, Input, Output, callback

# Ensure Mnth is in datetime format
combined_df["Month"] = pd.to_datetime(combined_df["Month"])

# Filter for the desired date range
filtered_df = combined_df[
    (combined_df["Month"] >= "2024-05-01") & 
    (combined_df["Month"] <= "2025-04-30")
]

# Group by Month and Crime type and count crimes
monthly_crime_counts = (
    filtered_df.groupby([filtered_df["Month"].dt.to_period("M"), "Crime type"])
    .size()
    .unstack(fill_value=0)
    .sort_index()
)

# Convert PeriodIndex to datetime for plotting
monthly_crime_counts.index = monthly_crime_counts.index.to_timestamp()

# Calculate percentage change
crime_pct_change = monthly_crime_counts.pct_change().fillna(0) * 100

# Prepare layout for Dash
growth_trend_layout = html.Div([
    html.H3("Month-on-Month % Change in Crime Types"),
    dcc.Graph(
        id="crime-growth-line",
        figure=go.Figure().update_layout(template="plotly_white")
    )
])

# Callback to populate chart
@callback(
    Output("crime-growth-line", "figure"),
    Input("crime-growth-line", "id")  # Dummy input to trigger callback
)
def update_growth_chart(_):
    fig = go.Figure()

    # Add each crime type as a separate line
    for crime_type in crime_pct_change.columns:
        fig.add_trace(go.Scatter(
            x=crime_pct_change.index,
            y=crime_pct_change[crime_type],
            mode="lines+markers",
            name=crime_type,          
        ))

    fig.update_layout(
        title="Month-on-Month % Change in Crime count by Type",
        xaxis_title="Month",
        yaxis_title="% Change",
        height=500
    )
    return fig
