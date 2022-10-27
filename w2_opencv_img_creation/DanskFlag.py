import numpy as np
import cv2 as cv

# 740x560, BGR
danmarksFlag = np.zeros((560,740,3),np.uint8)


for x in range(560):
    for y in range(740):

        if (x > 240 and x <= 320 and y <= 740):
            danmarksFlag[x,y] = [255,255,255]

        if (y > 240 and y < 320):
            danmarksFlag[x,y] = [255,255,255]

        if (x <= 240 and y <= 240) or (x > 320 and y <= 240):
            danmarksFlag[x,y] = [52, 16, 210]

        if  (x > 320 and y >= 320) or (x >= 0 and x <= 240 and y >=320):
            danmarksFlag[x,y] = [52, 16, 210]
        

        
cv.imshow("Dannebrog - CMP4221" ,danmarksFlag)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("Dannebrog.png", danmarksFlag)
