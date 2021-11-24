import cv2
import numpy as np

def isIntersect(ball,pad):
    	

	# Color range of bounding circle.
	boundaries = [
		([0,110, 0], [140,255,165])
				]

	for (lower, upper) in boundaries:
		
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")

		# Limiting pixels based on color values.
		mask = cv2.inRange(ball, lower, upper)
		output = cv2.bitwise_and(ball, ball, mask = mask)
		blurred = cv2.medianBlur(output,1)
		
		ret,thresh_ball = cv2.threshold(blurred,10,255,cv2.THRESH_BINARY)
		
		# AND operation pixel wise.
		intersect_mask = cv2.bitwise_and(thresh_ball, pad, mask = mask)
		img = np.hstack([ball,pad, intersect_mask])
		
		gray = cv2.cvtColor(intersect_mask, cv2.COLOR_BGR2GRAY)
		ret, final_mask = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)

		s = list(gray.shape)
		count=0

		for i in range(s[0]):
				for j in range(s[1]):
						if(final_mask[i][j] >= 220):
								count = count+1
		if(count>=4):
				return [1, final_mask]
		else:
    			return [0,final_mask]
				
		
		
	