import numpy as np
from math import exp, sin, pi
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
in plot_grid2, Blue is up spin and red is down spin
in the animation, yellow is up spin and purple is down spin

this program is the optimised_glauber program,
with a variable magnetic field.
The external magnetic field is a function of the tick
system implemented into the iteration.
"""

        
def gen_grid(x, y):
    grid = np.empty([x, y], dtype=bool)
    for i in range(x):
        for j in range(y):
            grid[i][j] = rd(0, 1)
    return grid

def allup(x, y):
    return np.array([[True]*x]*y, dtype=bool)

n = 1
T = 5
X = 10
Y = 10
#field = 0.5
grid = allup(X, Y)

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
    #tick ranges from 0 to X*Y
    #return tick*((2*(tick%2))-1)
    return 10*sin(2*pi*tick/(X*Y))


def glauber_warp(m=meas):
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
        #print(field)
        #print(tick)
    global meas
    meas = tick
    #print(meas)
    #print(field)
            #print(field)
    #return energy(grid)
    

def generate_data():
    glauber_warp(m=meas)
    return grid

def update(data):
    mat.set_data(data)
    return mat 

def data_gen():
    while True:
        yield generate_data()

fig, ax = plt.subplots()
mat = ax.matshow(generate_data())
plt.colorbar(mat)
ani = animation.FuncAnimation(fig, update, data_gen, interval=50, save_count=50)
plt.show()
#ani.save("500_500_1500frame_25fps_bool_test.gif", dpi=300, writer=animation.PillowWriter(fps=25))
#ani.save('animation.mp4')
        
#t1 = time()
#glauber_warp()
#t2 = time()
#print(t2-t1)