import subprocess
import matplotlib.pyplot as plt

cpp_output = subprocess.check_output(["C++/ising_C/x64/Debug/ising_C.exe"]).decode("utf-8")

my_list = [float(x) for x in cpp_output.strip().split()]

plt.plot(my_list)
plt.xlabel("Iteration point / n")
plt.ylabel("Energy")
plt.show()