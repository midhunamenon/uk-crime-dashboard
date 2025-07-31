import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html, Input, Output, callback
from utils.data_processing import combined_df

# Dropdown options
months = sorted(combined_df["Month_Name"].unique())

# Layout for the heatmap component
heatmap_layout = html.Div([
    html.H3("Crime Distribution Heatmap by Region"),
    dcc.Dropdown(
        id="heatmap-month-dropdown",
        options=[{"label": m, "value": m} for m in months],
        value=months[0],  # Default to the first month
        clearable=False
    ),
    dcc.Graph(id="crime-heatmap")
])

# Callback to update the heatmap based on selected month
@callback(
    Output("crime-heatmap", "figure"),
    Input("heatmap-month-dropdown", "value")
)
def update_heatmap(selected_month):
    # Filter the data for the selected month
    filtered_df = combined_df[combined_df["Month_Name"] == selected_month]

    # group by region and crime type to create a pivot table
    filtered_df["Area"] = filtered_df["LSOA name"].str.extract(r"^(.*?)(?:\s\d{3}[A-Z])?$")[0]
    pivot_df = (
       filtered_df.groupby(["Area", "Crime type"])
       .size()
       .unstack(fill_value=0)
       .sort_index()
    )
    
    #create annotations for heatmap cells
    annotations = []
    for i, region in enumerate(pivot_df.index):
        for j, crime in enumerate(pivot_df.columns):
            value = pivot_df.iloc[i, j]
            annotations.append(
                dict(
                    x=crime,
                    y=region,
                    text=str(value),
                    showarrow=False,
                    font=dict(
                        color="white" if value > pivot_df.values.max() * 0.5 else "black"
                    )
                )
            )
    
    # Dynamically adjust height based on number of areas
    num_areas = len(pivot_df.index)
    chart_height = max(500, num_areas * 25) # 25px per area, minimum 500

    # Create the heatmap figure
    fig = go.Figure(
        data=go.Heatmap(
            z=pivot_df.values,
            x=pivot_df.columns,
            y=pivot_df.index,
            colorscale="Viridis",
            colorbar=dict(title="Crime Count")
        )
    )

    fig.update_layout(
        height=chart_height,
        title=f"Crime Type by Region - {selected_month}",
        xaxis_title="Crime Type",
        yaxis_title="Region",
        annotations=annotations,
        margin=dict(l=120, r=20, t=40, b=80)
    )
    return fig


