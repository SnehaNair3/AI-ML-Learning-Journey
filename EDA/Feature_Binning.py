# FEATURE BINNING

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing


df=pd.read_csv('Churn_Modelling.csv')
df.head()
df.info()

df.drop(columns=['CustomerId','RowNumber','Surname'],axis=1,inplace=True)
df.head(5)

df.Age.min()
df.Age.max()

labels=['0-20','21-40','41-60','Above 61']
bins=[0,20,40,60,100]

df['Age_bins']=pd.cut(df.Age,bins,labels=labels,include_lowest=True)
df.head(5)

df[['Age','Age_bins']].to_csv('test.csv')
df.Age_bins.value_counts()

# Making the bar chart on the data
plt.bar(labels,df.Age_bins.value_counts())

# giving the title
plt.title('Age Count')

# giving x and y labels
plt.xlabel('Age Bins')
plt.ylabel('Age Count')

# Visualizing the plot
plt.show()


def add_labels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])


# MAKING THE BAR CHART ON THE DATA
plt.bar(labels,df.Age_bins.value_counts())

# add labels
add_labels(labels,df.Age_bins.value_counts())

# giving the title
plt.title('Age Count')

# giving x and y labels
plt.xlabel('Age Bins')
plt.ylabel('Age Count')

plt.show()

