from cmath import pi
import matplotlib.pyplot as plt
import numpy as np

c = 1.96133

sgs = np.loadtxt("sgs.txt", dtype = float)
Ts = np.loadtxt("Ts.txt", dtype = float)

Ts = Ts - 273

def plf(x, y):
    return np.polyfit(x, y, 1)

def sigma(coeffs, y, x):

    y1 = (np.mean(y*y))
    y2 = (np.mean(y)**2)
    x1 = (np.mean(x*x))
    x2 = (np.mean(y)**2)
    bs = ((np.sqrt(abs(((y1 - y2)/(x1 - x2)) - coeffs[0]**2)))/np.sqrt(len(y)))
    return bs

_y = plf(Ts, sgs)
y = np.polyval(_y, Ts)

a = [_y]

np.savetxt("k.txt", _y)

sigmas = sigma(a, sgs, Ts)
np.savetxt("sigmas.txt", sigmas)

plt.subplots(figsize = (8, 6), dpi = 400)
plt.plot(Ts, y)
plt.scatter(Ts, sgs)
plt.title(f"")
plt.ylabel("Поверхностное натяжение, Н/м")
plt.xlabel("Температура, град. Цельсия")
plt.legend()
plt.grid(b=True, which='major', color='grey', linestyle='-')
plt.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
plt.savefig("sigma(T).png")

print(-Ts*_y[0])

plt.subplots(figsize = (8, 6), dpi = 400)
plt.plot(Ts, -Ts*_y[0])
plt.title(f"")
plt.ylabel("q, Дж")
plt.xlabel("Температура, град. Цельсия")
plt.legend()
plt.grid(b=True, which='major', color='grey', linestyle='-')
plt.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
plt.savefig("q(T).png")

plt.subplots(figsize = (8, 6), dpi = 400)
plt.plot(Ts, -Ts*_y[0]*sgs)
plt.title(f"")
plt.ylabel("U/F, Дж/м^2")
plt.xlabel("Температура, град. Цельсия")
plt.legend()
plt.grid(b=True, which='major', color='grey', linestyle='-')
plt.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
plt.savefig("uf(T).png")