import subprocess
import matplotlib.pyplot as plt
from numpy import array, linspace

cpp_output = subprocess.check_output(["ising_C_energy_vs_temperature/x64/Debug/ising_C_energy_vs_temperature.exe"]).decode("utf-8")

my_list = array([float(x) for x in cpp_output.strip().split()])
n = len(my_list)

#plt.plot(my_list[:int(n/2)])
#plt.xlabel("Iteration point / n")
#plt.ylabel("Energy")
#plt.show()

temps = linspace(0.2, 5, num=50)

fig, ax = plt.subplots(1, 2)

ax[0].plot(temps, my_list[int(n/2):]) #row=0, col=0
#ax[0].xlabel("temperature")
#ax[0].ylabel("mean Energy")

ax[1].plot(temps, my_list[:int(n/2)]) #row=1, col=0
#ax[1].xlabel("temperature")
#ax[1].ylabel("variance in energy")