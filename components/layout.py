from dash import html
from components.charts import layout as bar_chart_layout
from components.time_series import layout as time_series_layout
from components.maps import layout as map_layout

# Top-level dashboard layout
layout = html.Div([
    html.H1("UK Police Force Crime Dashboard", style={"textAlign": "center"}),

    html.Div([
        html.H2("Crime Breakdown for Selected Month"),
        bar_chart_layout
    ], style={"marginBottom": "50px"}),

    html.Hr(),

    html.Div([
        html.H2("Monthly Trends by Crime Type"),
        time_series_layout
    ]),

    html.Hr(),

    html.Div([
        html.H2("Geospatial Crime Distribution"),
        map_layout
    ])
])