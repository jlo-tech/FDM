import math
import time
import scipy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def heatmap(states, k):
    
    ed = np.expand_dims(states[k], axis=1)
    
    plt.clf()
    plt.pcolormesh(ed, cmap=plt.cm.jet, vmin=0, vmax=10)
    plt.colorbar()

    return plt
    
def animate(k):
    heatmap(states, k)


xs = 100
vec = np.zeros(xs)
vec[xs // 2] = 100

states = [vec]

t = 0

alpha = 2
dx = 1
dt = (dx ** 2) / (4 * alpha)

coeff = alpha * (dt / dx**2)

while t < 30:

    # Build and solve matrix
    mat = np.zeros((xs, xs))
    
    # Solution vector
    sol = np.zeros(xs)
    
    for i in range(xs):
        sol[i] = (-states[-1][i] / coeff)
    
    # Boundary conditions 50° in the middle of the rod
    sol[xs // 2] = -(50 / coeff)
    
    # Fill matrix
    for i in range(xs):
        tv = np.zeros(xs)
        tv[0] = 1
        tv[1] = (-2 - 1/coeff)
        tv[2] = 1
        mat[i] = scipy.ndimage.shift(tv, -1 + i, cval=0.0)
    
    r = scipy.linalg.solve(mat, sol)
    
    states.append(r)
    
    t += dt
 
animator = anim.FuncAnimation(plt.figure(), animate, interval=1, frames=len(states), repeat=True)
animator.save("heat.gif")
