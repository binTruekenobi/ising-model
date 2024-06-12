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

in plot_grid, values of 1 represent up spin and 0 represents down spin
in plot_grid2, Blue is down spin and red is up spin
in the animation, yellow is up spin and purple is down spin
"""

        
def gen_grid(x, y):
    grid = np.empty([x, y], dtype=int)
    for i in range(x):
        for j in range(y):
            grid[i][j] = rd(0, 1)*2-1
    return grid


n = 500
T = 5
X = 500
Y = 500
field = 0
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
    cmap = colors.ListedColormap(['Blue','red'])
    plt.pcolor(grid[::-1], cmap=cmap, edgecolors='k', linewidths=0.2)
    plt.show()
    
def energy(grid):
    E=0
    for i in range(0, X):
        for j in range(0, Y):
            d_10 = grid[(i+1)%X][j]
            d_12 = grid[(i-1)%X][j]
            d_01 = grid[i][(j+1)%Y]
            d_21 = grid[i][(j-1)%Y]
            S = d_10 + d_12 + d_01 + d_21
            E+= (S+field)*grid[i][j]
    return -E


def glauber_warp():
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
        E = 2*d_11*(S + field)
        p = 1/(1 + exp(E/T))
        t = un(0, 1)
        if t<p:
            grid[i][j] = -grid[i][j]
    return energy(grid)

glauber_warp()
plot_grid2(grid)
# def generate_data():
#     glauber_warp()
#     return grid

# def update(data):
#     mat.set_data(data)
#     return mat 

# def data_gen():
#     while True:
#         yield generate_data()

# fig, ax = plt.subplots()
# mat = ax.matshow(generate_data())
# plt.colorbar(mat)
# ani = animation.FuncAnimation(fig, update, data_gen, interval=5, save_count=1500)
# plt.show()
#ani.save("500_500_1500frame_25fps_bool_test.gif", dpi=300, writer=animation.PillowWriter(fps=25))
#ani.save('animation.mp4')
        
#t1 = time()
#glauber_warp()
#t2 = time()
#print(t2-t1)