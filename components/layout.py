from dash import html
from components.charts import layout as bar_chart_layout, area_chart_layout
from components.time_series import layout as time_series_layout
from components.maps import map_layout
from components.heatmap import heatmap_layout
from components.growth_trends import growth_trend_layout

# Top-level dashboard layout
layout = html.Div([
    html.H1("Met Police Force Crimes 2024-2025", style={"textAlign": "center", "marginBottom": "20px"}),
    html.H2("Overview", style={"textAlign": "center"}),
    html.Div(growth_trend_layout, style={"padding": "20px"}),

    html.H2("Detailed Breakdown", style={"textAlign": "center", "marginTop": "40px"}),

    # Second Layer: Time series + bar chart
    html.Div([
        html.Div(time_series_layout, style={"width": "49%", "display": "inline-block", "verticalAlign": "top", "paddingRight": "1%"}),
        html.Div(bar_chart_layout, style={"width": "49%", "display": "inline-block", "verticalAlign": "top", "paddingLeft": "1%"})
    ], style={"padding": "20px"}),
    
    # Third Layer: Map chart + area chart
    html.Div([
        html.Div(map_layout, style={"width": "49%", "display": "inline-block", "verticalAlign": "top", "paddingRight": "1%"}),
        html.Div(area_chart_layout, style={"width": "49%", "display": "inline-block", "verticalAlign": "top", "paddingLeft": "1%"})
    ], style={"padding": "20px"}),

    # Trial section for heatmap
    html.H2("Trial", style={"textAlign": "center", "marginTop": "40px"}),
    html.Div(heatmap_layout, style={"padding": "20px"}),
    
    html.Hr(),
    html.Footer(
        "Crime data sourced from UK Police API",
        style={"textAlign": "center", "padding": "10px", "fontSize": "0.9em", "color": "#777"}
    )
])