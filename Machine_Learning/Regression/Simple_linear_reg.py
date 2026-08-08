
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv('50_Startups.csv')

df.head()
df.info()
df.describe()


X=df.iloc[:,0].values
y=df.iloc[:,-1].values

print(X)
print(y)


# Train test split
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

len(X_train)
len(X_test)


# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train=X_train.reshape(-1,1)
X_test=X_test.reshape(-1,1)

X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)


X_train
X_test



# Create Model

from sklearn.linear_model import LinearRegression

regressor=LinearRegression()
regressor.fit(X_train,y_train)


# Predictions
y_pred=regressor.predict(X_test)

# Plotting
plt.plot(y_test,color='blue',label='test')
plt.plot(y_pred,color='red',label='predicted')
plt.show()


# Out of box predictions

data=[[80000]]

new_df=pd.DataFrame(data)

new_df=sc.transform(new_df)

new_df

single=regressor.predict(new_df)
print(single)




