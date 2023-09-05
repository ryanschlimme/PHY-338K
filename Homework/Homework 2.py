# 30 August 2023
# Ryan Schlimme

import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

data = pd.read_csv(r"C:\Users\ryans\OneDrive\Desktop\PHY 338K HW 2.csv", sep = ",")

Ratio = [float(i) for i in data["Ratio"].values]
omega = [float(i) for i in data["omega"].values]

plt.figure(figsize=(5,3))
plt.plot(omega, Ratio)
#plt.loglog(omega, Ratio)
plt.title("Vout/Vin as a Function of Omega")
plt.xlabel("Angular Frequency (rad/s)")
plt.ylabel("Vout/Vin")
#plt.show()
plt.savefig(r"C:\Users\ryans\OneDrive\Desktop\College\Fall 2023\PHY 338K\Homework\Homework 2\RatiovFrequency.png")