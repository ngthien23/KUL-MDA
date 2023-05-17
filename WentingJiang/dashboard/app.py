import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import folium
from folium.plugins import HeatMap

# Create dummy data for first chart
df1 = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Num of skills shared': [3, 4, 4, 6, 5, 8]
})

df2 = pd.DataFrame({
    'Skill category': ['Singing', 'Cooking', 'Writing', 'Painting', 'Communication', 'Interpersonal skills'],
    'Num of skills shared': [30, 40, 40, 60, 50, 80]
})

df3 = pd.DataFrame({
    'Profile matched': ['Alice', 'Carry', 'John', 'Wendy', 'Sam', 'Carol'],
    'Matching score': [20, 20, 5, 4, 2, 1]
})

# Load data
df = pd.read_csv('dummy.txt', header=None)
df.columns = ['city', 'lat', 'lon', 'temp', 'wind', 'humidity']

# Create dummy spots for each city
for city in df['city'].unique():
    city_df = df.loc[df['city'] == city]
    for i in range(5):
        new_row = {'city': city,
                   'lat': city_df['lat'].values[0] + i*0.001,
                   'lon': city_df['lon'].values[0] + i*0.001,
                   'temp': city_df['temp'].values[0],
                   'wind': city_df['wind'].values[0],
                   'humidity': city_df['humidity'].values[0]}
        #df = df.append(new_row, ignore_index=True)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Define app
app = dash.Dash(__name__)

# Define styles
styles = {
    'body': {
        'background-image': 'url("https://i.redd.it/kxwh4x4z7aua1.jpg")',
        'background-repeat': 'no-repeat',
        'background-size': 'cover',
        'background-position': 'center',
    },
    'button': {
        'background-color': '#008CBA',
        'color': 'white',
        'border': 'none',
        'padding': '10px 20px',
        'border-radius': '5px',
        'cursor': 'pointer',
    },
}

# Define layout
app.layout = html.Div(
    style=styles['body'],
    children=[
        html.H1("SkillAnother", style={'text-align': 'center'}),
        dcc.Tabs(id="tabs", value='tab-1', children=[
            dcc.Tab(label='Skill shared', value='tab-1', children=[
                html.Div([
                    html.H2('“Noise is the most impertinent of all forms of interruption..”', style={'text-align': 'center'}),
                    #Know me for my abilities, not my disability
                    html.P('-Arthur Schopenhauer', style={'text-align': 'center'}),
                    dcc.Graph(
                        id="graph-1",
                    #    figure=px.bar(df, x="city", y="temp")
                        figure = px.bar(df1, x="Month", y="Num of skills shared")
),
                    dcc.Dropdown(
                        id='city-dropdown',
                        options=[{'label': i, 'value': i} for i in df['city'].unique()],
                        value='Antwerp'
                    ),
                    html.Div([
                        html.Iframe(id='map', width='100%', height='400'),
                    ], style={'margin-top': '30px', 'text-align': 'center'})
                ], style={'margin-top': '30px', 'text-align': 'center'})
            ]),
            dcc.Tab(label='Community overview', value='tab-2', children=[
                html.Div([
                    html.H2('Most shared skills:', style={'text-align': 'center'}),
                    dcc.Graph(
                        id="graph-2",
                        figure=px.bar(df2, x="Skill category", y="Num of skills shared")#, color="city")
                    ),
                    dcc.Graph(
                        id="graph-3",
                        figure=px.bar(df3, x="Profile matched", y="Matching score")
                    ),
                ], style={'margin-top': '30px', 'text-align': 'center'})
            ]),
        ]),
        html.Button('Click me!', style=styles['button']),
    ],
)

# Define callback to update map
@app.callback(
    dash.dependencies.Output('map', 'srcDoc'),
    dash.dependencies.Input('city-dropdown', 'value')
)
def update_map(city):
    city_df = df.loc[df['city'] == city]
    m = folium.Map(location=[city_df['lat'].values[0], city_df['lon'].values[0]], zoom_start=12)
    heatmap_data = [[row['lat'], row['lon']] for index, row in city_df.iterrows()]
    HeatMap(heatmap_data).add_to(m)
    return m._repr_html_()

if __name__ == '__main__':
    app.run_server(debug=True)

