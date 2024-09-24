import cv2
import numpy as np

bg = cv2.imread("Lesson 9/bg.jpg")
delegate = cv2.imread("Lesson 9/spongebob.jpg")

HSV = cv2.cvtColor(delegate, cv2.COLOR_BGR2HSV)
cv2.imshow("display", HSV)


lowerrange = np.array([45,50,50])
upperrange = np.array([80,255,255])
mask = cv2.inRange(HSV, lowerrange, upperrange)

reverse = cv2.bitwise_not(mask)
cv2.imshow("display", reverse)

cv2.waitKey(0)