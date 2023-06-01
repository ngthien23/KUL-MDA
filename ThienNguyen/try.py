import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.Iframe(
            src="https://public.flourish.studio/visualisation/12841425/embed",
            style={"width": "100%", "height": "600px", "border": "none"},
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
