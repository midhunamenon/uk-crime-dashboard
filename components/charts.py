from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash
from utils.crime_analysis import get_crime_counts_by_type

#Load the processed dataset
df = pd.read_csv("data/processed/Combined_crime_data.csv")
month_options = df["Month"].sort_values().unique()

# Layout with dropdown and bar chart
layout = html.Div([
    html.Label("Select Month:"),
    dcc.Dropdown(
        id="month-dropdown",
        options=[{"label": m, "value": m} for m in month_options],
        value=month_options[0],
        clearable=False
    ),
    dcc.Graph(id="bar-chart")
])

# Callback to update the bar chart based on selected month
@dash.callback(
    Output("bar-chart", "figure"),
    Input("month-dropdown", "value")
   )
def update_bar_chart(selected_month):
    crime_counts = get_crime_counts_by_type(df, selected_month)
    fig = px.bar(crime_counts, x="Crime Type", y="Count",
                 title=f"Crimes by Type in {selected_month}")
    fig.update_layout(xaxis_title="Crime Type", yaxis_title="Count")
    return fig