
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')


df.info()

df.TotalCharges=pd.to_numeric(df.TotalCharges,errors='coerce')

df.info()
# 11 missing values in TotalCharges now.
# small % (less than 1 %)  - so just get rid of those missing values.
df.dropna(how='any',inplace=True)
# wherever there is null value, drop it

df.head(5)

df.Churn.value_counts()
# Percentage
df.Churn.value_counts()/len(df)*100
# Almost 73% are active customers.


X=df.drop(['customerID','Churn'],axis=1)
y=df.Churn.values

X.columns

print(y)

# Convert categorical features to numericals --> Feature Encoding'

X=pd.get_dummies(X,columns=['gender', 'Partner', 'Dependents', 
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod'],drop_first=True)


X.head(1)


# Splitting the data into training and test
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)

len(X_train)
len(X_test)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train_sc=sc.fit_transform(X_train)
X_test_sc=sc.transform(X_test)

# Scaled values
X_train_sc

X_test_sc



# kNN Classifier

# Call the KNN classifier
from sklearn.neighbors import KNeighborsClassifier

# Initiating the classifier
model=KNeighborsClassifier()

# Passing the  data to classifier
model.fit(X_train_sc,y_train)

# Predicting
y_pred=model.predict(X_test_sc)

print(y_pred)
print(y_test)



# Classification metrics - to check how the model is behaving

from sklearn.metrics import accuracy_score
round(accuracy_score(y_test,y_pred)*100,2)



# New Data Prediction
data=[[0,2,178,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0]]

data_sc=sc.transform(data)

single=model.predict(data_sc)
print(model.predict_proba(data_sc))

print(single)






