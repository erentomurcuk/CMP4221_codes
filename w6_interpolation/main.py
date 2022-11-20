import cv2 as cv

# Read image - 64x64 Lena - Coloured
img64 = cv.imread('lena64.jpg')

# Bilinear Interpolation
img128_bl = cv.resize(img64, (128, 128), cv.INTER_LINEAR)
cv.imwrite('lena128_bl.jpg', img128_bl)

# Bicubic Interpolation
img128_bc = cv.resize(img64, (128, 128), cv.INTER_CUBIC)
cv.imwrite('lena128_bc.jpg', img128_bc)

# Nearest Neighbour Interpolation
img128_nn = cv.resize(img64, (128, 128), cv.INTER_NEAREST)
cv.imwrite('lena128_nn.jpg', img128_nn)

# Lanczos Interpolation
img128_lz = cv.resize(img64, (128, 128), cv.INTER_LANCZOS4)
cv.imwrite('lena128_lz.jpg', img128_lz)