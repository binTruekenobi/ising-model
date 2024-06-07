import numpy as np
from math import exp, sin, pi
from random import randint as rd, uniform as un
import matplotlib.pyplot as plt
        
def gen_grid(x, y):
    grid = np.empty([x, y], dtype=bool)
    for i in range(x):
        for j in range(y):
            grid[i][j] = rd(0, 1)
    return grid

def allup(x, y):
    return np.array([[True]*x]*y, dtype=bool)

n = 1
#T = 1.5
X = 20
Y = 20
grid = allup(X, Y)

def field_str(x):
    return (1-4*abs(x - (1/4) - int(x + (1/4))))

def magnetism(grid):
    M=0
    for i in grid:
        for j in i:
            M+=j
    return M*2-X*Y


def glauber_warp(tick, T):
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
    return magnetism(grid)

ticks = 500
reps = 100

temp= 0.8


eng_avg = np.zeros(ticks)
iter8 = np.linspace(0, ticks-1, num=ticks, dtype=int)
vals = np.array([field_str(i*1.5/ticks) for i in iter8])
for i in range(0, reps):
    for j in iter8:
        timer = 1.5*j/ticks
        eng = glauber_warp(timer, temp)
        eng_avg[j] += eng/reps
plt.plot(vals, eng_avg, '-')
    
        