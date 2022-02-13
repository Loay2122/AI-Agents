import numpy as np
import cv2

#########scaling#########
File_name = "img.jpg"
window_name = "Scaling Image"

img = cv2.imread(File_name)
(height, width) = img.shape[:2]
res = cv2.resize(img, (int(width/2 ), int(height/2)), interpolation=cv2.INTER_CUBIC)
cv2.imshow("Source", img)
cv2.imshow(window_name, res)
cv2.waitKey(0)

#########rotation#########
window_name = "Rotation Image"
img = cv2.imread(File_name)
res = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow(window_name, res)
cv2.waitKey(0)

#########cutting##########

img = cv2.imread(File_name)
print(img.shape)
cropedImg = img[0:50, 0:50,]
cv2.imshow("Original", img)
cv2.imshow("Croped", img)
cv2.waitKey(0)
print("End")