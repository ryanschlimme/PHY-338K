import numpy as np
import matplotlib.pyplot as plt

f = [100, 200, 400, 800, 1500, 3000, 10000, 25000, 50000, 100000, 250000, 500000]
gain = [-93.5, -98.9, -99.6, -99.6, -99.7, -99.7, -99.6, -97.8, -94.3, -92.8, -90.6, -85.3]

plt.figure(figsize = (4,3))
plt.plot(f, gain)
plt.xlabel("Frequency (log(Hz))")
plt.ylabel("Voltage Gain")
plt.xscale("log")
plt.savefig("gainVfreq.png")