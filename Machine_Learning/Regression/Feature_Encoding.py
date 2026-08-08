
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing



df=pd.read_csv('Churn_Modelling.csv')

df.info()

df.drop(columns=["CustomerId","RowNumber","Surname"],axis=1,inplace=True)
df.head(5)

df.Gender.value_counts() # only counts the current non-null values (if there are null values it wont be counted.)

# Handling missing values in Gender
df.Gender.mode()

df['Gender']=df['Gender'].fillna('Male')
df.info()


# LABEL ENCODING
# only for target variables.
# sklearn.preprocessing.LabelEncoder
le=preprocessing.LabelEncoder()
df['Gender_label']=le.fit_transform(df.Gender.values)
df.head(5)

df.Gender_label.value_counts()



# ONE-HOT ENCODING
# sklearn.preprocessing.OneHotEncoder
# pandas.get_dummies()
one_hot=pd.get_dummies(df['Geography'])
one_hot

# There are only 2 categorical data here, so encoding can be done only to Gender and Geography
#If we want to apply encoding to all the categorical data in the dataset:
df_dummies=pd.get_dummies(df)
df_dummies.head(5)




# DUMMY ENCODING
df_dummies_de=pd.get_dummies(df,drop_first=True)
df_dummies_de.head()



