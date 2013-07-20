# MANDELBROT SET
from numpy import *
from pylab import *
 
# number of iterations
iterations = 100

# density of the grid
density = 1000
 
# fractal range
x_min, x_max = -2, 1
y_min, y_max = -1.5, 1.5
 
# x, y are matrices containing the real and imaginary parts 
# of all z values in the grid
x, y = meshgrid(linspace(x_min, x_max, density),
                linspace(y_min, y_max, density))
 
# we define c as c=x+iy, c is a 1000x1000 matrix
c = x + 1j*y
 
# initially, z=c, we copy so that z and c are different objects in memory
z = c.copy()
 
# m is used to plot the fractal
m = zeros((density, density))
 
# iterations
for n in xrange(iterations):
	print "Completed %d %%" % (100 * float(n)/iterations)

	# indices of the numbers c such that |z(c)|<=10, with z = z_n
	indices = (abs(z) <= 10)

	# update z
	z[indices] = z[indices]**2 + c[indices]

	# we update the values in m
	m[indices] = n

	imshow(log(m), cmap=cm.jet, extent=(x_min, x_max, y_min, y_max))

	title('Mandelbrot Set')

	xlabel('Re(z)')
	ylabel('Im(z)')
	savefig("%4d.png"%n)
	close()
 
# we plot log(m)
imshow(log(m), cmap=cm.jet,extent=(x_min, x_max, y_min, y_max))

title('Mandelbrot Set')
xlabel('Re(z)')
ylabel('Im(z)')
show()

#Taken from http://cyrille.rossant.net/mandelbrot-set/
