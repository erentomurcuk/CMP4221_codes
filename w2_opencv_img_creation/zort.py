#Import all libraries we will use
import random
import numpy as np
import cv2 as cv

imageArray = np.zeros((100,100,1),np.uint8)

for x in range(100):
    for y in range(100):
        #We use "0" for black color (do nothing) and "1" for white color (change pixel value to [255,255,255])
        value = random.randint(0,5)
        if value == 1:
            imageArray[x,y] = [255]
        elif value == 2:
            imageArray[x,y] = [200]
        elif value == 3:
            imageArray[x,y] = [150]
        elif value == 4:
            imageArray[x,y] = [100]
        elif value == 5:
            imageArray[x,y] = [50]


#save our image as a "png" ima
cv.imwrite("newimage.png",imageArray)