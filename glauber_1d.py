import numpy as np
from math import exp
from random import randint as rd, uniform as un
import matplotlib.pyplot as plt
from time import time
from matplotlib import colors
import matplotlib.animation as animation

"""
boolean representation of spins,
False = down spin
True = up spin

Glauber dyamics program which is the limiting 1D case of the 2D sysem.
returns an animation
"""

        
def gen_grid(x):
    grid = np.empty(x, dtype=bool)
    for i in range(x):
        grid[i] = rd(0, 1)
    return grid


n = 1
T = 1
X = 100
grid = gen_grid(X)

def plot_grid(grid):
    plt.plot(grid)
    
def plot_grid2(grid):
    cmap = colors.ListedColormap(['red','Blue'])
    plt.pcolor(grid[::-1], cmap=cmap, edgecolor='k', linewidths=1)
    plt.show()

def energy(grid):
    """
    uses a lotof runtime?
    """
    E=0
    for i in range(0, X):
        E+= ((grid[(i+1)%X]+grid[(i-1)%X])*2-2)*(grid[i]*2-1)
    return -E

def glauber_warp():
    x = len(grid)-1
    iters = (x+1)*n
    for k in range(iters):
        i = rd(0, x)
        d_1  = grid[i]*2-1
        d_0 = grid[(i+1)%X]*2-1
        d_2 = grid[(i-1)%X]*2-1
        S = d_0 + d_2
        E = 2*d_1*S
        p = 1/(1 + exp(E/T))
        t = un(0, 1)
        if t<p:
            grid[i] = not(grid[i])
    #return grid
    #return np.reshape(grid, (-1, X))

def generate_data():
    glauber_warp()
    return np.reshape(grid, (-1, X))

def update(data):
    mat.set_data(data)
    return mat 

def data_gen():
    while True:
        yield generate_data()

fig, ax = plt.subplots()
mat = ax.matshow(generate_data())
#plt.colorbar(mat)
ani = animation.FuncAnimation(fig, update, data_gen, interval=50, save_count=50)
plt.show()
#ani.save("500_500_1500frame_25fps_test.gif", dpi=300, writer=animation.PillowWriter(fps=25))