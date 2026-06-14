# Handling Missing Values

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Churn_Modelling.csv')


df.info()

# The second way of finding whether the data has b=null values is by using the isnull() function
print(df.isnull().sum())

# Handling Missing Values

# 1 - Deleting the columns with missing data
updated_df=df.dropna(axis=1)
updated_df.info()

# The problem with this method is that we may lose some valuableinformation on that feature, as we have completely deleted it due to some null values.
# Should be used only if there are too many null values.


# 2 -- Deleting the rows with missing data
updated_df=df.dropna(axis=0)
updated_df.info()

# In this case, there are possibilities of getting better accuracy than before.THis might be because the columns contain more valuable information than we expected.


# 3 -- Filling the missing values - Imputation
# The possible ways to do this are:
   # Filling the missing data with ht emean or median if its a numerical value.
   # Filling the missing value with mode if its a categorical variable.
   # Filling the numerical value with 0 or -999, or some other number that will not occur in the data. This can be done so that the machine can recognise that the data is not real or is different.
   # Filling the categorical value with a new type for the missing values.

df['Age'].mean()  

df['Age'].median()

updated_df=df
updated_df['Age']=updated_df['Age'].fillna(df['Age'].mean())
updated_df.info()

# fillna - fills the null records
# dropna - drops the null records

updated_df1=df
updated_df1['Age']=updated_df['Age'].fillna(df['Age'].median())
updated_df1.info()

# When you have too many outliers ,its better to use median.
# When you have less outliers, its better to use mean.


# 4 -- Forward and Backward Filling - Imputation
df=pd.read_csv('Churn_Modelling.csv')
df.info()

df1=df
df1['Age']=df1['Age'].bfill()  # Backward fill
df1.info()

df1['Age']=df1['Age'].ffill()  # Forward fill