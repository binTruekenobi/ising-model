import numpy as np
from math import exp
from random import randint as rd, uniform as un
import matplotlib.pyplot as plt
       
def gen_grid(x, y):
    grid = np.empty([x, y], dtype=bool)
    for i in range(x):
        for j in range(y):
            grid[i][j] = rd(0, 1)
    return grid


X = 7
Y = 7
field = 0


def glauber_warp(T):
    x = len(grid)-1
    y = len(grid[0])-1
    count = 0
    while not (grid.all() or not grid.any()):
        i = rd(0, x)
        j = rd(0, y)
        d_11  = grid[i][j]*2-1
        d_10 = grid[(i+1)%X][j%Y]*2-1
        d_12 = grid[(i-1)%X][j%Y]*2-1
        d_01 = grid[i%X][(j+1)%Y]*2-1
        d_21 = grid[i%X][(j-1)%Y]*2-1
        S = d_10 + d_12 + d_01 + d_21
        E = 2*d_11*S
        p = 1/(1 + exp(E/T))
        t = un(0, 1)
        if t<p:
            grid[i][j] = not(grid[i][j])
        count+=1
    return count

nums = 100
iters = 1000
vals = np.empty(nums)
x_vals = np.linspace(1, 2.5, num=nums)
for k in range(0, nums):
    i = x_vals[k]
    print(i)
    val = 0
    for j in range(0, iters):
        grid = gen_grid(X, Y)
        val+=glauber_warp(i)
    val/=iters
    vals[k] = val
plt.plot(x_vals, vals, '-', c='b')

