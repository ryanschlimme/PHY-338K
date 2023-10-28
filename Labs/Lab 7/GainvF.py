import numpy as np
import matplotlib.pyplot as plt

f10 = [10, 20, 100, 200, 400, 1000, 3000, 10e3, 14e3, 20e3, 24e3, 30e3, 35e3]
Gain10 = [9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.4, 9.3, 8.1, 6.9, 5.8, 5.0]
f100 = [100, 300, 1000, 3000, 4000, 10e3, 14e3, 20e3, 23e3, 29e3]
Gain100 = [36.9, 36.9, 36.9, 36.9, 36.9, 36.7, 26.7, 19.3, 16.2, 13.3]

plt.figure(figsize = (4,3))
plt.loglog(f10, Gain10, label = "Gain 10")
plt.loglog(f100,Gain100, label = "Gain 100")
plt.title("Log-Log Gain as a Function of Input Frequency")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain")
plt.legend()
#plt.show()
plt.savefig("GainvF.png")