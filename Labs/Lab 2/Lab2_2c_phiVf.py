# Ryan Schlimme
# 10 September 2023

# Plotting circuit B in Lab 2 phase shift vs frequency relationship
import numpy as np
from matplotlib import pyplot as plt

f = [40, 100, 200, 300, 400, 1000, 2000, 3000, 4000, 10000, 20000, 40000]
phi = [85, 74, 58, 45, 40, 16, 8, 6, 4, 0, 0, 0]


plt.figure(figsize=(5,3))
# plt.margins(x=0.2, y = 10)
plt.plot(f, phi, color = "b")
plt.legend(["Raw Data"])
plt.title("Relating Frequency and Phase Shift")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phi (degrees)")
#plt.show()
plt.savefig(r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Fall 2023\PHY 338K\Labs\Lab 2\CircuitB_phi_vs_gain.pdf")