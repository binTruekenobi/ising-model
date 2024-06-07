import numpy as np
import matplotlib.pyplot as plt
"""
energy against state for 3x3-digit boolean representations of spin
"""

def binary(x):
    p = bin(x)[2:]
    return '0'*(9-len(p))+p

field = 0

def energy(grid):
    E=0
    for i in range(0, 3):
        for j in range(0, 3):
            d_10 = grid[(i+1)%3][j]
            d_12 = grid[(i-1)%3][j]
            d_01 = grid[i][(j+1)%3]
            d_21 = grid[i][(j-1)%3]
            S = d_10 + d_12 + d_01 + d_21
            E+= (S+field)*grid[i][j]
    return -E
    
arr = np.empty([3, 3])

vals = np.empty(512)
engs = np.empty(512)
for i in range(0, 512):
    val = binary(i)
    for j in range(0, 8):
        arr[j//3][j%3] = val[j]
    engs[i] = energy(arr)
    vals[i] = i
plt.plot(vals, engs)
    
    