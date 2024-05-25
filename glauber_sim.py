import numpy as np
from math import exp
from random import randint as rd, uniform as un
import matplotlib.pyplot as plt

"""
boolean representation of spins,
False = down spin
True = up spin
"""

def gen_grid(x, y):
    grid = np.empty([x, y], dtype=bool)
    for i in range(x):
        for j in range(y):
            grid[i][j] = rd(0, 1)
    return grid

n = 100
T = 2.77
grid = gen_grid(100, 100)

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
            d_21 = grid[i][j+1]
            d_01 = grid[i][j-1]
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
            d_21 = grid[i][j+1]
            d_01 = grid[i][j-1]
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
            d_21 = grid[i][j+1]
            d_01 = grid[i][j-1]
        S = d_10 + d_12 + d_01 + d_21
        E = 2*d_11*S
        if E<0:
            grid[i][j] = not(grid[i][j])
        else:
            p = 1/(1 + exp(E/T))
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
            d_21 = grid[i][j+1]
            d_01 = grid[i][j-1]
        S = d_10 + d_12 + d_01 + d_21
        E = 2*d_11*S
        p = 1/(1 + exp(E/T))
        t = un(0, 1)
        if E<0:
            grid[i][j] = not(grid[i][j])
        else:
            p = 1/(1 + exp(E/T))
            t = un(0, 1)
            if t<p:
                grid[i][j] = not(grid[i][j])
    plot_grid(grid)
    return grid
