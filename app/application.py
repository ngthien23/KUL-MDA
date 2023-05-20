import pandas as pd
import plotly.express as px
import dash
import folium
from folium.plugins import HeatMap
import dash_bootstrap_components as dbc
from dash import Input,Output, dash_table,html,dcc
from flask import Flask
# from jupyter_dash import JupyterDash

application = Flask(__name__)

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
app = dash.Dash(__name__,server=application,external_stylesheets=[dbc.themes.MATERIA])
# app = JupyterDash(__name__,external_stylesheets=[dbc.themes.MATERIA])

#Define layout
app.layout=html.Div(style={'background-image': 'url("https://i.redd.it/kxwh4x4z7aua1.jpg")','background-repeat': 'no-repeat','background-size': 'cover','background-position': 'center', 'height':'100vh','margin':'0'},
                     children=[dbc.Container([dbc.Row(html.Div('SkilledAnother', className="text-primary text-center fs-3"),className='my-2'),
                                              dbc.Row([dbc.Col(html.H2('Skilled sharing', className="text-primary text-center fs-3")),
                                                       dbc.Col([dcc.Dropdown(id='city-dropdown',options=[{'label': i, 'value': i} for i in df['city'].unique()],value='Antwerp')])],className='my-2'),
                                                       dbc.Row([dbc.Col([dcc.Graph(id="graph-1",figure = px.bar(df1, x="Month", y="Num of skills shared"))]),
                                                                dbc.Col(html.Div([html.Iframe(id='map', width='100%', height='400'),], style={'margin-top': '30px', 'text-align': 'center'},className='my-2'))
                                                                ])],fluid=True)])
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
    application.run()



