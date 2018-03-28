import mahotas as mh
import numpy as np
import cv2

# Imported mahotas & numpy with standard abbreviations
im = mh.imread('./images/pool-table-above-17031042.jpg', as_grey=1)

# Load the image & convert to gray
# im2 = im[::2,::2]
im2 = mh.gaussian_filter(im, 1.2)
cv2.imshow('gaussian', im)
# save first step
# mh.imsave('1.png', im2.astype(np.uint8))

# Mean filtering is implemented "by hand" with a convolution.
mean_filtered = mh.convolve(im2.astype(float), np.ones((9, 9))/81.)

# iminv = 255 - mean_filtered
# mh.imsave('binarized1.png', iminv.astype(np.uint8))

# You might need to adjust the number 4 here, but it worked well for this image.
imc = im2 > mean_filtered - 4
# cv2.imshow('open circles', (imc*255).astype(np.uint8));
# cv2.waitKey(0)

# mh.imsave('1.png', im2.astype(np.uint8))
# print(im2)

# imc = mh.convolve(imc.astype(float), np.ones((9, 9))/81.)

# imc = im2 > mean_filtered - 6

# mh.imsave('result.png', (imc*255).astype(np.uint8))
cv2.imshow('result', (imc*255).astype(np.uint8));
cv2.waitKey(0)
cv2.destroyAllWindows()
