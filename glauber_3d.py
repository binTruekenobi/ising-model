import numpy as np
from math import exp
from random import randint as rd, uniform as un
import matplotlib.pyplot as plt

"""
boolean representation of spins,
False = down spin
True = up spin

Glauber dynamics program which returns resulting energy
(as animations and graphs are not suitable)
"""

        
def gen_grid(x, y, z):
    grid = np.empty([x, y, z], dtype=bool)
    for i in range(x):
        for j in range(y):
            for k in range(z):
                grid[i][j][k] = rd(0, 1)
    return grid


n = 500
#T = 1
X = 10
Y = 10
Z = 10
grid = gen_grid(X, Y, Z)
field = 0

def getpoint(i, j, k):
    return [(i+1)%X, (i-1)%X, (j+1)%Y, (j-1)%Y, (k+1)%Z, (k-1)%Z]

def energy():
    E=0
    store = np.empty(6, dtype=bool)
    for i in range(0, X):
        for j in range(0, Y):
            for k in range(0, Z):
                points = getpoint(i, j, k)
                store[0:6] = [grid[points[0]][j][k], grid[points[1]][j][k],
                grid[i][points[2]][k], grid[i][points[3]][k],
                grid[i][j][points[4]], grid[i][j][points[5]]]
                S = np.sum(points)*2-6
                E-=grid[i][j][k]*S
    return E

def glauber_warp(T):
    x = len(grid)-1
    y = len(grid[0])-1
    z = len(grid[0][0])-1
    store = np.empty(6, dtype=bool)
    iters = (x+1)*(y+1)*(z+1)*n
    for l in range(iters):
        i = rd(0, x)
        j = rd(0, y)
        k = rd(0, z)
        points = getpoint(i, j, k)
        store[0:6] = [grid[points[0]][j][k], grid[points[1]][j][k],
        grid[i][points[2]][k], grid[i][points[3]][k],
        grid[i][j][points[4]], grid[i][j][points[5]]]
        S = np.sum(points)*2-6
        E = 2*grid[i][j][k]*S
        p = 1/(1 + exp(E/T))
        t = un(0, 1)
        if t<p:
            grid[i][j][k] = not(grid[i][j][[k]])
    return energy()


for t in np.linspace(2, 7, num=500):
    grid = gen_grid(X, Y, Z)
    eng = glauber_warp(t)
    plt.plot(t, eng, 'o')