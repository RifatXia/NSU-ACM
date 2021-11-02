# Detect circles in a image using built in functions in Python(OpenCV and Hough circle)
# Made by following the Youtube tutorial : https://www.youtube.com/watch?v=dp1r9oT_h9k&ab_channel=ProgrammingKnowledge
# RifatXia

import numpy as np
import cv2 as cv

# store the image 
img = cv.imread("NSU ACM R&D\\Shape Detection using OpenCV\\circles-2.png")

# copy the image 
output = img.copy()

# converting the image to grayscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)

# built in function to detect the circles with the parameters 
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

# storing the detected circles in a numpy and convert them to an integer   
detected_circles = np.uint16(np.around(circles))

# drawing outline around the circle in the image
for (x, y, r) in detected_circles[0, :]:
    cv.circle(output, (x, y), r, (0, 0, 255), 2)

# displaying the output 
cv.imshow('output', output)
cv.waitKey(0)
cv.destroyAllWindows()
