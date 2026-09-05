
import tensorflow as tf
from tensorflow import keras
from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten

# Dropout Regularization : To get rid of overfitting problem
from keras.layers import Conv2D,MaxPooling2D
from keras import backend as K


# Number of classes - do not change unless the data changes
num_classes=10


# sizes of batch and # of epochs of data
batch_size=64
epochs=24

# input image dimensions
img_rows,img_cols=28,28


# the data , shuffled and spllit between train and test sets
(x_train,y_train), (x_test,y_test) = fashion_mnist.load_data()

x_train.shape
x_test.shape

len(y_train)

print(y_train)


x_train.shape[0]


x_train=x_train.reshape(x_train.shape[0],img_rows,img_cols,1)
x_test=x_test.reshape(x_test.shape[0],img_rows,img_cols,1)
input_shape=(img_rows,img_cols,1)

input_shape

x_train.shape


# Type convert and scale the test and training data
x_train=x_train.astype('float32')
x_test=x_test.astype('float32')
x_train/=255.
x_test/=255.
print('x_train shape : ',x_train.shape)
print('x_test shape : ',x_test.shape)
print(y_train[0:3])



# Convert class vectors to binary class matrices . One-hot encoding
# 3 --> 0 0 0 1 0 0 0 0 0 0  and 1 --> 0 1 0 0 0 0 0 0 0 0
y_train=tf.keras.utils.to_categorical(y_train,num_classes)
y_test=tf.keras.utils.to_categorical(y_test,num_classes)
print(y_train[0:2])


# CNN CODE BEGINS

# Define the model
model=Sequential()

num_classes


# Create a CNN to classify the images
model.add(Conv2D(32,kernel_size=(3,3),
                 activation='relu',
                 input_shape=input_shape))  # feature  detector

model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(32,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))



# define compile to minimize categorical loss, use ada delta optimized, and optimize to maximizing  accuracy
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])


# Train the model and test/validate the model with the test data after each cycle (epoch) through the training data
# return history of loss and accuracy  for each epoch
hist=model.fit(x_train,y_train,
               batch_size=batch_size,
               epochs=epochs,
               verbose=1,
               validation_data=(x_test,y_test))


hist.history


# Evaluate the model with the test data to get the scores on "real data"
score=model.evaluate(x_test,y_test,verbose=0)
print('Tets loss : ',score[0])
print('Test accuracy : ',score[1])


# Plot data to see relationships in tarining and validation data
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

epoch_list=list(range(1,len(hist.history['accuracy'])+1))  # values for x-axis [1,2,....]
plt.plot(epoch_list,hist.history['accuracy'],epoch_list,hist.history['val_accuracy'])
plt.legend('Training accuarcy','Validation Accuracy')
plt.show()


# model summary
model.summary()