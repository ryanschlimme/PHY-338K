import numpy as np
import matplotlib.pyplot as plt

def EbersMoll(x):
    return 10e-9*(np.exp(x/0.025)-1)

xvals = np.linspace(0, 1, 10000)

slope = (xvals[9000]-xvals[8999])/(np.log(EbersMoll(xvals[9000]))-np.log(EbersMoll(xvals[8999])))
print(slope)

plt.figure(figsize = (4,3))
plt.plot(EbersMoll(xvals), xvals)
plt.xscale("log")
plt.xlabel("ln(IC)")
plt.ylabel("VBE")
plt.savefig("Ebers_Moll")