import cv2
import numpy as np
import os
import math
from matplotlib import pyplot as plt
#%matplotlib inline

#print(cv2.__version__)

webcam = cv2.VideoCapture(0)
ret, frame = webcam.read()
print(ret)
webcam.release()



#frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#cv2.imwrite("image/mypic_BGR1.jpg",frame)
#cv2.imwrite("image/mypic_RGB1.jpg",frame_RGB)

#os.system("nautilus images")
