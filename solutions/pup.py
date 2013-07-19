from pylab import *

# Load and view image
im = loadtxt('pup.txt')
imshow(im)
gray()
show()

# Get each 'quadrant'
[m, n] = shape(im)
quad1 = im[:m/2,:n/2]
quad2 = im[m/2:,:n/2]
quad3 = im[:m/2,n/2:]
quad4 = im[m/2:,n/2:]

# Use 'stack' functions to rearrange the quadrants
reconstructed_im = vstack([hstack([quad3, quad4]), hstack([quad1, quad2])])

# Finally, transpose the matrix and show corrected image
imshow(transpose(reconstructed_im))
show()
