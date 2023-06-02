import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.Iframe(
            src="https://public.flourish.studio/visualisation/13994608/embed",
            style={"width": "100%", "height": "800px", "border": "double"},
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
