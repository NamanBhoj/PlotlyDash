import dash
import dash_core_components as dcc # these define higher level componenets with js and react
import dash_html_components as html #these describe html type components
import plotly.express as px
import pandas as pd  

app = dash.Dash(__name__)

# make functional components 
df  = pd.read_csv(r'C:\Users\Naman Bhoj\Desktop\Y\2021\Aug-Octo\ip_plotly_dash\PlotlyDash\plotlydash\data\csv\aggregated_scores.csv')

fig = px.bar(df, x= "bank", y ="sv_rating")

app.layout= html.Div(
    children=[html.H1(children = "Hi App"), dcc.Graph(id = 'example', figure = fig)]

    
)

if __name__ == '__main__':
    app.run_server(debug =True)