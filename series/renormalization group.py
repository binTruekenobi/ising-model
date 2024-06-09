import numpy as np
from math import exp
from random import randint as rd, uniform as un
import matplotlib.pyplot as plt
from time import time
from matplotlib import colors
import matplotlib.animation as animation
import array_splitter_2d as asp

"""
boolean representation of spins,
False = down spin
True = up spin

in plot_grid, values of 1 represent up spin and 0 represents down spin
in plot_grid2, Blue is up spin and red is down spin
in the animation, yellow is up spin and purple is down spin
"""

        
def gen_grid(x, y):
    grid = np.empty([x, y], dtype=int)
    for i in range(x):
        for j in range(y):
            grid[i][j] = rd(0, 1)*2-1
    return grid

def allup(x, y):
    return np.array([[True]*x]*y, dtype=int)

n = 25
T = 50
field = 0
d1 = 2
d2 = 2


def plot_grid(grid):
    i = len(grid[0])
    j = len(grid)
    x_values =  np.linspace(0, i-1, i, dtype=int)
    y_values = np.linspace(0, j-1, j, dtype=int)
    x, y = np.meshgrid(x_values, y_values)
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, grid)
    
def plot_grid2(grid):
    cmap = colors.ListedColormap(['Blue','red'])
    plt.pcolor(grid[::-1], cmap=cmap, edgecolors='k', linewidths=1)
    plt.show()
    
def energy(grid, J):
    E=0
    for i in range(0, X):
        for j in range(0, Y):
            d_10 = grid[(i+1)%X][j]
            d_12 = grid[(i-1)%X][j]
            d_01 = grid[i][(j+1)%Y]
            d_21 = grid[i][(j-1)%Y]
            S = d_10 + d_12 + d_01 + d_21
            E+= (S*J+field)*grid[i][j]
    return -E

def magnetism(grid):
    M=0
    for i in grid:
        for j in i:
            M+=j
    return M*2-X*Y

def glauber_warp(grid, X, Y, J):
    eng = np.empty(Y)
    x = len(grid)-1
    y = len(grid[0])-1
    iters = (x+1)*(y+1)*n
    for k in range(iters):
        i = rd(0, x)
        j = rd(0, y)
        d_11  = grid[i][j]
        d_10 = grid[(i+1)%X][j%Y]
        d_12 = grid[(i-1)%X][j%Y]
        d_01 = grid[i%X][(j+1)%Y]
        d_21 = grid[i%X][(j-1)%Y]
        S = d_10 + d_12 + d_01 + d_21
        E = 2*J*d_11*(S + field)
        p = 1/(1 + exp(E/T))
        t = un(0, 1)
        if t<p:
            grid[i][j] = not(grid[i][j])
        if not k%(n*X):
            #print(k)
            eng[k//(n*X)] = energy(grid, J)
    #print(X*Y*(field+4))
    return eng

X = 32
Y = 32
J=1
grid = gen_grid(X, Y)
for i in range(0, 4):
    engs = glauber_warp(grid, X, Y, J)
    plt.plot(engs)
    grid = asp.array_splitter(grid)
    X = int(X/2)
    Y = int(Y/2)
    J*=2
