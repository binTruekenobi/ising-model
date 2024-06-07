import numpy as np
"""
specific case array splitter  for 2d
"""
def array_splitter(array, d1=2, d2=2):
    dim = array.shape
    if dim[0]%d1 or dim[1]%d2:
        return False
    dimens = [int(dim[0]/d1), int(dim[1]/d2)]
    x = np.zeros(dimens)
    for i in range(dim[0]):
        for j in range(dim[1]):
            x[i//d1][j//d2]+=array[i][j]
    return x