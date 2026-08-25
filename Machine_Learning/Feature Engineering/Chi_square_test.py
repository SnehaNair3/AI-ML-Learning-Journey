
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import chi2, SelectKBest
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




model=LogisticRegression()

# Apply chi2
chi2_selector=SelectKBest(chi2,k=5)
X_train_chi2=chi2_selector.fit_transform(X_train,y_train)

X_test_chi2=chi2_selector.transform(X_test)


# Build the model
model_chi2=LogisticRegression()
model_chi2.fit(X_train_chi2,y_train)
y_pred_chi2=model_chi2.predict(X_test_chi2)

accuracy_chi2=accuracy_score(y_test,y_pred_chi2)
print('Accuracy of the chi2 based model is  : ',round(accuracy_chi2*100,2))





