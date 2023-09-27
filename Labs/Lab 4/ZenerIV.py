# Ryan Schlimme
# 24 September 2023

import numpy as np
from matplotlib import pyplot as plt

V = [1.1, 1.3, 1.5, 2.0, 2.4, 3.0, 3.3, 3.7]
I = [228, 338, 750, 1200 ,1500 ,2002, 2360, 2700]

plt.figure(figsize = (4,3))
plt.plot(V, I)
plt.xlabel("Voltage (V)")
plt.ylabel("Current (microAmps)")
plt.title("I-V Plot for Zener Diode")
plt.savefig("ZenerIV.png")