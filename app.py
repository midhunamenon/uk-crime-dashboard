import dash
from dash import Dash, html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Hello, UK Crime Dashboard!"),
    html.P("If your are seeing this, Dash is working.")
])

if __name__ == '__main__':
    app.run(debug=True)

