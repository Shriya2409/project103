import pandas as pd
import plotly_express as px

df=pd.read_csv("data.csv")
#fig=px.bar(df, x='Country', y='InternetUsers')
fig=px.scatter(df, x='Population', y='Per capita', size='Percentage', color='Country')
fig.show()
