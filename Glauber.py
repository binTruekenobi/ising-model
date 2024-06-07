import numpy as np
from math import exp
from random import randint as rd, uniform as un
import matplotlib.pyplot as plt
from time import time
from matplotlib import colors
import matplotlib.animation as animation

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


n = 1
T = 1
X = 500
Y = 500
grid = gen_grid(X, Y)

def plot_grid(grid):
    i = len(grid[0])
    j = len(grid)
    x_values =  np.linspace(0, i-1, i, dtype=int)
    y_values = np.linspace(0, j-1, j, dtype=int)
    x, y = np.meshgrid(x_values, y_values)
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, grid)
    
def plot_grid2(grid):
    cmap = colors.ListedColormap(['red','Blue'])
    plt.pcolor(grid[::-1], cmap=cmap, edgecolors='k', linewidths=1)
    plt.show()
def energy():
    """
    uses a lotof runtime?
    """
    E=0
    for i in range(0, X):
        for j in range(0, Y):
            E+= grid[(i+1)%X][j%Y]+grid[(i-1)%X][j%Y]+ grid[i%X][(j+1)%Y]+grid[i%X][(j-1)%Y]
    E*=2
    E-=4*X*Y
    return E

def glauber_warp():
    x = len(grid)-1
    y = len(grid[0])-1
    iters = (x+1)*(y+1)*n
    for k in range(iters):
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
    #return grid

def generate_data():
    glauber_warp()
    return grid

def update(data):
    mat.set_data(data)
    return mat 

def data_gen():
    while True:
        yield generate_data()

fig, ax = plt.subplots()
mat = ax.matshow(generate_data())
#plt.colorbar(mat)
ani = animation.FuncAnimation(fig, update, data_gen, interval=50, save_count=1500)
plt.show()
ani.save("TLI3.gif", dpi=300, writer=animation.PillowWriter(fps=25))
#ani.save('animation.mp4')

#t1 = time()
#glauber_warp()
#t2 = time()
#print(t2-t1)
