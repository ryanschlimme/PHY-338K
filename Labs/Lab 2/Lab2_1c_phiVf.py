# Ryan Schlimme
# 10 September 2023

# Plotting circuit A in Lab 2 phase shift vs frequency relationship

import numpy as np
from matplotlib import pyplot as plt

f = [1000, 2000, 4000, 20000, 40000, 100000, 200000, 300000, 400000, 500000, 1000000, 1500000]
phi = [0, 1, 1, 5, 6, 18, 34, 47, 56, 60, 65, 90]


plt.figure(figsize=(5,3))
# plt.margins(x=0.2, y = 10)
plt.plot(f, phi, color = "b")
plt.xscale("log")
plt.legend(["Raw Data"])
plt.title("Relating Frequency and Phase Shift")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phi (degrees)")
plt.show()
#plt.savefig(r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Fall 2023\PHY 338K\Labs\Lab 2\CircuitA_phi_vs_gain.pdf")