import matplotlib.pyplot as plt
import numpy as np

temps= [0, 0, 0, 0]

dps = np.array([4, 3.6, 3.2, 2.8, 2.4, 2])
dps = dps * 0.986923

for i in range (1, 5):
    temps[i-1] = np.loadtxt(f"temp{i}.txt", dtype = float)

def plf(x, y):
    return np.polyfit(x, y, 1)

k = []

for i in range(4):
    k.append(plf(dps, temps[i]))

np.savetxt("coeffs.txt", k)

def sigma(coeffs, y, x):
    bs = []
    y1 = []
    y2 = []

    for i in range(len(y)):
        y1.append(np.mean(y[i]*y[i]))
    for i in range(len(y)):
        y2.append(np.mean(y[i])**2)
    for i in range(len(y)):
        tmp = x * x;
        x1 = np.mean(tmp)
    for i in range(len(y)):
        x2 = np.mean(x)**2
    for i in range(len(y)):
        bs.append((np.sqrt(((y1[i] - y2[i])/(x1 - x2)) - coeffs[i][0]**2))/np.sqrt(len(y)))

    return bs


np.savetxt("sigmas.txt", sigma(k, temps, dps))



##Графики Графики Графики Графики Графики Графики Графики Графики Графики Графики Графики Графики Графики 

ts = [20, 30, 50, 60]

for i in range(4):
    yfit = np.polyval(k[i], dps)

    fig, ax = plt.subplots(figsize = (8, 6), dpi = 400)
    ax.plot(dps, yfit, c = "black")
    ax.scatter(dps, temps[i])
    plt.title(f"t = {ts[i]} градусов Цельсия")
    plt.ylabel("Температура, градус Цельсия")
    plt.xlabel("Давление, Бар")
    ax.grid(b=True, which='major', color='grey', linestyle='-')
    ax.grid(b=True, which='minor', color='grey', linestyle='--')
    plt.minorticks_on()
    fig.savefig(f"plot{i+1}.png")