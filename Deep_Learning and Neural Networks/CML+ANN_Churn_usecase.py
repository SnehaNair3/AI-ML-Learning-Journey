
# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Importing the dataset
dataset=pd.read_csv('Churn_Modelling.csv')

X=dataset.iloc[:,3:13].values
y=dataset.iloc[:,13].values

dataset.head(5)


# Encoding categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

labelencoder_X_1=LabelEncoder()
X[:,1]=labelencoder_X_1.fit_transform(X[:,1])
labelencoder_X_2=LabelEncoder()
X[:,2]=labelencoder_X_2.fit_transform(X[:,2])


# Splitting the dataset ito the Training set and Test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

len(dataset)

len(X_train)


# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)


# Classical ML
from sklearn.tree import DecisionTreeClassifier

clf=DecisionTreeClassifier()
clf.fit(X_train,y_train)
pred=clf.predict(X_test)


# Making the confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,pred)
print(cm)

# Accuracy score
from sklearn.metrics import accuracy_score
score=accuracy_score(y_test,pred)
print(score*100)



# Classical ML- Random Forest

from sklearn.ensemble import RandomForestClassifier
clf2=RandomForestClassifier(n_estimators=200)
clf2.fit(X_train,y_train)
pred2=clf2.predict(X_test)

# Making the confusion matrix
from sklearn.metrics import confusion_matrix
cm2=confusion_matrix(y_test,pred2)
print(cm2)

# Accuracy score
from sklearn.metrics import accuracy_score
score2=accuracy_score(y_test,pred2)
print(score2*100)



# ANN

# Importing the keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense


# Initialising the ANN

# Sequential is basically a classifier present inside the keras models. 
# It si used for classification as well as regression.
classifier=Sequential()


# units - Its an art, comes by experience , input+output/2
# initializer -  how your weights are updated.
# relu activation function
# input_dim - input shape  (shape of the data, how many features do we have in the data)

# Adding the input layer and the first hidden layer
classifier.add(Dense(units=6, kernel_initializer='uniform',activation='relu',input_dim=10))

# Adding the second hidden layer
classifier.add(Dense(units=6, kernel_initializer='uniform',activation='relu'))

# Adding the third hidden layer
classifier.add(Dense(units=6, kernel_initializer='uniform',activation='relu'))

# Adding the output layer
classifier.add(Dense(units=1, kernel_initializer='uniform',activation='sigmoid'))

# If you're doing a binary classification , output layer should have sigmoid activation layer
# Else it should have a softmax output layer.

len(X_train)


# Compiling the ANN
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
y_train[0]

# Fitting the ANN to the training set
classifier.fit(X_train,y_train,batch_size=10,epochs=50)

# optimizer means how optimized the neural network is gonna be
# how are we gonna perform the back propagation,forward propagation, how handle weights while back propagation
# all these things are present inside the optimizer.
# optimizer - is a hyperparameter


# Loss function - is binary cross entropy because this is a binary classification problem.
# if its binary classification problem, use categorical cross entropy or sparsee_categorical_cross_entropy

# Epoch is again a hyperparameter


# Making predictions and evaluating the model
# predicting the test results
y_pred_ann=classifier.predict(X_test)
y_pred_ann=(y_pred_ann > 0.5)


cm3=confusion_matrix(y_test,y_pred_ann)
print(cm3)

from sklearn.metrics import accuracy_score

score3=accuracy_score(y_test,y_pred_ann)
print(score3*100)









