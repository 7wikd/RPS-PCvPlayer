desc = "script to gather images:\ncommand: python3 images.py <name> <number>"

import os
import cv2
import sys

try:
    label_name = sys.argv[1]
    samples = int(sys.argv[2])
except:
    print("Arguments missing...")
    print(desc)
    exit(-1)

IMG_PATH = 'images/'
IMG_CLASS = os.path.join(IMG_PATH,label_name)

try:
    os.mkdir(IMG_PATH)
except FileExistsError:
    pass

try:
    os.mkdir(IMG_CLASS)
except FileExistsError:
    print("{} already exists".format(IMG_CLASS))
    print("Images stored in this folder")

cap = cv2.VideoCapture(-1)

start = False
count = 0

while True:
    #### Get images ####
    ret, frame = cap.read()

    if not ret:
        continue
    if count == samples:
        break
    #### OVER ####
    cv2.rectangle(frame,(100,100),(500,500),(255,255,255),2)

    if start:
        roi = frame[100:500,100:500]
        path = os.path.join(IMG_CLASS,"{}.jpg".format(count))
        cv2.imwrite(path,roi)
        count += 1

    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(
        frame, 
        "Collecting images{}".format(count),
        (5,50),font,0.7,(0,255,255),2,
        cv2.LINE_AA
    )
    cv2.imshow("Collecting images",frame)

    k = cv2.waitKey(10)
    if k == ord("a"):
        start = not start
    if k == ord("q"):
        break

print("{} images saved in {}".format(count+1,IMG_CLASS))

cap.release()
cv2.destroyAllWindows()