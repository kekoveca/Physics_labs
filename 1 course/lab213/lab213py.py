import matplotlib.pyplot as plt
import numpy as np

fta = [0, 0, 0, 0, 0]

for i in range (1, 6):
    fta[i-1] = np.loadtxt(f"fta{i}.txt", dtype = float)

ftc = [0, 0, 0, 0, 0]

for i in range (1, 6):
    ftc[i-1] = np.loadtxt(f"ftc{i}.txt", dtype = float)

def coeff(data):
    return np.polyfit(range(0, len(data)), data, 1)[0]

def plf(data):
    return np.polyfit(range(0, len(data)), data, 1)

k_air = []
k_c = []

for i in range(5):
    k_air.append(coeff(fta[i]))

for i in range(5):
    k_c.append(coeff(ftc[i]))

#np.savetxt("k_air.txt", k_air)
#np.savetxt("k_c.txt", k_c)


def sigma(coeffs, data):
    bs = []
    x1 = []
    x2 = []
    y1 = []
    y2 = []

    for i in range(len(data)):
        y1.append(np.mean(data[i]*data[i]))
    for i in range(len(data)):
        y2.append(np.mean(data[i])**2)
    for i in range(len(data)):
        xx = np.array(range(1, (len(data[i]) + 1)))
        x1.append(np.mean(xx*xx))
    for i in range(len(data)):
        xx = np.array(range(1, (len(data[i]) + 1)))
        x2.append(np.mean(xx)**2)
    for i in range(len(data)):
        bs.append((np.sqrt(((y1[i] - y2[i])/(x1[i] - x2[i])) - coeffs[i]**2))/np.sqrt(len(data[i])))

    return bs

#np.savetxt("sk_air.txt", sigma(k_air, fta))
#np.savetxt("sk_c.txt", sigma(k_c, ftc))



##Термостат Термостат Термостат Термостат Термостат Термостат Термостат Термостат Термостат Термостат Термостат

lt = [0, 0, 0, 0]

for i in range(4):
    lt[i] = np.loadtxt(f"lt{i+1}.txt", dtype = float)

k_term = []

for i in range(4):
    k_term.append(coeff(lt[i]))

np.savetxt("k_term.txt", k_term)
np.savetxt("sk_term.txt", sigma(k_term, lt))



##Графики Графики Графики Графики Графики Графики Графики Графики Графики Графики Графики Графики Графики 

temps = [30.1, 35,  40, 45]

for i in range(4):
    x = range(0, len(lt[i]))
    plf = np.polyfit(x, lt[i], 1)
    yfit = np.polyval(plf, x)

    fig, ax = plt.subplots(figsize = (8, 6), dpi = 400)
    ax.plot(x, yfit, c = "black")
    ax.scatter(x, lt[i])
    plt.title(f"t = {temps[i]} градусов Цельсия")
    plt.ylabel("f(k + 1) - f(k)")
    plt.xlabel("k")
    ax.grid(b=True, which='major', color='grey', linestyle='-')
    ax.grid(b=True, which='minor', color='grey', linestyle='--')
    plt.minorticks_on()
    fig.savefig(f"g_lt{i+1}.png")


freqs_air = [3409, 3816, 4051, 4628, 5018]

for i in range(5):
    x = range(0, len(fta[i]))
    plf = np.polyfit(x, fta[i], 1)
    yfit = np.polyval(plf, x)

    fig, ax = plt.subplots(figsize = (8, 6), dpi = 400)
    ax.plot(x, yfit, c = "black")
    ax.scatter(x, fta[i])
    plt.title(f"L(k) для {freqs_air[i]} Гц, воздух")
    plt.ylabel("L, мм")
    plt.xlabel("k")
    ax.grid(b=True, which='major', color='grey', linestyle='-')
    ax.grid(b=True, which='minor', color='grey', linestyle='--')
    plt.minorticks_on()
    #fig.savefig(f"g_fta{i+1}.png")


freqs_c = [3058, 3421, 3833, 4047, 4517]

for i in range(5):
    x = range(0, len(ftc[i]))
    plf = np.polyfit(x, ftc[i], 1)
    yfit = np.polyval(plf, x)

    fig, ax = plt.subplots(figsize = (8, 6), dpi = 400)
    ax.plot(x, yfit, c = "black")
    ax.scatter(x, ftc[i])
    plt.title(f"L(k) для {freqs_c[i]} Гц, CO2")
    plt.ylabel("L, мм")
    plt.xlabel("k")
    ax.grid(b=True, which='major', color='grey', linestyle='-')
    ax.grid(b=True, which='minor', color='grey', linestyle='--')
    plt.minorticks_on()
    #fig.savefig(f"g_ftc{i+1}.png")