import dash
import dash_core_components as dcc # these define higher level componenets with js and react
import dash_html_components as html #these describe html type components
import plotly.express as px
import pandas as pd  
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
app = dash.Dash(external_stylesheets= [dbc.themes.FLATLY])

# # make functional components 
# df  = pd.read_csv(r'C:\Users\Naman Bhoj\Desktop\Y\2021\Aug-Octo\ip_plotly_dash\PlotlyDash\plotlydash\data\csv\aggregated_scores.csv')



navbar = dbc.Navbar(id = "navbar" , children = [  

    dbc.Row([
        dbc.Col(html.H1(children = "This is navbar"  , style = {"textAlign" : "center"}))
    ])

])
   

app.layout = dbc.Container(
    dbc.Row([(  navbar)
    
    
    ]))
       


if __name__ == '__main__':
    app.run_server(debug =True)