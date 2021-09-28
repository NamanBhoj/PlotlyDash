import plotly.graph_objects as go      
import plotly.express as px  #read data
#plot data
from plotly.offline import plot
import os
import pandas as pd

data = pd.read_csv(r"data/csv/aggregated_scores.csv")





fig = go.Figure(data = [go.Scatter(x= data['bank'], y = data['cx_quantitative_score'], marker_color = 'red')])
fig.update_layout(title= "Bar Chart of " + "Bank V/S Cx_quantitative_score" , xaxis_title = "Bank", yaxis_title= "Cx_qunatitative_Score" )


plot(fig)