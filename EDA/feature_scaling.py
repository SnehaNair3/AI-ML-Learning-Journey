import sys
print(sys.executable)
print(sys.version)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("All imports done.")

df=pd.read_csv('Churn_Modelling.csv')
df.info()

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

# What is Normalization?
# Normalization is the technique in which values are shifted and rescaled so that they end up ranging between 0 and 1.
# It is also known as Min-Max scaling.

# What is Standardization?
# Standardization is another scaling technique where the values are centered around the mean with a unit standard deviation.
# This means that the mean of the attribute becomes zero and the resultant distribution has a unit standard deviation.

df.head()
df.describe().round(2)


# TASK 1 - NORMALIZATION
df.head(5)
new_df=pd.DataFrame(df,columns=['Age','Tenure'])
new_df.head(5)

# Imputing the null values with the mean value
new_df['Age']=new_df['Age'].fillna(new_df['Age'].mean())
new_df.info()

scaler=MinMaxScaler() # Instantiating the MinMaxScaler() function
normalized_df=scaler.fit_transform(new_df)
print(normalized_df)

# EXAMPLE
x_array=np.array([[2],[3],[5],[6],[6]])

scaler=MinMaxScaler()
normalized_arr=scaler.fit_transform(x_array)
print(normalized_arr)

# STANDARDIZATION
scaler=StandardScaler()
standardized_df=scaler.fit_transform(new_df)
print(standardized_df)

# Example
x_array=np.array([[2],[3],[5],[6],[6]])
standardized_arr=scaler.fit_transform(x_array)
print(standardized_arr)