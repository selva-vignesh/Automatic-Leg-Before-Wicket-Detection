import cv2
import numpy as np

def ballDetect(img, min_rad, max_rad):

        """ This function detects the ball in the given image.
        Input:
             src     - Image/frame for ball detection.
             min_rad - Minimum radius of the ball (interms of pixel).
             max_rad - Maximum radius of the ball (interms of pixel).
        Returns:
             The image enclosing the detected ball by a green bounding circle. """


        # Converting the (BGR) Image to Grayscale image.
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Median Blur with 7 X 7 mask.
        blur = cv2.medianBlur(img_gray,7)

        # Applying thresholding
        ret,thresh = cv2.threshold(blur, 180, 255, cv2.THRESH_BINARY) 
        
        threshold = 250 # initial threshold
        # Canny Edge Detection
        canny_output = cv2.Canny(thresh, threshold, 255)
        
        # Applying Contours
        contours,_ = cv2.findContours(canny_output, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                        
                        
        contours_poly = [None]*len(contours)
        boundRect = [None]*len(contours)
        centers = [None]*len(contours)
        radius = [None]*len(contours)

        # Iterate through the contours and applying Mininum Enclosing circle.
        for i, c in enumerate(contours):
                contours_poly[i] = cv2.approxPolyDP(c, 1, True)
                centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])
                                      
        drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
                        
                        
        for i in range(len(contours)):
                color = (0,255,0)  # Color of bounding circle.
                if ((radius[i]>=min_rad) & (radius[i]<=max_rad)):
                        # Drawing bounding circle  
                        cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)
                                     
        added_image = cv2.addWeighted(img,0.4,drawing,1,0)
        return added_image 
        