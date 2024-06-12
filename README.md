# ising-model
glauber dynamics and metropolis-hastings algorithm


gifs below are from the glauber.py
![TLI2](https://github.com/binTruekenobi/ising-model/assets/162815260/e35ee15c-9ebd-469a-9250-fbbd006d468d)
![TLI](https://github.com/binTruekenobi/ising-model/assets/162815260/36c1b9b2-e867-44b8-8316-8c2bfe5a53e1)


n is set to 1 for ideal simulation running, setting n>1 for an animated plot will result in more squares updated per frame, so more computation per frame and longer evolution.
for a final picture of the grid as the end product, comment out the animation script and put plot_grid2(grid) where the "#return grid" line is kept (line 73), giving a grid of coloured squares/rectangles (which may need to be full screened if there are hundreds of grid points per row/column as there is a black line between the squares which results in the grid looking like a single solid rectangle).
This is the 2d case, so it is directly from Kramers-Wannier duality that the curie temperature of the 2d system is approximately 2/ln(1+rt(2)), or 2.2692, it's interesting to try e.g. T=2.3 and T=2.2 to see how they differ over large times. 
