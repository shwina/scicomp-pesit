from pylab import *


i = imread('pup.jpg')

def create_jigsaw_puzzle(I):
	
	[m, n] = shape(I)
	quad1, quad2, quad3, quad4 = I[0:m/2,0:n/2], I[m/2:m,0:n/2], \
									I[0:m/2,n/2:n], I[m/2:m,n/2:n]

	I = vstack((hstack((quad3, quad4)), hstack((quad1, quad2))))
	return I

gray()

I = (np.array(imread('pup.jpg')))
I = flipud(I)
I = I[:,:,0]

imshow(I)

I = create_jigsaw_puzzle(I)

xlabel('column')
ylabel('row')
imshow(I)

imsave('pup_puzzle.png', I)
show()
