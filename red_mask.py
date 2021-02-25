#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

def empty(a):
    pass

cap = cv2.VideoCapture(0)
w, h = 720, 480

count = 0

while True:
    success, image = cap.read()
    if not success:
        break

    result = image.copy()
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    low_red = np.array([162, 155,84])
    high_red = np.array([179, 255, 255])
    
    mask = cv2.inRange(image, low_red, high_red)
    result = cv2.bitwise_and(result,result,mask=mask)

    cv2.imshow('mask',mask)
    cv2.imshow('result',result)

    print(type(mask))
    #mask is 720 x 1280
    if (count >= 30):
        count = 0
        
    count += 1
    cv2.waitKey(200)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break


# In[ ]:




