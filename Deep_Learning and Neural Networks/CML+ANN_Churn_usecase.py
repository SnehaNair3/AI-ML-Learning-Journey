
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



# K-Fold Cross Validation
# Importing few libraries for k-folds
from scikeras.wrappers import KerasClassifier
from sklearn.model_selection import cross_val_score
from keras.models import Sequential
from keras.layers import Dense


def build_classifier():
    classifier=Sequential()
    classifier.add(Dense(units=6, kernel_initializer='uniform',activation='relu',input_dim=10))
    classifier.add(Dense(units=6, kernel_initializer='uniform',activation='relu'))
    classifier.add(Dense(units=1, kernel_initializer='uniform',activation='sigmoid'))
    classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
    return classifier


classifier=KerasClassifier(build_fn=build_classifier, batch_size=10,epochs=10)

accuracies=cross_val_score(estimator=classifier,X=X_train,y=y_train,cv=10,n_jobs=-1)
mean1=accuracies.mean()
variance=accuracies.std()


# Improvising the ANN - Hyperparanetr optimization

from scikeras.wrappers import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense


def build_classifier():
    classifier=Sequential()
    classifier.add(Dense(units=6, kernel_initializer='uniform',activation='relu',input_dim=10))
    classifier.add(Dense(units=6, kernel_initializer='uniform',activation='relu'))
    classifier.add(Dense(units=1, kernel_initializer='uniform',activation='sigmoid'))
    classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
    return classifier


classifier=KerasClassifier(build_fn=build_classifier)

parameters={'batch_size':[10,20],
            'epochs':[5,6]}

      # Total Combinations = 4 

grid_search=GridSearchCV(estimator=classifier,param_grid=parameters,scoring='accuracy',n_jobs=-1,cv=5)
grid_search=grid_search.fit(X_train,y_train)
grid_search.best_params_
grid_search.best_score_



# Improvising the ANN - Hyperparanetr optimization --> adding more hyperparameters

from scikeras.wrappers import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense


def build_classifier():
    classifier=Sequential()
    classifier.add(Dense(units=6, kernel_initializer='uniform',activation='relu',input_dim=10))
    classifier.add(Dense(units=6, kernel_initializer='uniform',activation='relu'))
    classifier.add(Dense(units=6, kernel_initializer='uniform',activation='relu'))
    classifier.add(Dense(units=6, kernel_initializer='uniform',activation='relu'))
    classifier.add(Dense(units=1, kernel_initializer='uniform',activation='sigmoid'))
    classifier.compile(optimizer=optimizer,loss=loss, metrics=['accuracy'])
    return classifier


classifier=KerasClassifier(build_fn=build_classifier)

parameters={'batch_size':[10,20,30,50],
            'epochs':[10,50,100,200],
            'loss' : ['binary_crossentropy','categorical_crossentropy'],
            'optimizer' : ['adam','rmsprop']}

      # Total Combinations = 4*4*2*2

grid_search=GridSearchCV(estimator=classifier,param_grid=parameters,scoring='accuracy',n_jobs=-1,cv=5)
grid_search=grid_search.fit(X_train,y_train)
grid_search.best_params_
grid_search.best_score_




# Improvising the performance of ANN
# 1 - INcrease the number of hidden layers
# 2 - Increase the number of epochs
# 3 - Fine-tuning the parameters - optimizers, batch_size,epochs
# 4 - Dropout regularization : Dropout(0.25)
# Dropout is implemented after each and every hidden layer
# It basically means you are dropping out some of the features
# 0.25 --> means you're dropping out 25% of the features


# Overfitting problem : training accuracy increases, test accuracy is low










import tensorflow as tf
import keras

print(tf.__version__)
print(keras.__version__)