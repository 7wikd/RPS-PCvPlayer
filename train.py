import cv2
import numpy as np
from keras_squeezenet import Squeezenet  
from keras.optimizers import Adam
from keras.utils import np_utils

from keras.layers import Activation,Dropout,Convolution2D,MaxPooling2D
from keras.models import Sequential
import tensorflow as tf

import os

IMG_PATH = 'images'

CLASS_MAP = {
   "none":0,
   "rock":1,
   "paper":2,
   "scissors":3 
}

NUM_CLASSES = len(CLASS_MAP)

def mapping(val):
    return CLASS_MAP[val]


model = Sequential([
    Squeezenet(input_shape=(227,227,3),include_top=False),
    Dropout(0.2),
    Convolution2D(NUM_CLASSES,(1,1),padding='valid'),
    Activation('relu'),
    MaxPooling2D(),
    Activation('softmax')
])


dataset = []
for dir in os.listdir(IMG_PATH):
    path = os.path.join(IMG_PATH,dir)
    if not os.path.isdir(path):
        continue
    for item in os.listdir(path):
        if item.startswith("."):
            continue
        img = cv2.imread(os.path.join(path,item))
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = cv2.resize(img,(227,227))
        dataset.append([img,dir])


data,labels = zip(*dataset)
labels = list(map(mapping,labels))

labels = np_utils.to_categorical(labels)

model.compile(
    optimizer=Adam(lr=0.001),
    loss = 'categorical_crossentropy',
    metrics = ['accuracy']
)

model.fit(np.array(data),np.array(labels),epochs = 10)

model.save("RPS-model.h5")
