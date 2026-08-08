
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
from sklearn.metrics import r2_score

# iris=load_iris()
# iris.data
# iris.feature_names
# iris.target_names
# data=pd.DataFrame(iris.data,columns=iris.feature_names)
# target=pd.DataFrame(iris.target,columns=['target'])
# df=pd.concat([data,target],axis=1)

# df.head()

df=pd.read_csv('boston.csv')



# Split the data into features and target
X=df.iloc[:,:-1]
y=df.iloc[:,-1]




