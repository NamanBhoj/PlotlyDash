import dash
import dash_core_components as dcc # these define higher level componenets with js and react
import dash_html_components as html #these describe html type components
import plotly.express as px
import pandas as pd  
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
app = dash.Dash(external_stylesheets= [dbc.themes.FLATLY])

# make functional components 
df  = pd.read_csv(r'C:\Users\Naman Bhoj\Desktop\Y\2021\Aug-Octo\ip_plotly_dash\PlotlyDash\plotlydash\data\csv\aggregated_scores.csv')





def bar_chart(data):

    fig = px.bar(data, x= "bank", y ="sv_rating")

    # fig.update_layout(xaxis = "Bank" , yaxis = "SV Rating")

    return fig

app.layout= dbc.Container(
    [dbc.Row([dbc.Col([html.H1( id = "h1" , children = "H App")])], style= {'textAlign' : 'center'} )
#create new row for graph and if two graphs and you need them in same row then you create two columns inside the same row
,
     dbc.Row([dbc.Col([dcc.Graph(id = "bar", figure = bar_chart(df))])])
    ])

   
       


if __name__ == '__main__':
    app.run_server(debug =True)