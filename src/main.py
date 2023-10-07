from county import *
from format_data import *

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

counties = []

def prepare_data():
    raw_csv_filepath = 'data/Raw_Input.csv'
    new_csv_filepath = 'data/new_csv.csv'
    format_data(raw_csv_filepath, new_csv_filepath)
    init_counties(counties)
    update_counties(counties,'2015')
    print([(c.get_name(), c.get_avg_prices()) for c in counties])

prepare_data()

app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Dropdown(
        id='slct_county',
        options=[c.get_name() for c in counties],
        value='Dublin'
    )
])

if __name__ == '__main__':
    prepare_data()
    app.run_server(debug=True)