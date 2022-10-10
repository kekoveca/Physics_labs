from cmath import pi
import matplotlib.pyplot as plt
import numpy as np

c = 0.2 * 9.8

h5l = np.loadtxt("h5l.txt", dtype = float)
h5t = np.loadtxt("h5t.txt", dtype = float)
h7l = np.loadtxt("h7l.txt", dtype = float)
h7t = np.loadtxt("h7t.txt", dtype = float)

h5l = h5l * c;
h5t = h5t * c;
h7l = h7l * c;
h7t = h7t * c;

q5l = np.loadtxt("q5l.txt", dtype = float)
q5t = np.loadtxt("q5t.txt", dtype = float)
q7l = np.loadtxt("q7l.txt", dtype = float)
q7t = np.loadtxt("q7t.txt", dtype = float)

q5l = q5l * 0.001 * 2;
q5t = q5t * 0.001 * 2;
q7l = q7l * 0.001 * 2;
q7t = q7t * 0.001 * 2;

print(q5l)

y = np.array([q5l, q5t, q7l, q7t])
x = np.array([h5l, h5t, h7l, h7t])

def plf(x, y):
    return np.polyfit(x, y, 1)

k = []

for i in range(4):
    k.append(plf(x[i], y[i]))


# np.savetxt("coeffs.txt", k)

def sigma(coeffs, y, x):
    bs = []
    y1 = []
    y2 = []
    x1 = []
    x2 = []

    for i in range(len(y)):
        y1.append(np.mean(y[i]*y[i]))
    for i in range(len(y)):
        y2.append(np.mean(y[i])**2)
    for i in range(len(y)):
        x1.append(np.mean(x[i]*x[i]))
    for i in range(len(y)):
        x2.append(np.mean(y[i])**2)
    for i in range(len(y)):
        bs.append((np.sqrt(abs(((y1[i] - y2[i])/(x1[i] - x2[i])) - coeffs[i][0]**2)))/np.sqrt(len(y[i])))

    return bs


# np.savetxt("sigmas.txt", sigma(k, y, x))



#Графики Графики Графики Графики Графики Графики Графики Графики Графики Графики Графики Графики Графики 

# ts = ["50 см, d = 4,1 мм, ламинарный поток", "50 см, d = 4,1 мм, турбулентный поток", "70 см, d = 5,2 мм, ламинарный поток", "70 см, d = 5,2 мм, турбулентный поток"]

# for i in range(4):
#     yfit = np.polyval(k[i], x[i])

#     fig, ax = plt.subplots(figsize = (8, 6), dpi = 400)
#     ax.plot(x[i], yfit, c = "black")
#     ax.scatter(x[i], y[i])
#     plt.title(f"{ts[i]}")
#     plt.ylabel("Расход, л/c")
#     plt.xlabel("Давление, Паскали")
#     ax.grid(b=True, which='major', color='grey', linestyle='-')
#     ax.grid(b=True, which='minor', color='grey', linestyle='--')
#     plt.minorticks_on()
#     fig.savefig(f"plot{i+1}.png")

px1 = np.loadtxt("px1.txt", dtype = float)
px2 = np.loadtxt("px2.txt", dtype = float)
x1 = np.loadtxt("x1.txt", dtype = float)
x2 = np.loadtxt("x2.txt", dtype = float)

# yfit = np.polyval(k[i], x[i])

plt.subplots(figsize = (8, 6), dpi = 400)
# ax.plot(x[i], yfit, c = "black")
plt.plot(x1, px1, c = 'orange', label = "d = 4.1 mm")
plt.plot(x2, px2, label = "d = 5.2 mm")
plt.title(f"")
plt.ylabel("Давление, Па")
plt.xlabel("Длина, м")
plt.legend()
plt.grid(b=True, which='major', color='grey', linestyle='-')
plt.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
plt.savefig("plot_x.png")