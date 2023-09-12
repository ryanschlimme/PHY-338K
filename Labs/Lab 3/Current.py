# 12 September 2023
# Ryan Schlimme

# This script analyzes data taken from an LRC cicuit to determine the relationship between frequency and the current dissipated by the resistor

import numpy as np
from matplotlib import pyplot as plt

f = [200, 250, 300, 350, 400, 450, 500, 550, 600, 700, 800, 1000]
gain = [0.28, 0.39, 0.5, 0.65, 0.82, 0.91, 0.97, 0.98, 0.9, 0.7, 0.55, 0.39]

I = [round(float((2-2*i)/100*1000), 3) for i in gain]
print(I)

plt.figure(figsize=(5,3))
# plt.margins(x=0.2, y = 10)
plt.plot(f, I, color = "b")
plt.legend(["Raw Data"])
plt.title("Relating Current and Gain")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Current (mA)")
#plt.show()
plt.savefig(r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Fall 2023\PHY 338K\Labs\Lab 3\Current.pdf")