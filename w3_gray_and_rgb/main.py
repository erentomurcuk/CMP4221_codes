import numpy as np
import cv2 as cv

# Create single-colour images
blue64 = np.zeros((64,64,3),np.uint8)
green64 = np.zeros((64,64,3),np.uint8)
red64 = np.zeros((64,64,3),np.uint8)

# Importing the image
_64pimg = cv.imread('64pimg.png')

# Convert the image to a grayscale image
_64pimg_grayscale = cv.cvtColor(_64pimg, cv.COLOR_BGR2GRAY)

# Save the monochrome image
cv.imwrite("64p_monochrome.png", _64pimg_grayscale)

# Extract colours B, G, R
_64pimg_blue = _64pimg[:,:,0]
_64pimg_green = _64pimg[:,:,1]
_64pimg_red = _64pimg[:,:,2]

# Create single colour images
for x in range (64):
    for y in range (64):
        blue64[x,y,0] = _64pimg_blue[x,y]
        green64[x,y,1] = _64pimg_green[x,y]
        red64[x,y,2] = _64pimg_red[x,y]


# Save monochrome single colour images
cv.imwrite("64p_blue.png", _64pimg_blue)
cv.imwrite("64p_green.png", _64pimg_green)
cv.imwrite("64p_red.png", _64pimg_red)

# Save coloured single colour images
cv.imwrite("64p_blue_clr.png", blue64)
cv.imwrite("64p_green_clr.png", green64)
cv.imwrite("64p_red_clr.png", red64)

# Comparison of the (0,0) pixel on the B-G-R coloured/monochrome and stock monochrome image respectively
print(f"Coloured blue: {blue64[0,0]}")
print(f"Coloured green: {green64[0,0]}")
print(f"Coloured red: {red64[0,0]}")

print(f"Grayscale blue: {_64pimg_blue[0,0]}")
print(f"Grayscale green: {_64pimg_green[0,0]}")
print(f"Grayscale red: {_64pimg_red[0,0]}")

print(f"Grayscale full image: {_64pimg_grayscale[0,0]}")