from dash import dcc, html, Input, Output
import pandas as pd
import plotly.graph_objects as go
import dash
from utils.crime_analysis import get_crime_trend_by_type

#Load and prepare the dataset
df = pd.read_csv("data/processed/Combined_crime_data.csv")
crime_time_series = get_crime_trend_by_type(df)
crime_types = crime_time_series["Crime type"].unique()

#Function to build the interactive line chart
def create_chart(selected):
    fig = go.Figure()

    # Add each crime type as a sepearate line
    # Highlight the selected crime type
    # by making it more prominent
    # and grey out the others
    for crime in crime_types:
        data = crime_time_series[crime_time_series["Crime type"] == crime]
        fig.add_trace(go.Scatter(
            x=data["Month"],
            y=data["Crime ID"],
            mode="lines+markers",
            name=crime,
            line=dict(width=2.5 if crime == selected else 1),
            opacity=1.0 if crime == selected else 0.2 #grey out others
        ))

    fig.update_layout(
        title="Crime Trends Over Time",
        xaxis_title="Month",
        yaxis_title="Crime Count"
    )
    return fig

# Layout with a crime type selector
layout = html.Div([
    html.Label("Highlight Crime Type:"),
    dcc.Dropdown(
        id="crime-type-toggle",
        options=[{"label": ct, "value": ct} for ct in crime_types],
        value=crime_types[0],  # Default to the first crime type which loads the chart
        clearable=False,
        style={"width": "50%"}
    ),
    dcc.Graph(id="line-chart")
])

# Callback for updating the line chart when toggle changes
@dash.callback(
    Output("line-chart", "figure"),
    Input("crime-type-toggle", "value")
)
def update_line_chart(selected):
    return create_chart(selected)
        