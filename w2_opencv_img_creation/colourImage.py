import numpy as np
import cv2 as cv

# 300x300, BGR
colorImg = np.zeros((300,300,3),np.uint8)

triSwipe = 255

for x in range(300):
    for y in range(300):
        
        if x <= 100: # Blue
            colorImg[x] = [triSwipe,0,0]
        
        elif x > 100 and x <= 200: # Green
            if (x == 101): triSwipe = 255
            colorImg[x] = [0,triSwipe,0]

        elif x > 200 and x <= 300: # Red
            if (x == 201): triSwipe = 255
            colorImg[x] = [0,0,triSwipe]
    triSwipe -= 1

        
cv.imshow("colour image - CMP4221" ,colorImg)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("colourImg.png", colorImg)
