

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_regression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split


X,y=make_regression(n_samples=10000,n_features=10,n_informative=3)
print(X)
print(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# Perform feature scaling here
# from sklearn.preprocessing import StandardScaler

# sc=StandardScaler()
# X_train_sc=sc.fit_transform(X_train)
# X_test_sc=sc.transform(X_test)


# First Model - Decision Tree Classifier
model_dt=DecisionTreeRegressor(random_state=42)
model_dt.fit(X_train,y_train)
y_pred_dt=model_dt.predict(X_test)
print('R2 Score DT : ', round(r2_score(y_test,y_pred_dt)*100,2),'%')
print('MAE DT : ', round(mean_absolute_error(y_test,y_pred_dt),2))
print('MSE DT : ', round(mean_squared_error(y_test,y_pred_dt),2))


# Bagging

bag=BaggingRegressor(estimator=DecisionTreeRegressor(),
                      n_estimators=500,
                      max_samples=0.5,
                      bootstrap=True,
                      random_state=42)


bag.fit(X_train,y_train)
y_pred_bag=bag.predict(X_test)

print('R2 Score Bagging : ', round(r2_score(y_test,y_pred_dt)*100,2),'%')
print('MAE Bagging : ', round(mean_absolute_error(y_test,y_pred_dt),2))
print('MSE Bagging : ', round(mean_squared_error(y_test,y_pred_dt),2))

# Random Forest
from sklearn.ensemble import RandomForestRegressor

model_rf=RandomForestRegressor(random_state=42,n_estimators=500)
model_rf.fit(X_train,y_train)
y_pred_rf=model_rf.predict(X_test)

print('R2 Score RF : ', round(r2_score(y_test,y_pred_dt)*100,2),'%')
print('MAE RF : ', round(mean_absolute_error(y_test,y_pred_dt),2))
print('MSE RF : ', round(mean_squared_error(y_test,y_pred_dt),2))

# Bagging using SVM
bag_svm=BaggingRegressor(estimator=SVR(),
                      n_estimators=500,
                      max_samples=0.25,
                      bootstrap=True,
                      random_state=42)


bag_svm.fit(X_train,y_train)
y_pred_svm=bag_svm.predict(X_test)

print('R2 Score SVM : ', round(r2_score(y_test,y_pred_dt)*100,2),'%')
print('MAE SVM : ', round(mean_absolute_error(y_test,y_pred_dt),2))
print('MSE SVM : ', round(mean_squared_error(y_test,y_pred_dt),2))



# Pasting
pasting=BaggingRegressor(estimator=DecisionTreeRegressor(),
                      n_estimators=500,
                      max_samples=0.25,
                      bootstrap=False,
                      random_state=42)


pasting.fit(X_train,y_train)
y_pred_pasting=pasting.predict(X_test)

print('R2 Score Pasting : ', round(r2_score(y_test,y_pred_dt)*100,2),'%')
print('MAE Pasting : ', round(mean_absolute_error(y_test,y_pred_dt),2))
print('MSE Pasting : ', round(mean_squared_error(y_test,y_pred_dt),2))
 


# Takeways : 
# 1 - Randon Forest is better than Bagges models
# Further Bagged models are better than Pasting
# 2 - Good results come around 25% to 50% row sampling
# 3 - To find the best parameters , we need to do hyper parameter optimization


