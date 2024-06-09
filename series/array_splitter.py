import numpy as np

"""
unfinished n-dimensional array splitter
"""

def array_splitter(array, split):
    dim = len(split)
    if dim != array.ndim:
        raise IndexError("invalid dimensions for partition")
        return
    dims = []
    y = array
    for i in range(dim):
        dimens = len(y)
        split_n = split[i]
        length = dimens/split_n
        if float(int(length))!=length:
            raise ValueError(f"dimension {i} of size {dimens} does not divide into {split_n} partitions")
            return
        dims.append(int(length))
        y = y[i]
    print(dims, dim)
    x = np.zeros(dims)
    print(x)
    xflat = x.flatten()
    dim_arr = array.shape
    arr_mult = np.ones(dim)
    for i in range(dim-1):
        for j in range(1+i, dim):
            arr_mult[i]*=dim_arr[j]
    print(arr_mult)
    index = np.empty(dim)
    for i, val in np.ndenumerate(array.flatten()):
        #print(i, val)
        index = i[0]
        indeces = []
        for j in range(dim):
            indeces.append(index//arr_mult[j])
            index = index%arr_mult[j]
        #print(i, indeces)
        for j in range(dim):
            indeces[j] = int(indeces[j]%dims[j])
        print(i, indeces)
        #print(i)
        #print(i[0], i[1])
        #print(i[0]//3, i[1]//4)
        #for k in range(0, dim):
            #print(i[k]//dims[k])
        # index = 0
        # for j in range(dim):
        #     index+=i[j]*dim_arr[j]
        # print(index)
        # print(i, [i[0]//3, i[1]//4])
        # y = x
        #for j in index:
        #    y = y[j]
        
        #print(x)
        #x[]
        
    return x
array_splitter(np.ones([6, 8]), [3, 2])
