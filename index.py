python
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Initialize Dash app
app = dash.Dash(__name__)

# Load dataset
data = pd.read_excel("./data/Distribution_of_Active_Members.xlsx")

# Create a sample visualization - distribution by age band
fig = px.bar(data, x='Age Band', y='Count', color='Gender', 
             title='Distribution of Active Members by Age and Gender')

# App layout
app.layout = html.Div([
    html.H1("Active Members Statistics in 2023", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig),
    html.Div("Select filters below to customize the data visualization:", style={'margin': '20px 0'}),
    dcc.Dropdown(
        id='sector-filter',
        options=[
            {'label': sector, 'value': sector} for sector in data['Sector'].unique()
        ],
        value='All Sectors',
        placeholder='Select a sector to filter data',
        style={'width': '50%'}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
