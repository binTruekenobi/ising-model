import numpy as np
from math import exp, sin
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

def allup(x, y, z):
    return np.array([[[True]*x]*y]*z, dtype=bool)

n = 1
T = 15
X = 8
Y = 8
Z = 8
grid = allup(X, Y, Z)
field = 0

def getpoint(i, j, k):
    return [(i+1)%X, (i-1)%X, (j+1)%Y, (j-1)%Y, (k+1)%Z, (k-1)%Z]

def energy(grid, field):
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
                E-=grid[i][j][k]*(S+field)
    return E

def field_str(x):
    return (1-4*abs(x - (1/4) - int(x + (1/4))))*50

def magnetism(grid):
    M=0
    for i in grid:
        for j in i:
            for k in j:
                M+=k
    return M*2-X*Y*Z

def glauber_warp(tick):
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
        E = 2*grid[i][j][k]*(S+field)
        p = 1/(1 + exp(E/T))
        t = un(0, 1)
        if t<p:
            grid[i][j][k] = not(grid[i][j][[k]])
    return magnetism(grid)

ticks = 50
reps = 500
#temp= 0.8


eng_avg = np.zeros(ticks)
iter8 = np.linspace(0, ticks-1, num=ticks, dtype=int)
vals = np.array([field_str(i/ticks) for i in iter8])
for i in range(0, reps):
    for j in iter8:
        timer = j/ticks
        eng = glauber_warp(timer)
        eng_avg[j] += eng/reps
plt.plot(vals, eng_avg, 'o')