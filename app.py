#Libraries to build the dashboard
import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px

#Load cleaned crime data. This loads the combined data, converts month column to datetime and 
#creates a new column Month_Str like 2024-07 for the dropdown
df = pd.read_csv("data/processed/Combined_crime_data.csv")
df["Month"] = pd.to_datetime(df["Month"])
df["Month_Str"] = df["Month"].dt.strftime("%Y-%m")

#Create Dash app. This initialises the Dash app
app = dash.Dash(__name__)

# Define the layout of the page. This creates heading, dropdown menu to select month and a bar 
# chart placeholder
app.layout = html.Div([
    html.H2("UK Crime Dashboard - Monthly Overview"),

    html.Label("Select Month:"),
    dcc.Dropdown(
        id="month-dropdown",
        options=[
            {"label": month, "value": month} 
            for month in sorted(df["Month_Str"].unique())
        ],
        value=sorted(df["Month_Str"].unique())[-1],
        clearable=False
    ),
    dcc.Graph(id="crime-type-bar")
])

# Create Callback function to update bar chart. When the dropdown value changes, it filters 
# the data for the selected month, counts how many times the crime occurs and builds a bar chart using Plotly express
@app.callback(
    Output("crime-type-bar", "figure"),
    Input("month-dropdown", "value")
)
def update_chart(selected_month):
    filtered = df[df["Month_Str"] == selected_month]
    counts = filtered["Crime type"].value_counts().reset_index()
    counts.columns = ["Crime Type", "Count"]

    fig = px.bar(
        counts,
        x="Crime Type",
        y="Count",
        title=f"Crime by Type - {selected_month}",
        labels={"Count": "Number of Crimes"}
    )
    return fig

# Run server
if __name__ == "__main__":
    app.run(debug=True)
