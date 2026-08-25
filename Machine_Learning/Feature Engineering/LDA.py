
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
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


# Build the model
model_orig=LogisticRegression()
model_orig.fit(X_train,y_train)
y_pred_orig=model_orig.predict(X_test)

accuracy_orig=accuracy_score(y_test,y_pred_orig)
print('Accuracy of the base model is  : ',round(accuracy_orig*100,2))


# Applying LDA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

lda=LinearDiscriminantAnalysis()
X_train_lda=lda.fit_transform(X_train,y_train)
X_test_lda=lda.transform(X_test)


explained_variance=lda.explained_variance_ratio_

print(explained_variance)  # variance of the 5 features


# Training the logistic regression on the training set
model_lda=LogisticRegression()
model_lda=model_lda.fit(X_train_lda,y_train)
y_pred_lda=model_lda.predict(X_test_lda)


accuracy_lda=accuracy_score(y_test,y_pred_lda)
print('Accuracy of the LDA  model is  : ',round(accuracy_lda*100,2))