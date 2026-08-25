
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SequentialFeatureSelector
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


# Apply the Successive Feature Selection (SFS) to select 5 best features 
model=LogisticRegression()
sfs=SequentialFeatureSelector(model,n_features_to_select=5)

sfs=sfs.fit(X_train,y_train)


# Get the selected features
selected_features=X_train.columns[sfs.support_]
X_train_selected=X_train[selected_features]
X_test_selected=X_test[selected_features]


# Build the model
model_orig=LogisticRegression()
model_orig.fit(X_train,y_train)
y_pred_orig=model_orig.predict(X_test)

accuracy_orig=accuracy_score(y_test,y_pred_orig)
print('Accuracy of the base model is  : ',round(accuracy_orig*100,2))


# Build the SFS based model on 5 predictors
model_sfs=LogisticRegression()
model_sfs.fit(X_train_selected,y_train)
y_pred_sfs=model_sfs.predict(X_test_selected)

accuracy_sfs=accuracy_score(y_test,y_pred_sfs)
print('Accuracy of SFS based model is : ',round(accuracy_sfs*100,2))

print(len(sfs.feature_names_in_))



# Using mlxtend

from mlxtend.feature_selection import SequentialFeatureSelector


model2=LogisticRegression()
sfs2=SequentialFeatureSelector(model2,k_features=5,forward=True,floating=False,scoring='accuracy',cv=0)


sfs2=sfs2.fit(X_train,y_train)


# Get the selected features
selected_features=list(sfs2.k_feature_names_)
X_train_selected=X_train[selected_features]
X_test_selected=X_test[selected_features]



model_sfs2=LogisticRegression()
model_sfs2.fit(X_train_selected,y_train)
y_pred_sfs2=model_sfs2.predict(X_test_selected)

accuracy_sfs2=accuracy_score(y_test,y_pred_sfs2)
print('Accuracy of SFS based model is : ',round(accuracy_sfs2*100,2))

