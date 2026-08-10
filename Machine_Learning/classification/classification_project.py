
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
# Accuracy DT :  71.84300341296928

from sklearn.metrics import classification_report
print('report DT : ', classification_report(y_test,y_pred_dt))

df.Churn.value_counts()/len(df)*100
# Churn
# No     73.421502
# Yes    26.578498
# with a simple python script also we will get the same accuracy.



from imblearn.over_sampling import RandomOverSampler

# Upsample the minority class using RandomOverSampler
oversampler=RandomOverSampler()
X_train_upsampled,y_train_upsampled=oversampler.fit_resample(X_train_sc,y_train)


# Model Building
model_dt2=DecisionTreeClassifier()
model_dt2.fit(X_train_upsampled,y_train_upsampled)

# Predict on the test set
y_pred_dt2=model_dt2.predict(X_test_sc)

# Calculate accuracy
print('Accuarcy DT2 : ',accuracy_score(y_test,y_pred_dt2)*100)
# Accuarcy DT2 :  73.32195676905575


from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred_dt2))

#  SMOTEENN
from sklearn.tree import DecisionTreeClassifier
from imblearn.combine import SMOTEENN
from sklearn.metrics import accuracy_score,classification_report

# Create a SMOTENN object
smote_enn=SMOTEENN(random_state=42)


# Resample the data
X_train_resampled,y_train_resampled=smote_enn.fit_resample(X_train_sc,y_train)


# Model Building
model_dt3=DecisionTreeClassifier()
model_dt3.fit(X_train_resampled,y_train_resampled)


# Prediction on the test set
y_pred_dt3=model_dt3.predict(X_test_sc)

# Calculate accuracy
print('Accuarcy DT3 : ',accuracy_score(y_test,y_pred_dt3)*100)
# Accuarcy DT3 :  72.07053469852104


# SMOTE
from imblearn.over_sampling import SMOTE

# Create a SMOTE object
smote=SMOTE(random_state=42)

# Resample the data
X_train_resampled,y_train_resampled=smote.fit_resample(X_train_sc,y_train)

# model Building
model_dt4=DecisionTreeClassifier()
model_dt4.fit(X_train_resampled,y_train_resampled)

# Predict on the test data
y_pred_dt4=model_dt4.predict(X_test_sc)

# Calculate accuracy
print('Accuarcy DT4 : ',accuracy_score(y_test,y_pred_dt4)*100)
# Accuarcy DT4 :  73.03754266211604

# Print classification report 
print(classification_report(y_test,y_pred_dt4))


# ADASYN
from imblearn.over_sampling import ADASYN

# Create a ADASYN object
adasyn=ADASYN()

# Resample the data
X_train_resampled,y_train_resampled=adasyn.fit_resample(X_train_sc,y_train)


# Build model
model_dt5=DecisionTreeClassifier()
model_dt5.fit(X_train_resampled,y_train_resampled)

# Predict
y_pred_dt5=model_dt5.predict(X_test_sc)

# accuracy
print('Accuracy dt5 : ', accuracy_score(y_test,y_pred_dt5)*100)
# Accuracy dt5 :  72.5824800910125

print(classification_report(y_test,y_pred_dt5))



# AllKNN
from imblearn.under_sampling import AllKNN


# Assume df is your dataframe containing the dataset.


# Seperate features and target variable
X=df.drop(['customerID','Churn'],axis=1)
y=df["Churn"]

X=pd.get_dummies(X,columns=['gender', 'Partner', 'Dependents',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod'],drop_first=True)


# Split adta into train test
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42,stratify=y)
# stratified split for imbalanced

# Check for class imbalance in training data
print("Class imbalance in training data : ")
print(y_train.value_counts())


# Use AllKNN for undersampling
allknn=AllKNN(sampling_strategy='auto')
X_train_resampled,y_train_resampled=allknn.fit_resample(X_train,y_train)


# Standardize the data
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train_resampled)
X_test_scaled=scaler.transform(X_test)


# Create a decision tree classifier with appropriate parameters
print("Training decision tree..")
dtc=DecisionTreeClassifier(random_state=42,max_depth=5)
dtc.fit(X_train_scaled,y_train_resampled)


# Make predictions on test data
y_pred_dtc=dtc.predict(X_test_scaled)

# Evaluate accuarcy
print('Accuarcy DTC : ', accuracy_score(y_test,y_pred_dtc)*100)
# Accuarcy DTC :  73.54948805460751






# TomekLinks
from imblearn.under_sampling import TomekLinks
from sklearn.model_selection import GridSearchCV


# Assume df is your dataframe containing the dataset.


# Seperate features and target variable
X=df.drop(['customerID','Churn'],axis=1)
y=df["Churn"]

X=pd.get_dummies(X,columns=['gender', 'Partner', 'Dependents',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod'],drop_first=True)


# Split data into train test
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42,stratify=y)
# stratified split for imbalanced

# Check for class imbalance in training data
print("Class imbalance in training data : ")
print(y_train.value_counts())


# Use TomekLinks for undersampling
tomek=TomekLinks(sampling_strategy='majority')  # not majority gives better results
X_train_resampled,y_train_resampled=tomek.fit_resample(X_train,y_train)


# Standardize the data
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train_resampled)
X_test_scaled=scaler.transform(X_test)


# Create a decision tree classifier with appropriate parameters
print("Training decision tree..")
dtc=DecisionTreeClassifier(random_state=42,max_depth=5)

# Define the paramtere grid for finetuning
param_grid={
    'max_depth' : [3,5,7,None],
    'min_samples_split' : [2,5,10],
    'min_samples_leaf' : [1,2,4]
}

# Use GridSearchCV for fine-tuning
grid_search=GridSearchCV(dtc,param_grid,cv=5,scoring='accuracy',n_jobs=1)
grid_search.fit(X_train_scaled,y_train_resampled)

# Get the  best parameters from the grid search
best_params=grid_search.best_params_

# Print the best parameters
print("Best Parametres : ",best_params)

# Create a decision tree classfier with the best paramters
dtc_best=DecisionTreeClassifier(random_state=42,**best_params)
dtc_best.fit(X_train_scaled,y_train_resampled)


# Make predictions on test data
y_pred_dtc_best=dtc_best.predict(X_test_scaled)

# Evaluate accuarcy
print('Accuarcy DTC Best : ', accuracy_score(y_test,y_pred_dtc_best)*100)
# Accuarcy DTC Best :  78.32764505119454

print(classification_report(y_test,y_pred_dtc_best))