
# Importing libraries
import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt


# REading  the file
df=pd.read_csv('50_Startups.csv')
df.head(5)
df.info()
df.describe()

# Divide the data into dependents vs independents
# X=df.drop('Profit').values
# y=df['Profit'].values

X=df.iloc[:,:-1].values
y=df.iloc[:,-1].values

print(X)
print(y)


# Feature Encoding - OneHot Encoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])],remainder='passthrough')

X=np.array(ct.fit_transform(X))

print(X)


# Train Test Split
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

len(X_train)
len(X_test)


# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)


# Create LR Model
from sklearn.linear_model import LinearRegression

regressor=LinearRegression()
regressor.fit(X_train,y_train)


# Predictions

y_pred=regressor.predict(X_test)

# Plotting of y_test and y_pred
plt.plot(y_test, color='blue',label='test')
plt.plot(y_pred,color='red',label='predictions')
plt.show()


# Out of the box predictions
data=[[1.0, 0.0 ,0.0, 80000, 125000, 250000]]
new_df=pd.DataFrame(data)
new_df=sc.transform(new_df)
print(new_df)

single=regressor.predict(new_df)
print(single)
