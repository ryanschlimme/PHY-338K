import numpy as np
import matplotlib.pyplot as plt

VCC20 = [10, 8.9, 8.5, 8.0, 7.4, 7.0, 6.5, 6.0, 5.2, 4.8, 4.2, 3.9, 3.4, 2.6, 1.9, 1.2, 0.4, 0]
VOut20 = [6.8, 5.65, 5.2, 4.7, 4.1, 3.78, 3.28, 2.8, 2.08, 1.71, 1.05, 0.85, 0.34, 0.20, 0.18, 0.15, 0.11, 0.02]
VCC40 = [10, 9.5, 8.9, 8.0, 7.1, 6.2, 4.8, 3.9, 2.8, 1.6, 0]
VOut40 = [3.7, 3.0, 2.5, 1.6, 0.81, 0.25, 0.2, 0.18, 0.15,  0.13, 0.02]
R = 1000

IC20 = [(x-y)/R for x, y in zip(map(float, VCC20), map(float, VOut20))]
IC40 = [(x-y)/R for x, y in zip(map(float, VCC40), map(float, VOut40))]

plt.figure(figsize = (4,3))
plt.plot(IC20, VOut20)
plt.plot(IC40, VOut40)
plt.legend(["20 microamps", "40 microamps"])
plt.xlabel("IC")
plt.ylabel("VCE")
plt.savefig("VCC Comparison")