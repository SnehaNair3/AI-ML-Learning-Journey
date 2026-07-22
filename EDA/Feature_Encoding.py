
# Feature Encoding

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing


df=pd.read_csv('Churn_Modelling.csv')
df.head(5)

df.info()

df.drop(columns=["CustomerId","RowNumber","Surname"],axis=1,inplace=True)
df.head(5)

df.Gender.value_counts()

# Handling missing values in Gender
df.Gender.mode()

df['Gender']=df['Gender'].fillna('Male')

df.Gender.value_counts()

df.info()

# Label Encoding
