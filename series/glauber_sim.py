import numpy as np
from math import exp
from random import randint as rd, uniform as un
import matplotlib.pyplot as plt
from time import time

"""
boolean representation of spins,
False = down spin
True = up spin
"""
class point():
    def __init__(self, i, j, spin):
        self.spin 
        x = X-1
        y = Y-1
        """
        d in order:
        d10, d12, d01, d21
        """
        d = np.empty([1, 8], dtype=int)
        if i == 0:
            d[4] = X
            d[5] = j
            d[2] = 1
            d[3] = j
            d[0:4] = [1, j, x, j]
        elif i == X:
            d[0:4] = [0, j, x-1, j]
        else:
            d[0:4] = [i+1, j, i-1, j]
        if j == 0:
            d[4:8] = [i, y, i, 1]
        elif j == y:
            d[4:8] = [i, y, i, 0]
        else:
            d[4:8] = [i, j-1, i, j+1]
        self.d = d
        
def gen_grid(x, y):
    grid = np.empty([x, y], dtype=bool)
    for i in range(x):
        for j in range(y):
            grid[i][j] = rd(0, 1)
    return np.ndarray.tolist(grid)


n = 10000
T = 0.1
X = 2
Y = 3
grid = gen_grid(X, Y)

def plot_grid(grid):
    j = len(grid[0])
    i = len(grid)
    x_values =  np.linspace(0, i-1, i, dtype=int)
    y_values = np.linspace(0, j-1, j, dtype=int)
    x, y = np.meshgrid(x_values, y_values)
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, grid)
    

            
def glauber():
    x = len(grid)-1
    y = len(grid[0])-1
    iters = (x+1)*(y+1)*n
    for k in range(iters):
        i = rd(0, x)
        j = rd(0, y)
        d_11  = grid[i][j]*2-1
        if i == 0:
            d_12 = 0
            d_10 = grid[1][j]*2-1
        elif i == x:
            d_12 = grid[x-1][j]*2-1
            d_10 = 0
        else:
            d_10 = grid[i+1][j]*2-1
            d_12 = grid[i-1][j]*2-1
        if j == 0:
            d_21 = grid[i][1]*2-1
            d_01 = 0
        elif j == y:
            d_21 = 0
            d_01 = grid[i][y-1]*2-1
        else:
            d_21 = grid[i][j+1]*2-1
            d_01 = grid[i][j-1]*2-1
        S = d_10 + d_12 + d_01 + d_21
        E = 2*d_11*S
        p = 1/(1 + exp(E/T))
        t = un(0, 1)
        if t<p:
            grid[i][j] = not(grid[i][j])
    plot_grid(grid)
    return grid

def glauber_warp():
    x = len(grid)-1
    y = len(grid[0])-1
    iters = (x+1)*(y+1)*n
    for k in range(iters):
        i = rd(0, x)
        j = rd(0, y)
        d_11  = grid[i][j]*2-1
        if i == 0:
            d_12 = grid[x][j]*2-1
            d_10 = grid[1][j]*2-1
        elif i == x:
            d_12 = grid[x-1][j]*2-1
            d_10 = grid[0][j]*2-1
        else:
            d_10 = grid[i+1][j]*2-1
            d_12 = grid[i-1][j]*2-1
        if j == 0:
            d_21 = grid[i][1]*2-1
            d_01 = grid[i][y]*2-1
        elif j == y:
            d_21 = grid[i][0]*2-1
            d_01 = grid[i][y-1]*2-1
        else:
            d_21 = grid[i][j+1]*2-1
            d_01 = grid[i][j-1]*2-1
        S = d_10 + d_12 + d_01 + d_21
        E = 2*d_11*S
        p = 1/(1 + exp(E/T))
        t = un(0, 1)
        if t<p:
            grid[i][j] = not(grid[i][j])
    plot_grid(grid)
    return grid

def metropolis():
    x = len(grid)-1
    y = len(grid[0])-1
    iters = (x+1)*(y+1)*n
    for k in range(iters):
        i = rd(0, x)
        j = rd(0, y)
        d_11  = grid[i][j]*2-1
        if i == 0:
            d_12 = 0
            d_10 = grid[1][j]*2-1
        elif i == x:
            d_12 = grid[x-1][j]*2-1
            d_10 = 0
        else:
            d_10 = grid[i+1][j]*2-1
            d_12 = grid[i-1][j]*2-1
        if j == 0:
            d_21 = grid[i][1]*2-1
            d_01 = 0
        elif j == y:
            d_21 = 0
            d_01 = grid[i][y-1]*2-1
        else:
            d_21 = grid[i][j+1]*2-1
            d_01 = grid[i][j-1]*2-1
        S = d_10 + d_12 + d_01 + d_21
        E = 2*d_11*S
        if E<0:
            grid[i][j] = not(grid[i][j])
        else:
            p = exp(-E/T)
            t = un(0, 1)
            if t<p:
                grid[i][j] = not(grid[i][j])
    plot_grid(grid)
    return grid

def metropolis_warp():
    x = len(grid)-1
    y = len(grid[0])-1
    iters = (x+1)*(y+1)*n
    for k in range(iters):
        i = rd(0, x)
        j = rd(0, y)
        d_11  = grid[i][j]*2-1
        if i == 0:
            d_12 = grid[x][j]*2-1
            d_10 = grid[1][j]*2-1
        elif i == x:
            d_12 = grid[x-1][j]*2-1
            d_10 = grid[0][j]*2-1
        else:
            d_10 = grid[i+1][j]*2-1
            d_12 = grid[i-1][j]*2-1
        if j == 0:
            d_21 = grid[i][1]*2-1
            d_01 = grid[i][y]*2-1
        elif j == y:
            d_21 = grid[i][0]*2-1
            d_01 = grid[i][y-1]*2-1
        else:
            d_21 = grid[i][j+1]*2-1
            d_01 = grid[i][j-1]*2-1
        S = d_10 + d_12 + d_01 + d_21
        E = 2*d_11*S
        p = exp(-E/T)
        t = un(0, 1)
        if E<0:
            grid[i][j] = not(grid[i][j])
        else:
            p = exp(-E/T)
            t = un(0, 1)
            if t<p:
                grid[i][j] = not(grid[i][j])
    plot_grid(grid)
    return grid
t1 = time()
#metropolis_warp()
t2 = time()
print(t2-t1)