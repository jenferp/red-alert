import cv2

# Opening the camera code from https://subscription.packtpub.com/book/application_development/9781785283932/3/ch03lvl1sec28/accessing-the-webcam
# Likely modify this? https://docs.opencv.org/master/db/d28/tutorial_cascade_classifier.html

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    # If the user presses "esc", close the video window.
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()