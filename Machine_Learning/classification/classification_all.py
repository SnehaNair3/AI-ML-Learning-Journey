

# DATA --> EDA  --> Define X and y   -->   Feature Encoding  --> Train-test split  --> Feature Scaling  -->  Model training  --> Prediction


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

df.head(5)
df.info()

df.TotalCharges=pd.to_numeric(df.TotalCharges,errors='coerce')
df.info()

len(df)
df.dropna(how='any',inplace=True)
len(df)


df.Churn.value_counts()
df.Churn.value_counts()/len(df)*100


X=df.drop(['customerID','Churn'],axis=1)
y=df.Churn.values

print(X)
print(y)

print(X.columns)

# Feature Encoding --> Dummy encoding
# Convert categorical features to numericals
X=pd.get_dummies(X,columns=['gender','Partner', 'Dependents', 'tenure',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod'],drop_first=True)

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


print(X_train_sc)
print(X_test_sc)


# kNN Classifier
from sklearn.neighbors import KNeighborsClassifier

# Initiating the classifier
model=KNeighborsClassifier()

# Passing the data to classifier
model.fit(X_train_sc,y_train)


y_pred=model.predict(X_test_sc)

print(y_test)
print(y_pred)

# classification metrics
from sklearn.metrics import accuracy_score

print('Accuracy  kNN Classifier : ',accuracy_score(y_test,y_pred)*100)
# Accuracy  kNN Classifier :  75.99544937428895


# Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier

model_dt=DecisionTreeClassifier()

model_dt.fit(X_train_sc,y_train)


y_pred_dt=model_dt.predict(X_test_sc)

print(y_test)
print(y_pred_dt)

print('Accuracy of Decision Tree Classifier : ', accuracy_score(y_test,y_pred_dt)*100)
# Accuracy of Decision Tree Classifier :  73.77701934015927




# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

model_rf=RandomForestClassifier()

model_rf.fit(X_train_sc,y_train)


y_pred_rf=model_rf.predict(X_test_sc)


print('Accuracy of Random Forest Classifier : ', accuracy_score(y_test,y_pred_rf)*100)
# Accuracy of Random Forest Classifier :  77.98634812286689

from sklearn.metrics import recall_score,precision_score,classification_report

# print('Recall (RFT) : ', recall_score(y_test,y_pred_rf))
# recall - values should be 0 and 1 
# so do feature encoding ( label encoding -- target variable)
print('Recall : ',recall_score(y_test, y_pred_rf, pos_label='Yes'))


# classification report
print('kNN report : ',classification_report(y_test,y_pred))
print('DT report : ',classification_report(y_test,y_pred_dt))
print('RF report : ',classification_report(y_test,y_pred_rf))




# Naive Bayes Classifier
from sklearn.naive_bayes import BernoulliNB

model_nb=BernoulliNB()

model_nb.fit(X_train_sc,y_train)

y_pred_nb=model_nb.predict(X_test_sc)

print('Accuracy of NB Classifier : ',accuracy_score(y_test,y_pred_nb)*100)
# Accuracy of NB Classifier :  72.01365187713311




# SVM Classifier
from sklearn.svm import SVC

model_svc=SVC()

model_svc.fit(X_train_sc,y_train)

y_pred_svc=model_svc.predict(X_test_sc)

print('Accuracy of SVC Classifier : ',accuracy_score(y_test,y_pred_svc)*100)
# Accuracy of SVC Classifier :  78.78270762229806

print('SVC report : ',classification_report(y_test,y_pred_svc))



# Logistic Regression Classifier
from sklearn.linear_model import LogisticRegression

model_lr=LogisticRegression()

model_lr.fit(X_train_sc,y_train)

y_pred_lr=model_lr.predict(X_test_sc)

print('Accuracy score LR : ', accuracy_score(y_test,y_pred_lr)*100)
# Accuracy score LR :  79.01023890784982


