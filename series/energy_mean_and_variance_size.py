import numpy as np
from math import exp
from random import randint as rd, uniform as un
import matplotlib.pyplot as plt

n = 300

def gen_grid(x, y):
    grid = np.empty([x, y], dtype=int)
    for i in range(x):
        for j in range(y):
            grid[i][j] = rd(0, 1)*2-1
    return grid

#grid = gen_grid(X, Y)
#T = 0.8
    
def energy(X, Y, grid):
    E=0
    for i in range(0, X):
        for j in range(0, Y):
            d_10 = grid[(i+1)%X][j]
            d_12 = grid[(i-1)%X][j]
            d_01 = grid[i][(j+1)%Y]
            d_21 = grid[i][(j-1)%Y]
            S = d_10 + d_12 + d_01 + d_21
            E+= S*grid[i][j]
    return -E

def glauber_warp(X, Y, grid):
    maxeng = -4*X*Y
    iters = X*Y*n
    engs = np.empty(X*Y)
    x = len(grid)-1
    y = len(grid[0])-1
    for k in range(iters):
        i = rd(0, x)
        j = rd(0, y)
        d_11  = grid[i][j]
        d_10 = grid[(i+1)%X][j]
        d_12 = grid[(i-1)%X][j]
        d_01 = grid[i][(j+1)%Y]
        d_21 = grid[i][(j-1)%Y]
        S = d_10 + d_12 + d_01 + d_21
        E = 2*d_11*S
        p = 1/(1 + exp(E/T))
        t = un(0, 1)
        if t<p:
            grid[i][j] = -grid[i][j]
        if not k%n:
            engs[k//n] = energy(X, Y, grid)/maxeng
    return engs

nt = 30
means = np.empty(nt)
variances = np.empty(nt)
reps = 300

sizes = np.empty(nt)

T = 1
for j in range(3, nt):
    X = j
    Y = j
    N=X*Y
    sizes[j] = j**2
    mean = 0
    variance = 0
    for k in range(reps):
        grid = gen_grid(X, Y)
        vals = glauber_warp(X, Y, grid)
        m = sum(vals)/N
        v = 0
        for i in vals:
            v+=i**2
        v/=N
        v -= m**2
        mean+=m
        variance+=v
    mean/=reps
    variance/=reps
    means[j] = mean
    variances[j] = variance


fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_title("Fig 1")
ax2.set_title("Fig 2")
ax1.set_xlabel("size of grid")
ax1.set_ylabel("mean energy")
ax2.set_xlabel("size of grid")
ax2.set_ylabel("variance in energy")

ax1.plot(sizes, means) #row=0, col=0

ax2.plot(sizes, variances) #row=1, col=0

plt.show()





