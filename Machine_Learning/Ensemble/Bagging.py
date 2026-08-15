
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split


X,y=make_classification(n_samples=10000,n_features=10,n_informative=3)
print(X)
print(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# Perform feature scaling here
# from sklearn.preprocessing import StandardScaler

# sc=StandardScaler()
# X_train_sc=sc.fit_transform(X_train)
# X_test_sc=sc.transform(X_test)


# First Model - Decision Tree Classifier
model_dt=DecisionTreeClassifier(random_state=42)
model_dt.fit(X_train,y_train)
y_pred_dt=model_dt.predict(X_test)
print('Accuracy DT : ', round(accuracy_score(y_test,y_pred_dt)*100,2),'%')


# Bagging

bag=BaggingClassifier(base_estimator=DecisionTreeClassifier(),
                      n_estimators=500,
                      max_samples=0.5,
                      bootstrap=True,
                      random_state=42)

