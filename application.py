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

application = Flask(__name__)

# Define app
app = dash.Dash(__name__,server=application,external_stylesheets=[dbc.themes.MATERIA])
df=pd.read_csv('./max_noise_per_minute_per_location.csv')
max_noise=df[['MP 01: Naamsestraat 35  Maxim','MP 02: Naamsestraat 57 Xior','MP 03: Naamsestraat 62 Taste','MP 04: His & Hers','MP 05: Calvariekapel KU Leuven','MP 06: Parkstraat 2 La Filosofia','MP 07: Naamsestraat 81','MP 08: bis - Vrijthof']].max().max()
min_noise=df[['MP 01: Naamsestraat 35  Maxim','MP 02: Naamsestraat 57 Xior','MP 03: Naamsestraat 62 Taste','MP 04: His & Hers','MP 05: Calvariekapel KU Leuven','MP 06: Parkstraat 2 La Filosofia','MP 07: Naamsestraat 81','MP 08: bis - Vrijthof']].min().min()
df[['MP 01: Naamsestraat 35  Maxim','MP 02: Naamsestraat 57 Xior','MP 03: Naamsestraat 62 Taste','MP 04: His & Hers','MP 05: Calvariekapel KU Leuven','MP 06: Parkstraat 2 La Filosofia','MP 07: Naamsestraat 81','MP 08: bis - Vrijthof']]=(df[['MP 01: Naamsestraat 35  Maxim','MP 02: Naamsestraat 57 Xior','MP 03: Naamsestraat 62 Taste','MP 04: His & Hers','MP 05: Calvariekapel KU Leuven','MP 06: Parkstraat 2 La Filosofia','MP 07: Naamsestraat 81','MP 08: bis - Vrijthof']]-min_noise)/(max_noise-min_noise)

metadata_dict={'MP 01: Naamsestraat 35  Maxim': (50.87725712,4.700745598),
               'MP 02: Naamsestraat 57 Xior': (50.87655782,4.70069841),
               'MP 03: Naamsestraat 62 Taste': (50.87590806,4.700202903),
               'MP 04: His & Hers': (50.87532021,4.700002902),
               'MP 05: Calvariekapel KU Leuven': (50.87452565,4.699911938),
               'MP 06: Parkstraat 2 La Filosofia': (50.87423474,4.699965129),
               'MP 07: Naamsestraat 81':(50.87391635,4.700123169),
               'MP 08: bis - Vrijthof': (50.87902068,4.701208869)}

date_input=dbc.Row([dbc.Label('Select date:', html_for='date-picker',width=10),
                    dbc.Col(dcc.DatePickerSingle(id='date-picker', date=date(2022,12,12)), width=8,),],
                    className='mb-3')

time_input=dbc.Row([dbc.Label('Select Time:', html_for='time-picker', width=10),
                    dbc.Col(dcc.Input(id='time-picker', value='12:00', type='text'), width=10,),], className='mb-3')

app.layout=dbc.Container([dbc.Row([dbc.Col(html.H1('Noise Heatmap of Leuven', className='text-center text-primary, mb-4'), width=12)]),
                          dbc.Row([dbc.Col([date_input,time_input], width={'size':4, 'offset':2})]),
                          dbc.Row([dbc.Col(html.Div(id='error-message', className='text-centered text-danger'), width={'size':8, 'offset':2})]),
                          dbc.Row([dbc.Col(html.Iframe(id='heatmap', width='100%', height=650), width={'size':8, 'offset':2}),],
                                    align='center', style={'height':'60%'})], style={'backgroundColor': '#c6ece6', 'height':'100%'}, fluid=True)

@app.callback([Output('heatmap', 'srcDoc'),
               Output('error-message', 'children')],
              [Input('date-picker', 'date'),
               Input('time-picker', 'value')])
def update_heatmap(selected_date,selected_time):
    date=datetime.strptime(selected_date, '%Y-%m-%d')
    reformatted_date=date.strftime('%Y-%d-%m')
    query=f'{reformatted_date} {selected_time}'
    print(f'Query is {query}')
    filtered_data=df[df['timestamp']==query]
    print(f'Filtered data frame: \n {filtered_data}')
    if filtered_data.empty:
        m=folium.Map(location=[50.87532021,4.700002902], zoom_start=16)
        return m._repr_html_(), 'Noise data is only available for the period between December 1 2022 and December 12 2022, please choose a date in this range, and specify the time in a "00:00" format'
    map_points=[]

    for label in ['MP 01: Naamsestraat 35  Maxim','MP 02: Naamsestraat 57 Xior','MP 03: Naamsestraat 62 Taste','MP 04: His & Hers','MP 05: Calvariekapel KU Leuven','MP 06: Parkstraat 2 La Filosofia','MP 07: Naamsestraat 81','MP 08: bis - Vrijthof']:
        latitude, longitude=metadata_dict[label]
        value_noise=filtered_data[label].values
        noise_level=value_noise[0]
        # print(f'Noise level is: {noise_level}')
        map_points.append((latitude, longitude, noise_level))
    print(f'Map points: \n {map_points}')

    gradient = {0.0: 'blue', 0.3: 'yellow', 1: 'red'}
    m=folium.Map(location=[50.87532021,4.700002902], zoom_start=16)
    HeatMap(data=map_points, radius=8, max_zoom=13, max_val=0, gradient=gradient).add_to(m)

    return m._repr_html_(),''

if __name__ == '__main__':
    application.run(debug=True)