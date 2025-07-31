from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
import dash
from utils.crime_analysis import get_crime_counts_by_type

#Load the processed dataset
df = pd.read_csv("data/processed/Combined_crime_data.csv")
df["Month"] = pd.to_datetime(df["Month"]) # Ensure month is in datetime format
month_options = df["Month"].dt.strftime("%B %Y").sort_values().unique()

#-------Bar Chart section-------
# Layout with dropdown and bar chart
bar_chart_layout = html.Div([
    html.Label("Select Month:"),
    dcc.Dropdown(
        id="month-dropdown",
        options=[{"label": m, "value": m} for m in month_options],
        value=month_options[0],
        clearable=False
    ),
    dcc.Graph(id="bar-chart"),

    #html.Hr(),

    #html.H3("Cumulative Crime Trends by Type"),
    #dcc.Graph(id="area-chart")
])

# Callback to update the bar chart based on selected month
@callback(
    Output("bar-chart", "figure"),
    Input("month-dropdown", "value")
)
def update_bar_chart(selected_month):
    selected_month_dt = pd.to_datetime(selected_month)
    filtered = df[df["Month"] == selected_month_dt]
    crime_counts = filtered.groupby("Crime type").size().reset_index(name="Count")
    crime_counts = crime_counts.sort_values(by="Count", ascending=False)
    
    fig = px.bar(
        crime_counts,
        x="Crime type",
        y="Count",
        title=f"Crimes by Type in {selected_month}"
    )
    fig.update_layout(xaxis_title="Crime Type", yaxis_title="Count")
    return fig

#-------Area Chart section-------
# Layout for the area chart
area_chart_layout = html.Div([
    html.H3("Cumulative Crime Trends by Type"),
    dcc.Graph(id="area-chart")
])
# Callback to update the area chart with cumulative trends
@callback(
    Output("area-chart", "figure"),
    Input("month-dropdown", "value") #Triggers update; not used directly
)
def update_area_chart(selected_month):
    df["Month"] = pd.to_datetime(df["Month"])
    cumulative_df = df.copy()
    cumulative_df = cumulative_df.groupby(["Month", "Crime type"]).size().reset_index(name="Cumulative Count")
    cumulative_df["Cumulative Total"] = cumulative_df.groupby("Crime type")["Cumulative Count"].cumsum()
    
    fig = px.area(
        cumulative_df,
        x="Month",
        y="Cumulative Total",
        color="Crime type",
        title="Cumulative Crime Trends by Type Over Time"
    )
    fig.update_layout(xaxis_title="Month", yaxis_title="Cumulative Crimes")
    return fig
