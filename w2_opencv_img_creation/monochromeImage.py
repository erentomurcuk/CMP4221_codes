import numpy as np
import cv2 as cv

# 300x256, single channel (monochrome)
monochromeImg = np.zeros((255,300,1),np.uint8)

monochromeSwipe = 255

for x in range(255):
    monochromeImg[x] = monochromeSwipe
    monochromeSwipe -= 1

        
cv.imshow("monochrome image - CMP4221" ,monochromeImg)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("monoImg.png", monochromeImg)
