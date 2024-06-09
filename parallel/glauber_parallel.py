from multiprocessing import Process, Queue
import numpy as np
from math import exp
from random import randint as rd, uniform as un
import matplotlib.pyplot as plt

n_cores = 10

def analyse(data):
    l = len(data)
    mean = sum(data)/l
    var = 0
    for i in data:
        var+=i**2
    var/=l
    var-=mean**2
    return (mean, var)
        
def gen_grid(x, y):
    grid = np.empty([x, y], dtype=bool)
    for i in range(x):
        for j in range(y):
            grid[i][j] = rd(0, 1)
    return grid

n = 50
X = 10
Y = 10
field = 0
grid = gen_grid(X, Y)
N = X*Y

def energy(grid):
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

def magnetism(grid):
    M=0
    for i in grid:
        for j in i:
            M+=j
    return M*2-X*Y

def glauber_warp(T, grid):
    engs = np.empty(n)
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
        E = 2*d_11*(S + field)
        p = 1/(1 + exp(E/T))
        t = un(0, 1)
        if t<p:
            grid[i][j] = not(grid[i][j])
        if k%(X*Y):
            engs[k//(X*Y)] = energy(grid)
    return engs

reps = 100
def simulate_temperature(temp, result_queue):
    mean = 0
    variance = 0
    for k in range(reps):
        grid = gen_grid(X, Y)
        vals = glauber_warp(temp, grid)
        m = sum(vals)/N
        v = 0
        for i in vals:
            v+=i**2
        v/=N
        v -= m**2
        mean+=m
        variance+=v
    result_queue.put([mean/reps, variance/reps])


#temperatures = np.linspace(1, 15, num=10)
if __name__ == "__main__":
    vals = []
    temperatures = np.linspace(0.1, 5, num=30)
    ns = len(temperatures)
    temps_split = [temperatures[n_cores*i:n_cores*(i+1)] for i in range((ns//n_cores))] + [temperatures[n_cores*(ns//n_cores):]]
    for i in temps_split:
        result_queue = Queue()
        processes = []
        for temp in i:
            process = Process(target=simulate_temperature, args=(temp, result_queue))
            processes.append(process)
            process.start()
        for process in processes:
            process.join()
        while not result_queue.empty():
            vals.append(result_queue.get())
        #print("All simulations completed.", vals)
        
    #temperatures = np.linspace(1, 15, num=10)
    fig, ax = plt.subplots(2, 1)
    means = [i[0] for i in vals]
    variances = [i[1] for i in vals]
    ax[0].plot(temperatures, means, '-')
    ax[1].plot(temperatures, variances, '-')