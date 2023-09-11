# Ryan Schlimme
# 10 September 2023

# Plotting circuit B in Lab 2 gain vs frequency relationship. Determining the 3 dB point from gain plot.

import numpy as np
from matplotlib import pyplot as plt

f = [40, 100, 200, 300, 400, 1000, 2000, 3000, 4000, 10000, 20000, 40000]
gain = [0.16, 0.3, 0.5, 0.63, 0.7, 0.86, 0.89, 0.89, 0.91, 0.92, 0.92, 0.91]

dB3 = 1/ (10000*0.0015e-6) / (2*np.pi)    # The 3dB point as 1/RC


plt.figure(figsize=(5,3))
# plt.margins(x=0.2, y = 10)
plt.plot(f, gain, color = "b")
plt.xscale("log")
plt.vlines(dB3, ymin = 0, ymax = 1, color = "k")
plt.legend(["Raw Data", "3 dB Point"])
plt.title("Relating Frequency and Gain")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain")
#plt.show()
plt.savefig(r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Fall 2023\PHY 338K\Labs\Lab 2\CircuitB_f_vs_gain.pdf")