import cv2
import os

# Opening the camera code from https://subscription.packtpub.com/book/application_development/9781785283932/3/ch03lvl1sec28/accessing-the-webcam
# Likely modify this? https://docs.opencv.org/master/db/d28/tutorial_cascade_classifier.html
# May be a worthwhile read for object detection with deep learning (specifically the dnn module):
    # https://www.pyimagesearch.com/2017/09/11/object-detection-with-deep-learning-and-opencv/

cap = cv2.VideoCapture(0)
path = "\webcam-images"
# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    # frame is a 3d numpy array. When you run imwrite() to save the frame, you are able to return an image.
    # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    frame = cv2.flip(frame, 1)
    cv2.imshow('Input', frame)

    # Add a function here that takes in an input of whatever "frame" is 

    c = cv2.waitKey(1)

    # If the user presses "esc", close the video window.
    if c == 27:
        cv2.imwrite("./images/frame%d.jpg" % 2, frame)     # Code for saving the frame when you press esc, saves to the current direction you are in
        print(frame)
        print(type(frame))
        break

cap.release()
cv2.destroyAllWindows()

print("Hello world")