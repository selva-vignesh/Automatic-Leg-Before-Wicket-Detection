import cv2
import numpy as np

def vidSegment(vid,crop):
        
        count = 0  # to find no.of frames
        while True: 
            flag, image = vid.read() 
            print("Flag", flag)
            if(flag == 0):
                break
                
            #Cropping
            image = image[crop[0]:crop[1], crop[2]:crop[3]]
            
            cv2.imwrite("/home/qubercomm/Project/Frames/frame" +str(count)+".jpg", image) 
            count += 1
            
        vid.release()
        return count
