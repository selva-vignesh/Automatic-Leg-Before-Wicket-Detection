import cv2 
import numpy as np

def padDetect(image, boundVal):


	boundaries = [ boundVal ]

	for (lower, upper) in boundaries:
		
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")

		# Limiting pixels based on color values.
		mask = cv2.inRange(image, lower, upper)
		mask = cv2.bitwise_and(image, image, mask = mask)
		blurred = cv2.medianBlur(mask,11)
		
		ret,thresh = cv2.threshold(blurred,100,255,cv2.THRESH_BINARY)
		
		return thresh