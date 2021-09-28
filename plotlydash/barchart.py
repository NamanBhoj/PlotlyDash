import plotly.graph_objects as go      
import plotly.express as px  #read data
#plot data
from plotly.offline import plot
import os
import pandas as pd

# DIRECTORY_PATH = os.path.abspath(os.path.dirname(__file__))
# data_path = os.path.join(DIRECTORY_PATH , '/data/csv/', 'aggregated_score.csv')


#reading data 
data = pd.read_csv(r"data/csv/aggregated_scores.csv")

# graph object is used  to define how the graph should look
# THIS IS TO SEE THE WHOLE DATA NOW SAY YOU WANT TO COMPARE TWO BANKS THATS NETX
fig = go.Figure([go.Bar(x = data['bank'], y = data['cx_quantitative_score'], marker_color = 'green')])
fig.update_layout(title= "Bar Chart of " + "Bank V/S Cx_quantitative_score" , xaxis_title = "Bank", yaxis_title= "Cx_qunatitative_Score" )
# TODO: "MAKE THE UPDAATION OF THIS NAME DYNAMIC IN LINE 17"





#COMPARE TWO Bankers

# data1 = data.query("bank='Bendigo'")
# # data2 = data.query("bank='ANZ'")


# print(data1)


# now plot it using plot function
plot(fig)


