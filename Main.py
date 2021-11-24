import cv2
import numpy as np 
from tkinter import *

# Other modules imported
import FrameSeg as fs
import BallDetection as bd
import PadDetection as pd
import DecisionMaking as dm


top = Tk()   
top.geometry("150x100") 

path = '/home/qubercomm/Project/video.mp4'  # path to the video file

#Input Video
vid = cv2.VideoCapture(path)

#Frame Segmentation
crop = [450,600,670,800] 
frame_count = fs.vidSegment(vid,crop)

# Color boundaries
boundVal = ([0, 0, 10], [100, 100, 255])

# Max and Min Radius of the Ball
min_rad, max_rad = [7,14] 

#Ball and Pad detection
flag = 0 
for j in range(frame_count):    # Loop over the frames

    txt = "/home/qubercomm/Project/Frames/frame"+str(j)+".jpg" # path to the extracted frames.

    img = cv2.imread(txt.format(val = j),cv2.IMREAD_COLOR)

    # Ball Detection
    ball = bd.ballDetect(img, min_rad, max_rad)

    #Pad Detection
    pad = pd.padDetect(img, boundVal)

    #Decision Making
    flag, intersected = dm.isIntersect(ball, pad)

    output = np.hstack([ball, pad])
    cv2.imshow("Decision Making",output)
    cv2.imshow("Making",intersected)
    cv2.waitKey(0) 

    if (flag):
        decision = Label(top,text = "Out!",font=("Helvetica", 22)).place(x=10,y =10)
        break
        

if(flag==0):
    decision = Label(top,text = "Not Out!",font=("Helvetica", 22)).place(x=10,y =10)
    
top.mainloop()