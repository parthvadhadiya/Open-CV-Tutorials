import cv2
import numpy as np
import os
import math
from matplotlib import pyplot as plt
#%matplotlib inline

#print(cv2.__version__)

webcam = cv2.VideoCapture(0)

cv2.namedWindow("example", cv2.WINDOW_NORMAL)
 
while True:
      
    _, frame = webcam.read()
    cv2.imshow("example", frame) 
     
    # code 27 is ESC key
    if cv2.waitKey(20) & 0xFF == 27:
        break

        
cv2.destroyAllWindows() 
webcam.release()


#------ this code for capture videos

'''
webcam = cv2.VideoCapture(0)
cv2.namedWindow("PyData Tutorial", cv2.WINDOW_AUTOSIZE)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('videos/video_rod.avi',fourcc, 20.0, (640,480))

while webcam.isOpened():
    ret, frame = webcam.read()
    video.write(frame)
    # write/append to video object
    cv2.imshow('PyData Tutorial',frame)
    if cv2.waitKey(40) & 0xFF == 27:
        break
# release both video objects created
webcam.release()
video.release()
cv2.destroyAllWindows()
os.system("vlc videos/video_rod.avi")

'''

#------make rectangle
'''
webcam = cv2.VideoCapture(0)
cv2.namedWindow("PyData Tutorial", cv2.WINDOW_AUTOSIZE)
message = ""

while webcam.isOpened():
    
    _, frame = webcam.read()
    
    cv2.rectangle(frame, (100, 100), (530, 400), (150, 150, 0), 3)
    cv2.putText(frame, message, (95, 95), cv2.FONT_HERSHEY_SIMPLEX, .7, 
                (150, 150, 0), 2)
    
    cv2.imshow('PyData Tutorial',frame)
    key = cv2.waitKey(100) & 0xFF
    if key not in [255, 27]:
        message += chr(key)
    elif key == 27:
        break
        
# release both video objects created
webcam.release()
cv2.destroyAllWindows()


'''
#--circle

'''
webcam = cv2.VideoCapture(0)
cv2.namedWindow("PyData Tutorial", cv2.WINDOW_AUTOSIZE)

while webcam.isOpened():
    
    _, frame = webcam.read()
    mask = np.zeros_like(frame)
    height, width, _ = frame.shape
    
    cv2.circle(mask, (width / 2, height / 2), 200, (255, 255, 255), -1)
    frame = np.bitwise_and(frame, mask)
    
    cv2.imshow('PyData Tutorial', frame)
    if cv2.waitKey(40) & 0xFF == 27:
        break
        
# release both video objects created
webcam.release()
cv2.destroyAllWindows()
'''
