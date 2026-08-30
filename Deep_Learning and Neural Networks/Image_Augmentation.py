
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
from skimage import exposure
from skimage.util import random_noise
from skimage import transform
from cv2 import resize



import skimage
print(skimage.__version__)


img=mpimg.imread('barbie.png')

plt.imshow(img)

# Image Augmentation 

# RESCALING

img_rescale=resize(img, (150,150))
plt.imshow(img_rescale)

img_rescale=resize(img, (50,50))
plt.imshow(img_rescale)


# FLIPPING
horizontal_flip=np.fliplr(img)
plt.imshow(horizontal_flip)

vertical_flip=np.flipud(img)
plt.imshow(vertical_flip)


# ROTATION
from skimage import transform
trans_img=transform.rotate(img,random.uniform(-40,40))  # degrees
plt.imshow(trans_img)


# ADDING NOISE
img_noise=random_noise(img, mode='s&p',clip=True)
plt.imshow(img_noise)
