import subprocess
import matplotlib.pyplot as plt
from numpy import array
#takes the output of the C++ executable, processes it, and  plots it. Note: using int(x) or just x can work but if the field is fractional, int(x) rounds values.

c_out = subprocess.check_output(["ising_C.exe"]).decode("utf-8")

vals = array([float(x) for x in c_out.strip().split()])

plt.plot(vals)
plt.xlabel("Iteration point / n")
plt.ylabel("Energy")
plt.show()
