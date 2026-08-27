
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score


data=pd.read_csv('breast_cancer.csv')
data.head(5)


# Distribution of y-variable
data.diagnosis.value_counts()

data.diagnosis.value_counts()/len(data)*100

data.shape
# 569 records(rows) and 33 columns

# Convert B and M into 0 and 1.
data['diagnosis']=data['diagnosis'].map({'M':1, 'B':0})

data.head()
data.diagnosis.value_counts()


# X and y
X=data.iloc[:,[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]]
y=data.diagnosis.values



# Train and test split
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


len(X_train)
len(X_test)

len(X_train)/len(data)*100


# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train_sc=sc.fit_transform(X_train)
X_test_sc=sc.transform(X_test)


# Model Building
from sklearn.ensemble import RandomForestClassifier

model=RandomForestClassifier()
model.fit(X_train_sc,y_train)

# Preicting on tst values
y_pred_rf=model.predict(X_test_sc)

# Mterics
from sklearn.metrics import confusion_matrix, classification_report

print('Accuracy of RF model : ',accuracy_score(y_test,y_pred_rf)*100)

print('CM is : ',confusion_matrix(y_test,y_pred_rf))
print('Classification Report is : ',classification_report(y_test,y_pred_rf))


# Manual HPO
n_estimaors_list=[1,2,3,10,50,100,200]

for estim_list in n_estimaors_list:
    model=RandomForestClassifier(n_estimators=estim_list)
    model.fit(X_train_sc,y_train)
    y_pred=model.predict(X_test_sc)
    result=accuracy_score(y_test,y_pred)
    print('\n Estimator value : ',estim_list)
    print('Accuracy is : ',result)


leaf_size=[1,2,3,4,5,10]

for i in leaf_size:
    model=RandomForestClassifier(n_estimators=50,min_samples_leaf=i)
    model.fit(X_train_sc,y_train)
    y_pred=model.predict(X_test_sc)
    result=accuracy_score(y_test,y_pred)
    print('\n Estimator value : ',estim_list)
    print('Accuracy is : ',result)

