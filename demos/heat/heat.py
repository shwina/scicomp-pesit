from pylab import *

''' This code solves the two-dimensional heat conduction equation
	on a rectangular mesh, and saves the results the the following 
	text files:

	1. T.txt - M-by-N "temperature history". M = number of time-steps
				N = number of grid points
	
	2. x.txt and y.txt - The x- and y- co-ordinates of the grid points
	
	3. t.txt - The time steps (seconds)  '''

# Inputs

L = 0.1
H = 0.1
nx= 20
ny= 20
endtime = 20
dt = 0.25
k = 20.0
Cp = 100
rho = 50
t = arange(0, endtime+dt, dt)

# Create mesh

[x, y] = meshgrid(linspace(0, L, nx), linspace(0, H, ny))
dx = x[0, 1] - x[0, 0]
dy = y[1, 0] - y[0, 0]

# Set boundary conditions

T = zeros(shape(x))
T[:,0] = 50
T[:,-1] = 50
T[0,:] = 100
T[-1,:] = 50
T[5:10,-1] = 400
T[-1,5:10] = 400


T = ravel(T) # Flatten
T = reshape(T,[len(T),1])
boundary_indices = nonzero(T)
M = zeros([nx*ny, nx*ny])
N = copy(M)

# Construct equations:

for i in range(1,ny-1):
	for j in range(1,nx-1):
		k = i + nx*j
		M[k,k-1:k+2] = [1, -2, 1]/dx**2
		N[k,k-nx],N[k,k],N[k,k+nx] = [1, -2, 1]/dy**2

L = (M+N)
L -= diag(ravel(ones(shape(T))*rho*Cp/dt))
L[boundary_indices, :] = 0
L[boundary_indices, boundary_indices] = 1

# Simulate:

temperatures = []
for i in range(len(t)):

	R = -T*rho*Cp/dt
	R[boundary_indices] = T[boundary_indices]
	T = np.linalg.solve(L, R)
	temperatures.append(T)

# Save results:

savetxt('T.txt', temperatures)
savetxt('x.txt',x)
savetxt('y.txt',y)
savetxt('t.txt',t)
