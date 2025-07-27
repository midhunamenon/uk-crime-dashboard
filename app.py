#Libraries to build the dashboard
import dash
from components.layout import layout

# Initialise app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "UK Crime Dashboard"
app.layout = layout

# Run server
if __name__ == "__main__":
    app.run(debug=True)