
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score


df=pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

df.TotalCharges=pd.to_numeric(df.TotalCharges,errors='coerce')
df.dropna(how='any',inplace=True)
X=df.drop(['customerID','Churn'],axis=1)
y=df.Churn.values
X.columns


# Convert categorical faetures to numericals --> Feature Encoding --> Dummy Encoding
X=pd.get_dummies(X,columns=['gender', 'Partner', 'Dependents',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod'],drop_first=True)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train_sc=sc.fit_transform(X_train)
X_test_sc=sc.transform(X_test)


# Call the DT classifier
from sklearn.tree import DecisionTreeClassifier

model_dt=DecisionTreeClassifier()

model_dt.fit(X_train_sc,y_train)

y_pred_dt=model_dt.predict(X_test_sc)

print('Accuracy DT : ',accuracy_score(y_test,y_pred_dt)*100)

from sklearn.metrics import classification_report
print('report DT : ', classification_report(y_test,y_pred_dt))

df.Churn.value_counts()/len(df)*100
# Churn
# No     73.421502
# Yes    26.578498
# with a simple python script also we will get the same accuracy.
