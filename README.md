# ising-model
glauber dynamics and metropolis-hastings algorithm


gifs below are from the glauber.py
![TLI2](https://github.com/binTruekenobi/ising-model/assets/162815260/e35ee15c-9ebd-469a-9250-fbbd006d468d)
![TLI](https://github.com/binTruekenobi/ising-model/assets/162815260/36c1b9b2-e867-44b8-8316-8c2bfe5a53e1)


n is set to 1 for ideal simulation running, setting n>1 for an animated plot will result in more squares updated per frame, so more computation per frame and longer evolution.
for a final picture of the grid as the end product, comment out the animation script and put plot_grid2(grid) where the "#return grid" line is kept (line 73), giving a grid of coloured squares/rectangles (which may need to be full screened if there are hundreds of grid points per row/column as there is a black line between the squares which results in the grid looking like a single solid rectangle).
This is the 2d case, so it is directly from Kramers-Wannier duality that the curie temperature of the 2d system is approximately 2/ln(1+rt(2)), or 2.2692, it's interesting to try e.g. T=2.3 and T=2.2 to see how they differ over large times. 

notes:
Running the glauber.py file without **modifying the animation script in lines 87-92** will cause the file to be saved to desktop.
As this runs and stores all points in one go while creating the overall gif, the ram requirements are quite high, for example, a 500x500 grid (at T=1) for 1500 frames, 25fps resulted in over 8.5 GB RAM usage, and resulted in a 31 MB gif, due to this, and through other tests, to keep the usage under 1GB, maybe aim to have width x height x frames < 10^7
i.e. a 100x100 grid would be best if ran with < 1000 frames. Other than this, the requirements are as follows:

numpy (pretty much any version will do), math's exp function (although replacing exp with np.exp would remove that requirement, random's randint and uniform (which can be replaced using numpy), time, matplotlib.pyplot, matplotlib colours, and matpplotlib.animation.

the series/parallel can be stored in about 84kb, the c++ can be stored in a similar volume but downloading the entire file takes a few hundred Mb due to he Debug file. 
An grid of size L will take about L bits of memory in most files, but the graph will take a lot more.

For the paralelized code change your cpu core number so you don't break it,
for the c++ interfacing the .exe *should* work, but you might have to recompile the c++ and then run it (changing the file name in the interface to whatever .exe pops out)



