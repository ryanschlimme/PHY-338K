# Ryan Schlimme
# 16 September 2023

# Producing VI curve for 1N4006 diode SPICE simulation.

import numpy as np
from matplotlib import pyplot as plt

V = [0.75, 0.1, 0.5, 0.75, 1, 5, 10, 15, 50, 100, 250, 500, 1000]
I = [2.15e-9, 4.33e-9, 74.64e-6, 1.38e-3, 3.51e-3, 42.48e-3, 92.14e-3, 141.95e-3, 491.29e-3, 990.78e-3, 2.5, 5, 10]

plt.figure(figsize=(5,3))
# plt.margins(x=0.2, y = 10)
plt.loglog(I, V, color = "b")
plt.legend(["Raw Data"])
plt.title("Relating Output Current and Input Voltage")
plt.xlabel("Current (A)")
plt.ylabel("Voltage (V)")
#plt.show()
plt.savefig(r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Fall 2023\PHY 338K\Homework\Homework 3\VI Curve.png")