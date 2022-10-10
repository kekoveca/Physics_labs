import matplotlib.pyplot as plt
import numpy as np

mom = np.loadtxt("moments.txt", dtype = float)
ome = np.loadtxt("omega.txt", dtype = float)

plf = np.polyfit(mom, ome, 1)
yfit = np.polyval(plf, mom)

fig, ax = plt.subplots(figsize = (13, 8), dpi = 400)
ax.plot(mom, yfit, c = "black")
ax.scatter(mom, ome)
plt.ylabel("Omega, rad^-1")
plt.xlabel("M, N*m")
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
print(plf)
fig.savefig("graphic.png")