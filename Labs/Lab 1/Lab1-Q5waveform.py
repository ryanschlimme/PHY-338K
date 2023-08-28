# Ryan Schlimme
# 25 August 2023

# This script plots two sine waves based on observed amplitude change in lab for use as a sketch in report.

import matplotlib.pyplot as plt
import numpy as np

xvals = np.linspace(-5*np.pi, 5*np.pi, 100)

plt.figure(figsize=(5,3))
plt.plot(xvals, 2*np.sin(xvals))
plt.plot(xvals, 2*np.sin(xvals)+1)
plt.legend(["DC Coupled", "AC Coupled"])
# plt.title("Terminator Dependence on Waveform")
plt.xlabel("AU")
plt.ylabel("V")
plt.tick_params(labelbottom = False, bottom = False)
#plt.show()
plt.savefig(r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Fall 2023\PHY 338K\Labs\Lab 1\PHY338KLab1Q7.pdf")