# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import os

# define a helper function to detected face
def detect_and_predict_blood(frame, bloodNet, check):
    # This function takes in an input of the frame, the model, and a "check" variable for debugging purposes
    # You can remove this check parameter without breaking the code, it was for helping me discover what each variable was easily

    detection_list = []
    preds = []

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (224, 224))
    frame = img_to_array(frame)
    frame = preprocess_input(frame)

    detection_list.append(frame)

    if check == True:
        print("detection_list before turning into np.array:")
        #print(type(detection_list))
        #print(detection_list)
    # Create a numpy array to apply the model, in case that we have multiple things (subject to change depending on if we change the input)
    detection_list = np.array(detection_list, dtype="float32")
    preds = bloodNet.predict(detection_list, batch_size=32) # DV: bloodNet should be our model to detect blood in a frame
        
    # Return an array on whether there is blood or no blood in the frame:
    # Example: array([[0.00736171 0.99263835]], dtype="float32"). When you access this value, you'll get [[0.00736171 0.99263835]]
    return preds

# Load the blood detector model from disk
bloodNet = load_model('./blood_noblood_classifier.model') # DV: Change the path to our model

# Initialize the video stream and allow the camera sensor to warm up
vs = VideoStream(src=0).start()
time.sleep(2.0)

# Loop over the frames from the video stream
while True:
    
    # Grab the frame from the threaded video stream and resize it to have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    
    # Run the prediction on blood on the entire frame
    preds = detect_and_predict_blood(frame, bloodNet, False)

    # Obtain the prediction. preds is an array right now that looks like, for example: [[0.00736171 0.99263835]]
    # So we have to create a tuple from the values inside
    (blood, noblood) = (preds[0][0], preds[0][1])
    
    # Assign a label on whether blood is detected on the screen and assign a color
    label = "Blood" if blood > noblood else "No Blood"
    color = (0, 0, 255) if label == "Blood" else (0, 255, 0)
    
    # Include the probability in the label
    label = "{}: {:.2f}%".format(label, max(blood, noblood) * 100)
    
    # Display the label on the frame
    cv2.putText(frame, label, (20, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)

    # Show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    # If the q is pressed, break from the loop
    if key == ord("q"):
        # DV: Check the last frame
        # Debug/discovery stuff
        # print("Q was pressed")
        # preds = detect_and_predict_blood(frame, bloodNet, True)
        # print("Print preds")
        # print(preds)
        # (blood, noblood) = (preds[0][0], preds[0][1])
        # print("The blood no blood tuple")
        # print((blood, noblood))
        # if blood > noblood:
        #     print("Blood detected")
        # else:
        #     print("No blood detected")

        break
        
# Do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()