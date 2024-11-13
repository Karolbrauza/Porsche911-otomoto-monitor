import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

def load_data(filename='porsche_911_offers.csv'):
    return pd.read_csv(filename)

def analyze_data(df):
    trends = df.groupby('location').agg({'price': ['mean', 'min', 'max']})
    return trends

def create_visualizations(df):
    plt.figure(figsize=(10, 6))
    df['price'].hist(bins=30)
    plt.title('Price Distribution of Porsche 911 Offers')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.savefig('price_distribution.png')

    fig = px.scatter(df, x='price', y='location', title='Price vs Location')
    fig.write_html('price_vs_location.html')

def create_dashboard(df):
    app = dash.Dash(__name__)

    app.layout = html.Div(children=[
        html.H1(children='Porsche 911 Offers Dashboard'),

        dcc.Graph(
            id='price-distribution',
            figure={
                'data': [
                    {'x': df['price'], 'type': 'histogram', 'name': 'Price'},
                ],
                'layout': {
                    'title': 'Price Distribution'
                }
            }
        ),

        dcc.Graph(
            id='price-vs-location',
            figure=px.scatter(df, x='price', y='location', title='Price vs Location')
        )
    ])

    app.run_server(debug=True)

if __name__ == "__main__":
    data = load_data()
    trends = analyze_data(data)
    create_visualizations(data)
    create_dashboard(data)
