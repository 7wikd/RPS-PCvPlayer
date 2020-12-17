from keras.models import load_model

import cv2
import numpy as np
from random import random

CLASS_MAP={
    0: "none",
    1: "rock",
    2: "paper",
    3: "scissors"
}

def mapping(val):
    return CLASS_MAP[val]

def calc_win(move1,move2):
    if move1 == move2:
        return "Tie"

    if move1 == "rock":
        if move2 == "scissors":
            return "User"
        if move2 == "paper":
            return "Computer"

    if move1 == "paper":
        if move2 == "rock":
            return "User"
        if move2 == "scissors":
            return "Computer"

    if move1 == "scissors":
        if move2 == "paper":
            return "User"
        if move2 == "rock":
            return "Computer"

model = load_model()

cap = cv2.VideoCapture(0)

prev_move = None

while True:
    ret,frame = cap.read()
    if not ret:
        continue
    cv2.rectangle(frame,(100,100),(500,500),(255,255,255),2)
    