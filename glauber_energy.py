import numpy as np
from math import exp
from random import randint as rd, uniform as un
import matplotlib.pyplot as plt

dimension = 2

"""
boolean representation of spins,
False = down spin
True = up spin

Glauber dyamics program which returns
energy for various points along the simulation
"""

        
def gen_grid(x, y):
    grid = np.empty([x, y], dtype=bool)
    for i in range(x):
        for j in range(y):
            grid[i][j] = rd(0, 1)
    return grid



X = 10
Y = 10
#grid = gen_grid(X, Y)
#print(grid)

def energy(grid):
    """
    uses a lotof runtime?
    """
    E=0
    for i in range(0, X):
        for j in range(0, Y):
            d_10 = grid[(i+1)%X][j]*2-1
            d_12 = grid[(i-1)%X][j]*2-1
            d_01 = grid[i][(j+1)%Y]*2-1
            d_21 = grid[i][(j-1)%Y]*2-1
            S = d_10 + d_12 + d_01 + d_21
            E+= S*(grid[i][j]*2-1)
    return -E

def magnetism(grid):
    M=0
    for i in grid:
        for j in i:
            M+=j
    return M*2-X*Y

def glauber_warp(n, T, grid):
    eng = []
    vals = []
    x = len(grid)-1
    y = len(grid[0])-1
    iters = (x+1)*(y+1)*n
    for k in range(iters):
        i = rd(0, x)
        j = rd(0, y)
        d_11  = grid[i][j]*2-1
        d_10 = grid[(i+1)%X][j]*2-1
        d_12 = grid[(i-1)%X][j]*2-1
        d_01 = grid[i][(j+1)%Y]*2-1
        d_21 = grid[i][(j-1)%Y]*2-1
        S = d_10 + d_12 + d_01 + d_21
        E = 2*d_11*S
        p = 1/(1 + exp(E/T))
        t = un(0, 1)
        if t<p:
            grid[i][j] = not(grid[i][j])
        if not k%(n):
            eng.append(energy(grid))
            vals.append(k)
    # if eng[-1]!=-X*Y*4:
    #     print(eng[-1])
    #     print(grid)
    return eng
    #return grid



#t1 = time()
#glauber_warp(100, 5)

#x = glauber_warp(500, 10, gen_grid(X, Y))
#plt.plot(x[0], x[1])


# for i in range(0, 100):
#     x = glauber_warp(500, 0.56, gen_grid(10, 10))[-1]
#     #if x!=-64:
#     #    print(x)
#     plt.plot(i, x, 'o')

for i in np.linspace(2.26, 2.36, num=50):
    points = []
    for j in range(0, 10):
        grid = gen_grid(X, Y)
        gr = glauber_warp(50, i, grid)
        points.append(gr[-1])
        #points.append(magnetism(glauber_warp(250, i, grid)))
    plt.plot(i, min(points), 'o')
    plt.show()
    #plt.plot(i, abs(magnetism(glauber_warp(500, i, grid))), 'o')

#t2 = time()
#print(t2-t1)