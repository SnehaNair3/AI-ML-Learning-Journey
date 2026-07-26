import pandas as pd
import seaborn as sns
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import math
import pymysql
pd.set_option('display.max_column',None)


dbcon=pymysql.connect(host="localhost",user="root",password="Me@sqll123",database="breast_cancer_db")

dbcon

# Example for loading data from MySQL
# pandas.read_sql_query() - Read SQL query into a Dataframe
df=pd.read_sql_query(""" SELECT * FROM breastcancer WHERE diagnosis='M' """, dbcon,parse_dates=True)

df.head(5)

df.info()
df.shape
df.describe()

# checking the null values in the dataframe
df.isnull().sum()


sns.countplot(x="diagnosis",data=df)


sns.pairplot(df,hue="diagnosis")


labels=df['diagnosis']
values=df['mean_area']
fig=go.Figure(data=[go.Pie(labels=labels,values=values)])
fig.show()



labels=df['diagnosis']
values=df['mean_texture']
fig=go.Figure(data=[go.Pie(labels=labels,values=values)])
fig.show()




