import matplotlib.pyplot as plt
import numpy as np

dataraw = np.loadtxt("Periods.txt", dtype = float)
datarawsq = dataraw * dataraw
data = 0.000404292 * (1.4424 + 1.0947) * dataraw - 0.008392802
leng = np.arange(0, 4.5, 0.5)
lengsq = leng * leng

plf = np.polyfit(leng, data, 2)
fit = np.polyval(plf, leng)

fig, ax = plt.subplots(figsize=(16, 10), dpi = 400)
ax.plot(leng, fit, c = 'black')
plt.ylabel("I, kg*m^2")
plt.xlabel("H^2, cm^2")
plt.grid(b=True, which='major', color='grey', linestyle='-')
plt.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig.savefig("plot3.png")
#plt.show()