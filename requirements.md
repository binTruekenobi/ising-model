Note:
Running the glauber.py file without **modifying the animation script in lines 87-92** will cause the file to be saved to desktop.
As this runs and stores all points in one go while creating the overall gif, the ram requirements are quite high, 
for example, a 500x500 grid (at T=1) for 1500 frames, 25fps resulted in over 8.5 GB RAM usage, and resulted in a 31 MB gif, 
due to this, and through other tests, to keep the usage under 1GB, aim to have width x height x frames < 10^7
i.e. a 100x100 grid would be best if ran with < ~1000 frames. Other than this, the module requirements are as follows:

numpy (pretty much any version will do), math's exp function (although replacing exp with np.exp would remove that requirement, 
random's randint and uniform (which can be replaced using numpy), time, matplotlib.pyplot, matplotlib colours, and matpplotlib.animation.

in terms of hardware requirements:

the series/parallel can be stored in about 84kb, the c++ can be stored in a similar volume but downloading the entire file takes a few hundred Mb due to he Debug file. 
An lattice of size L will take about L bits of memory in most files, but the graph will take a lot more if you run it.

For the paralelized code change your cpu core number (n_cores) so you don't break it. Do not expect to see any significant speedup (if any) 
using this code over the serial equivalent, python has a GIL which essentially removes any easily-obtained speedup using "Process"/"Queue" 
in the multiprocessing module, a speedup will only be obtained if the c++ was parallel.

for the c++ interfacing the .exe *should* work, but you might have to recompile the c++ and then run it (changing the file name in the interface to whatever .exe pops out)

