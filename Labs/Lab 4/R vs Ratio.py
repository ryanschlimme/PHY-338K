import numpy as np
import matplotlib.pyplot as plt

R = [220, 470, 1000, 2200, 4700, 10000]
Vmax = [3.0, 3.2, 3.4, 3.6, 3.6, 3.6]
Vmin = [0, .6, 1.4, 2.2, 2.8, 3.2]

VDC = [1.5, 1.9, 2.4, 2.9, 3.2, 3.4]
Vripple = [3.0, 2.6, 2.0, 1.4, 0.8, 0.4]

N = range(0, len(VDC))
ratio = []

for n in N:
    ratio.append(VDC[n]/Vripple[n])

plt.figure(figsize = (4,3))
plt.plot(R, ratio)
plt.xlabel("Resistance")
plt.ylabel("VDC / Vripple")
plt.savefig("R vs Ratio")