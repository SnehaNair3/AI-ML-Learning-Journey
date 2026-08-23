import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


df=pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
df.head()

df.info()
# Converting TotalCharges to numericals
df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')
df.drop(['customerID'],axis='columns',inplace=True)

df['TotalCharges'].isnull().sum()

# NaN Imputation
df.dropna(how='any',inplace=True)
df['TotalCharges'].isnull().sum()
df.info()

df.head()

# Dummy encoding
df=pd.get_dummies(df,drop_first=True)
df.head(5)

# Churn Rate
df.Churn_Yes.value_counts()/len(df)*100


# Considering 'Churn' --> y-variable
# Other columns --> X variable

X=df.drop(['Churn_Yes'],axis=1)
y=df['Churn_Yes']

print(X)
print(y)




# Split the data into training and test sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=42)


# Apply the Recursive Feature Elimination (RFE) to select 5 best features 
model=LogisticRegression()
rfe=RFE(model,n_features_to_select=5)

rfe=rfe.fit(X_train,y_train)


# Get the selected features
selected_features=X_train.columns[rfe.support_]
X_train_selected=X_train[selected_features]
X_test_selected=X_test[selected_features]


# Build the model
model_orig=LogisticRegression()
model_orig.fit(X_train,y_train)
y_pred_orig=model_orig.predict(X_test)

accuracy_orig=accuracy_score(y_test,y_pred_orig)
print('Accuracy of the base model is  : ',round(accuracy_orig*100,2))


# Build the RFE based model on 5 predictors
model_rfe=LogisticRegression()
model_rfe.fit(X_train_selected,y_train)
y_pred_rfe=model_rfe.predict(X_test_selected)

accuracy_rfe=accuracy_score(y_test,y_pred_rfe)
print('Accuracy of RFE based model is : ',round(accuracy_rfe*100,2))


# 20 features
# Apply the Recursive Feature Elimination (RFE) to select 5 best features 
model2=LogisticRegression()
rfe=RFE(model2,n_features_to_select=20)

rfe=rfe.fit(X_train,y_train)


# Get the selected features
selected_features=X_train.columns[rfe.support_]
X_train_selected=X_train[selected_features]
X_test_selected=X_test[selected_features]


# Build the RFE based model on 5 predictors
model_rfe2=LogisticRegression()
model_rfe2.fit(X_train_selected,y_train)
y_pred_rfe=model_rfe2.predict(X_test_selected)

accuracy_rfe=accuracy_score(y_test,y_pred_rfe)
print('Accuracy of RFE based model is : ',round(accuracy_rfe*100,2))



