
# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

# Reading the file
df=pd.read_csv('50_Startups.csv')

df.head()

df.info()
df.describe()


# Divide the data ito dependents vs independents
X=df.iloc[:,0].values
y=df.iloc[:,-1].values  # y is the last col

print(X)
print(y)


# Train Test Split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

len(X_train)
len(X_test)

print(X_test)
print(y_test)
print(X_train)


# This line is reshaping your data into a 2D array with one column.
#  It's one of the most common preprocessing steps in scikit-learn.
# (5,1) means 5 rows(samples) and 1 col
# (-1,1) means any no of rows and 1 col
# Most scikit-learn models expect the input X to be 2-dimensional.
# Why is X reshaped but not y?
# X represents the input features, which sklearn expects as a matrix of shape (n_samples, n_features).
# y represents the target values, which are expected as a 1D array of shape (n_samples,).
X_train=X_train.reshape(-1,1)
X_test=X_test.reshape(-1,1)



# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

print(X_test)

# Create Linear Regression Model
from sklearn.linear_model import LinearRegression

regressor=LinearRegression()
regressor.fit(X_train,y_train)


# Predictions
y_pred=regressor.predict(X_test)

# Plotting of y_test vs y_pred
plt.plot(y_test,color='blue',label='test')
plt.plot(y_pred,color='red',label='predicted')
plt.show()


# REGRESSION METRICS
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

mae=mean_absolute_error(y_test,y_pred)
print(mae)
mean_absolute_error(y_pred,y_test)

mse=mean_squared_error(y_test,y_pred)
print(mse)


rmse=np.sqrt(mse)
print(rmse)

r2=r2_score(y_pred,y_test)
print(r2)


# CALCULATE the adjusted R2 score
n=X_test.shape[0]
K=X_test.shape[1]

adjusted_r2=1-(1-r2)*(n-1)/(n-1-K)
print(adjusted_r2)




