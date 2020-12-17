from keras.models import load_model
import cv2
import numpy as np
import sys

fpath = sys.argv[1]

CLASS_MAP={
    0: "none",
    1: "rock",
    2: "paper",
    3: "scissors"
}

def mapping(val):
    return CLASS_MAP[val]

model = load_model()

img = cv2.imread(fpath)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img = cv2.resize(img,(227,227))

pred = model.predict((np.array(img)))
move = np.argmax(pred[0])
name = mapping(move)

print("Predicted: {}".format(name))