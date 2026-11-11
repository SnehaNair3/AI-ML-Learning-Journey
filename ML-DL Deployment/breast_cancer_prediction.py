import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

dataset_url="https://github.com/apogiatzis/breast-cancer-azure-ml-notebook/raw/refs/heads/master/breast-cancer-data.csv"
df=pd.read_csv(dataset_url)

df.head(5)

# label encoding
df['diagnosis']=df['diagnosis'].map({'M':1,'B':0})
df.diagnosis.value_counts()

features=['radius_mean','texture_mean','perimeter_mean','smoothness_mean','compactness_mean']
X=df[features]
y=df.diagnosis

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
len(X_train)
len(X_test)


# Model Building
model=RandomForestClassifier(n_estimators=00,n_jobs=-1)
model.fit(X_train,y_train)


prediction=model.predict(X_test)

print('Accuracy is : ',round(accuracy_score(prediction,y_test))*100, '%')


# prediction on a random data point 
data=[[1,2,3,4,5]]

new_df=pd.DataFrame(data, columns=['radius_mean','texture_mean','perimeter_mean','smoothness_mean','compactness_mean'])

single=model.predict(new_df)
print(single)

proba=model.predict_proba(new_df)[:,1]
print(proba)

if single ==1:
    output="The patient is diagnosed with Breast Cancer."
    output1="Confidence: {}".format(proba*100)
else:
    output="The patient is not diagnosed with Breast Cancer."  
    output1=""  
print(output + output1)









