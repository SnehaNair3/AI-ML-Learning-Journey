
from keras.applications import VGG16
from tensorflow.keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input,decode_predictions

import numpy as np


# Load the VGG16 pre-trained models and specify the input shape
model=VGG16(weights='imagenet',include_top=True,input_shape=(224,224,3))


 # Loading an image and preprocess it for the model

img_path='pexels-morningtrain-18105.jpg'
img=image.load_img(img_path,target_size=(224,224))
x=image.img_to_array(img)
x=np.expand_dims(x,axis=0)
x=preprocess_input(x)


# Use the model to predict the class
pred=model.predict(x)

print(pred)


# Get the top 5 predictions with class names
decode_preds=decode_predictions(pred,top=5)[0]

# top 5 class predictions
for pred in decode_preds:
    print(pred[1], ": ",pred[2])



