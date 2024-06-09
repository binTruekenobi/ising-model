Contains ising models run using parallel/multithreaded code. (Pythons "multiprocessing" module)

**NOTE:** The number "n_cores" must be set to a number less than or equal to the number of cores (not logical cores or NUMA nodes) on the CPU it is ran on or the program will not run.

Due to python's GIL, the programs are often slower than their single-threaded/serial equivalent. 
