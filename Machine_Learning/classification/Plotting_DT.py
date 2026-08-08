

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

df.head()

# TotalCharges is a numerical attribute, but it is shown as object - so convert to numeric
df.TotalCharges=pd.to_numeric(df.TotalCharges,errors='coerce')

df.info()

# Now 11 null values found in TotalCharges
# since its less than 1 % (11/7043), drop those null values
df.dropna(how='any',inplace=True)


df.Churn.value_counts()
df.Churn.value_counts()/len(df)*100

X=df.drop(['customerID','Churn'],axis=1)
y=df.Churn.values

X.columns


# Feature Encoding - Dummy encoding
# Converting categorical variable to numerical
X=pd.get_dummies(X,columns=['gender', 'Partner', 'Dependents',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod'],drop_first=True)


X.head(1)


# Splitting data into training and testing
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



# Decision Tree cLassifier
from sklearn.tree import DecisionTreeClassifier

model_dt=DecisionTreeClassifier()

model_dt.fit(X_train_sc,y_train)

y_pred_dt=model_dt.predict(X_test_sc)


# Classification metrics
from sklearn.metrics import accuracy_score

print(accuracy_score(y_test,y_pred_dt)*100)



# Visualizing the Decision Tree
from sklearn.tree import plot_tree

plt.figure(figsize=(10,8))
plot_tree(model_dt,filled=True,feature_names=X_train.columns,class_names=True)
plt.show()
# here max_depth attribute is None (default).



# other ways to visualize DT
# graphviz
# dtreeviz


# 2 - max_depth=2

model_dt2=DecisionTreeClassifier(max_depth=2)

model_dt2.fit(X_train_sc,y_train)

y_pred_dt2=model_dt2.predict(X_test_sc)


# Classification metrics
from sklearn.metrics import accuracy_score

print(accuracy_score(y_test,y_pred_dt2)*100)



# Visualizing the Decision Tree
from sklearn.tree import plot_tree

plt.figure(figsize=(10,8))
plot_tree(model_dt2,filled=True,feature_names=X_train.columns,class_names=True)
plt.show()


# graphiz
from sklearn.tree import export_graphviz
import graphviz


export_graphviz(model_dt2,out_file="tree.dot",feature_names=X_train.columns,class_names=True,filled=True,proportion=True,special_characters=True)

with open("tree.dot") as f:
    dot_graph=f.read()
graph=graphviz.Source(dot_graph,format='png')
graph    