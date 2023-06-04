import pandas as pd
import plotly.express as px
import dash
import folium
from folium.plugins import HeatMap
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import html,dcc
from flask import Flask
from datetime import date, datetime
import plotly.graph_objects as go
import os

#Here the application's server is setup in flask so that it is compatible by default with AWS Elastic Beanstalk. It is called 'application' because that is a requirement for the selected deployment option 
application = Flask(__name__)

# The app is created in Dash using Flask as the server
app = dash.Dash(__name__,server=application,external_stylesheets=[dbc.themes.MATERIA])
#The processed data is read from the csv file
df=pd.read_csv('./max_noise_per_hour_per_location.csv')
#The max and minimum of the data are determined
max_noise=df[['MP 01: Naamsestraat 35  Maxim','MP 02: Naamsestraat 57 Xior','MP 03: Naamsestraat 62 Taste','MP 05: Calvariekapel KU Leuven','MP 06: Parkstraat 2 La Filosofia','MP 07: Naamsestraat 81']].max().max()
min_noise=df[['MP 01: Naamsestraat 35  Maxim','MP 02: Naamsestraat 57 Xior','MP 03: Naamsestraat 62 Taste','MP 05: Calvariekapel KU Leuven','MP 06: Parkstraat 2 La Filosofia','MP 07: Naamsestraat 81']].min().min()
# print(f'Max noise is: {max_noise} and Min noise is: {min_noise}')

#A function is defined to create a bar plot showing the gradient of colors used for the heatmap with the numeric values that define these color ranges
def create_color_scale():
    color_scale=[[0, 'blue'],[0.4, 'lime'],[0.6,'yellow'],[0.8,'orange'], [1,'red']]
    values=[30,60,80,100,120]
    fig=go.Figure(data=go.Heatmap(z=[values,values],x=['',''],y=['',''],zmin=0,zmax=120, colorscale=color_scale, colorbar=dict(tickmode='array',tickvals=[30,60,80,100,120],ticktext=['30 dB', '60 dB', '80 dB', '100 dB', '120 dB']),showscale=True))
    fig.update_layout(width=160, height=600)
    return fig

#A meta data dictionary is created with the coordinates of the different locations
metadata_dict={'MP 01: Naamsestraat 35  Maxim': (50.87725712,4.700745598),
               'MP 02: Naamsestraat 57 Xior': (50.87655782,4.70069841),
               'MP 03: Naamsestraat 62 Taste': (50.87590806,4.700202903),
               'MP 04: His & Hers': (50.87532021,4.700002902),
               'MP 05: Calvariekapel KU Leuven': (50.87452565,4.699911938),
               'MP 06: Parkstraat 2 La Filosofia': (50.87423474,4.699965129),
               'MP 07: Naamsestraat 81':(50.87391635,4.700123169),
               'MP 08: bis - Vrijthof': (50.87902068,4.701208869)}

#Options of the dropdown menu for the time
times = ["{:02d}:00".format(i) for i in range(24)]
##Dash-bootstrap components is used in conjunction with dash to provide more efficient customization of the app's layout
#The component for taking the input for the date is created
date_input=dbc.Row([dbc.Label('Select date:', html_for='date-picker',width=10),
                    dbc.Col(dcc.DatePickerSingle(id='date-picker', date=date(2022,12,12)), width=8,),],
                    className='mb-3')

#The component for taking the input for the time is created
time_input=dbc.Row([dbc.Label('Select Time:', html_for='time-picker', width=10),
                    dbc.Col(dcc.Dropdown(id='time-picker', options=[{'label': time, 'value': time} for time in times], value=times[0]), width=10,),], className='mb-3')

image1_path = 'shap.png'
image2_path = 'shap2.png'

#The app's layout is define using row and column components to organize it
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H1('Noise Heatmap of Leuven', className='text-center text-primary, mb-4'),
                    width=12
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col([date_input, time_input], width={'size': 8, 'offset': 1})
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(id='error-message', className='text-centered text-danger'),
                    width={'size': 8, 'offset': 1}
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Iframe(id='heatmap', width='100%', height=650),
                    width={'size': 8, 'offset': 1},
                    style={'position': 'relative'}
                ),
                dbc.Col(
                    dcc.Graph(id='colorscale', figure=create_color_scale()),
                    width={'size': 1, 'offset': 0},
                    style={'position': 'relative'}
                )
            ],
            align='center',
            style={'height': '60%'}
        ),
        html.Div(
            [
                html.Iframe(
                    src="https://public.flourish.studio/visualisation/13994608/embed",
                    style={"width": "100%", "height": "800px", "border": "double"}
                )
            ],
            style={'position': 'center', 'bottom': '0', 'left': '0', 'width': '100%'}
        )
    ],
    style={'backgroundColor': '#c6ece6', 'height': '100%'},
    fluid=True
)


#A function with call back is created so that the heatmap is updated for the data and time input by the user
@app.callback([Output('heatmap', 'srcDoc'),
               Output('error-message', 'children')],
              [Input('date-picker', 'date'),
               Input('time-picker', 'value')])
def update_heatmap(selected_date,selected_time):
    # date=datetime.strptime(selected_date, '%Y-%m-%d')
    # reformatted_date=date.strftime('%Y-%d-%m')
    query=f'{selected_date} {selected_time}:00'
    # print(f'Query is {query}')
    filtered_data=df[df['timestamp']==query]
    # print(f'Filtered data frame: \n {filtered_data}')
    #This part displays an error message and an empty map of Leuven if the user selected time and date are not in the range of available data
    if filtered_data.empty:
        m=folium.Map(location=[50.87532021,4.700002902], zoom_start=16)
        return m._repr_html_(), 'Noise data is only available for days 3 to 12 of each month for all months of year 2022, and only between the hours 17:00 and 03:00, please choose a date and time in one of these ranges.'
    map_points=[]
    #This pairs the coordinates with the noise level data to create the points that will be shown by the heatmap
    for label in ['MP 01: Naamsestraat 35  Maxim','MP 02: Naamsestraat 57 Xior','MP 03: Naamsestraat 62 Taste','MP 05: Calvariekapel KU Leuven','MP 06: Parkstraat 2 La Filosofia','MP 07: Naamsestraat 81']:
        latitude, longitude=metadata_dict[label]
        value_noise=filtered_data[label].values
        noise_level=value_noise[0]
        # print(f'Noise level is: {noise_level}')
        map_points.append((latitude, longitude, noise_level))
    # print(f'Map points: \n {map_points}')

    #This defined the gradient of colors used for the heatmap and the ranges of values for each color
    gradient={0.0: 'blue', ((60-min_noise)/(max_noise-min_noise)): 'lime', ((80-min_noise)/(max_noise-min_noise)): 'yellow', ((100-min_noise)/(max_noise-min_noise)): 'orange', 1: 'red'}

    #Here a folium map object is initialized with Leuven's coordinates
    m=folium.Map(location=[50.87532021,4.700002902], zoom_start=16)
    #Here a heatmap object from folium, displaying the points of data for the user selected date and time, is added to the folium map object
    HeatMap(data=map_points, radius=16, max_zoom=13, gradient=gradient, blur=14).add_to(m)

    return m._repr_html_(),''

#This runs the app when the script is executed
if __name__ == '__main__':
    application.run(debug=False)