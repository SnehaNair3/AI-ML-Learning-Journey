
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
df.head(5)
df.columns
df.info()
df.Churn.value_counts()/len(df)*100

X=df.drop(['customerID','Churn'],axis=1)
y=df.Churn.values

print(X)
print(y)


# Convert categorical features to numericls --> Feature Encoding --> Dummy Encoding
X=pd.get_dummies(X,columns=['gender','Partner', 'Dependents',
       'PhoneService', 'MultipleLines', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
       'PaymentMethod', 'TotalCharges'],drop_first=True)


X.head(1)

# Splitting data into training and test
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)

len(X_train)
len(X_test)


# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train_sc=sc.fit_transform(X_train)
X_test_sc=sc.transform(X_test)

X_train_sc
X_test_sc


# AdaBoost
# Call the AdaBoost Classifier
from sklearn.ensemble import AdaBoostClassifier

# Initiating the classifier
model_ada=AdaBoostClassifier(n_estimators=200)

# Passing the data to classifier
model_ada.fit(X_train_sc,y_train)

# Predictions
y_pred_ada=model_ada.predict(X_test_sc)

from sklearn.metrics import accuracy_score

print('Accuarcy Adaboost : ', accuracy_score(y_test,y_pred_ada)*100)


# Gradient Boost
# Call the Gradient Boost Classifier
from sklearn.ensemble import GradientBoostingClassifier

# Initiating the classifier
model_gradient=GradientBoostingClassifier(n_estimators=200)

# Passing the data to classifier
model_gradient.fit(X_train_sc,y_train)

# Predictions
y_pred_gradient=model_gradient.predict(X_test_sc)

from sklearn.metrics import accuracy_score

print('Accuarcy Gradient boost : ', accuracy_score(y_test,y_pred_gradient)*100)



# XGBoost

y[y=='No']=0
y[y=='Yes']=1



# Splitting data into training and test
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)

len(X_train)
len(X_test)

y_test=y_test.astype(int)
y_train=y_train.astype(int)


# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train_sc=sc.fit_transform(X_train)
X_test_sc=sc.transform(X_test)

X_train_sc
X_test_sc


# Call the Gradient Boost Classifier
from xgboost import XGBClassifier

# Initiating the classifier
model_xgb=XGBClassifier(n_estimators=200)

# Passing the data to classifier
model_xgb.fit(X_train_sc,y_train)

# Predictions
y_pred_xgb=model_xgb.predict(X_test_sc)

from sklearn.metrics import accuracy_score

print('Accuarcy XGboost : ', accuracy_score(y_test,y_pred_xgb)*100)


# 2nd parameter
# Initiating the classifier
model_xgb2=XGBClassifier(n_estimators=100)

# Passing the data to classifier
model_xgb2.fit(X_train_sc,y_train)

# Predictions
y_pred_xgb2=model_xgb2.predict(X_test_sc)

from sklearn.metrics import accuracy_score

print('Accuarcy XGboost : ', accuracy_score(y_test,y_pred_xgb2)*100)


# 3rd parameter
# Initiating the classifier
model_xgb3=XGBClassifier(n_estimators=100,max_depth=4)

# Passing the data to classifier
model_xgb3.fit(X_train_sc,y_train)

# Predictions
y_pred_xgb3=model_xgb3.predict(X_test_sc)

from sklearn.metrics import accuracy_score

print('Accuarcy XGboost : ', accuracy_score(y_test,y_pred_xgb3)*100)



# 4th parameter
# Initiating the classifier
model_xgb4=XGBClassifier(n_estimators=100,max_depth=4,learning_rate=0.1)

# Passing the data to classifier
model_xgb4.fit(X_train_sc,y_train)

# Predictions
y_pred_xgb4=model_xgb4.predict(X_test_sc)

from sklearn.metrics import accuracy_score

print('Accuarcy XGboost : ', accuracy_score(y_test,y_pred_xgb4)*100)






