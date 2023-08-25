# Ryan Schlimme
# 25 August 2023

# This script takes experimental data for output voltage (Vo) as a function of load resistance (RL), plots the raw data, and fits it to the theoretical curve, providing estimates and errors for the function parameters.

import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

data = pd.read_csv(r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Fall 2023\PHY 338K\Labs\Lab 1\PHY 338K RL vs Vo Data.csv", sep = ",")

RL = [float(i) for i in data["RL"].values]
Vo = [float(i) for i in data["Vo"].values]
invRL = [float(1/i) for i in RL]
invVo = [float(1/i) for i in Vo]

def func(R, V, Ro):
	return R / (R + Ro) * V

guess = [2, 50]                     # Guess for V = 2, Ro = 50 Ohms
popt, pcov = curve_fit(func, RL, Vo, p0 = guess)
print("Fitted Parameters: ", popt)
print("Parameter Standard Errors: ", np.sqrt(np.diag(pcov)))

xvals = [i for i in np.linspace(0.01,10000,100)]
invxvals = [float(1/i) for i in xvals]

funcReturn = func(xvals, float(popt[0]), popt[1])
invFuncReturn = [float(1/i) for i in funcReturn]

plt.figure(figsize=(5,3))
plt.margins(x=0.2, y = 10)
plt.plot(invRL, invVo)
plt.xlim([0, 0.2])
plt.ylim([0, 70])
plt.plot(invxvals, invFuncReturn)
plt.legend(["Raw Data", "Fit"])
plt.title("Relating Load Resistance and Output Voltage")
plt.xlabel("1/Load Resistance (Ohms)")
plt.ylabel("1/Vout (Volts)")
plt.savefig(r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Fall 2023\PHY 338K\Labs\Lab 1\PHY338KLab1.pdf")