from dash import html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

from utils.crime_analysis import get_geospatial_data
from utils.data_processing import combined_df # preloaded df

# Get dropdown values
months = sorted(combined_df["Month_Name"].unique())
#crime_types = sorted(combined_df["Crime type"].unique()) # Add individual crime types dropdown
#crime_types.insert(0, "All Crimes")  # Add 'All Crimes' option

# Map layout with dropdown and map
map_layout = html.Div([
    html.H2("Crime Distribution Map"),

    dcc.Dropdown(
        id="map-month-dropdown",
        options=[{"label": m, "value": m} for m in months],
        value=months[0],  # Default to the first month
        clearable=False
    ),

 #   dcc.Dropdown(
 #       id="map-crime-dropdown",
 #       options=[{"label": c, "value": c} for c in crime_types],
 #       value="All Crimes",  # Default to the first crime type
 #       clearable=False
 #   ),

    dcc.Graph(
        id="crime-map",
        style={"height": "850px"}  # Set a fixed height for the map
    )
])

# Callback to update the map based on selected month and crime type
@callback(
    Output("crime-map", "figure"),
    Input("map-month-dropdown", "value"),
    #Input("map-crime-dropdown", "value")
)
def update_map(selected_month):
    #filter the data based on user input
    data = get_geospatial_data(combined_df, selected_month)

    # Filter only if a specific crime type is selected
    #if selected_crime != "All Crimes":
    #   data = data[data["Crime type"] == selected_crime]

    if data.empty:
        fig = px.scatter_mapbox(
            lat=[],
            lon=[],
            center={"lat": 52.5, "lon": -1},
            zoom=5,
            title="No Crime Data Available",
            height=850
        )
    else:
        fig = px.scatter_mapbox(
            data,
            lat="Latitude",
            lon="Longitude",
            color="Crime type", # Color by Crime type
            hover_name="Crime type",
            zoom=6,
            center={
                "lat": data["Latitude"].mean(), 
                "lon": data["Longitude"].mean()
            },
            height=700,
            title=f"Crime Distribution - {selected_month}"         
        )

    fig.update_layout(
        mapbox_style="open-street-map",
        margin=dict(l=0, r=0, t=40, b=0),
        legend_title="Crime Type"
    )
    return fig