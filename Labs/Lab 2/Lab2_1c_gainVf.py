# Ryan Schlimme
# 10 September 2023

# Plotting circuit A in Lab 2 gain vs frequency relationship. Determining the 3 dB point from gain plot.

import numpy as np
from matplotlib import pyplot as plt

f = [1000, 2000, 4000, 20000, 40000, 100000, 200000, 300000, 400000, 500000, 1000000, 1500000]
gain = [0.96, 0.96, 0.96, 0.99, 0.96, 0.91, 0.78, 0.65, 0.56, 0.48, 0.27, 0.21]

dB3 = 1/ (10000*0.01e-6) / (2*np.pi)    # The 3dB point as 1/RC


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
plt.savefig(r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Fall 2023\PHY 338K\Labs\Lab 2\CircuitA_f_vs_gain.pdf")