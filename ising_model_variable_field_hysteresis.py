import numpy as np
from math import exp, sin, pi
from random import randint as rd, uniform as un
import matplotlib.pyplot as plt
from matplotlib import colors

        
def gen_grid(x, y):
    grid = np.empty([x, y], dtype=bool)
    for i in range(x):
        for j in range(y):
            grid[i][j] = rd(0, 1)
    return grid

def allup(x, y):
    return np.array([[True]*x]*y, dtype=bool)

n = 15
T = 3
X = 10
Y = 10
grid = allup(X, Y)

    
def plot_grid2(grid):
    cmap = colors.ListedColormap(['Blue','red'])
    plt.pcolor(grid[::-1], cmap=cmap, edgecolors='k', linewidths=1)
    plt.show()
    
def energy(grid, field):
    E=0
    for i in range(0, X):
        for j in range(0, Y):
            d_10 = grid[(i+1)%X][j]*2-1
            d_12 = grid[(i-1)%X][j]*2-1
            d_01 = grid[i][(j+1)%Y]*2-1
            d_21 = grid[i][(j-1)%Y]*2-1
            S = d_10 + d_12 + d_01 + d_21
            E+= (S+field)*(grid[i][j]*2-1)
    return -E

global meas
meas = 0


def field_str(tick):
    return 10*sin(2*pi*tick/(X*Y))


def glauber_warp(m=meas):
    eng = []
    vals = []
    tick = m
    x = len(grid)-1
    y = len(grid[0])-1
    iters = int((x+1)*(y+1)*n)
    field = field_str(tick)
    for k in range(iters):
        i = rd(0, x)
        j = rd(0, y)
        d_11  = grid[i][j]*2-1
        d_10 = grid[(i+1)%X][j%Y]*2-1
        d_12 = grid[(i-1)%X][j%Y]*2-1
        d_01 = grid[i%X][(j+1)%Y]*2-1
        d_21 = grid[i%X][(j-1)%Y]*2-1
        S = d_10 + d_12 + d_01 + d_21
        E = 2*d_11*(S+field)
        p = 1/(1 + exp(E/T))
        t = un(0, 1)
        if t<p:
            grid[i][j] = not(grid[i][j])
        tick+=0.01
        field = field_str(tick)
        eng.append(energy(grid, field))
        vals.append(tick)
        #print(field)
        #print(tick)
    global meas
    meas = tick
    return (vals, eng)
    #print(meas)
    #print(field)
            #print(field)
    #return energy(grid)

x_v = np.zeros([X*Y*n, 1])
y_v = np.zeros([X*Y*n, 1])
for i in range(0, 100):
    obt = glauber_warp(m=meas)
    for j in range(0, len(obt[0])):
        x_v[j]+=obt[0][j]
        y_v[j]+=obt[1][j]
plt.plot(x_v, y_v)
