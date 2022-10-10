import matplotlib.pyplot as plt
import numpy as np
import math as m

n1 = np.loadtxt("1.txt", dtype = float)
n2 = np.loadtxt("2.txt", dtype = float)
n3 = np.loadtxt("3.txt", dtype = float)
n4 = np.loadtxt("4.txt", dtype = float)

t1 = 10.695
t2 = 9.2039
t3 = 14.06
t4 = 18.846
l2 = 1
rl = 5.684

ts = np.array([10.695, 9.2039, 14.06, 18.846])
ns = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])


k1 = m.sqrt(t1/rl)
k2 = m.sqrt(t2/rl)
k3 = m.sqrt(t3/rl)
k4 = m.sqrt(t4/rl)
v1 = ns*k1
v2 = ns*k2
v3 = ns*k3
v4 = ns*k4

plf1 = np.polyfit(ns, n1, 1)
yfit1 = np.polyval(plf1, ns)
plf2 = np.polyfit(ns, n2, 1)
yfit2 = np.polyval(plf2, ns)
plf3 = np.polyfit(ns, n3, 1)
yfit3 = np.polyval(plf3, ns)
plf4 = np.polyfit(ns, n4, 1)
yfit4 = np.polyval(plf4, ns)



fig, ax = plt.subplots(figsize = (13, 8), dpi = 400)

ax.plot(ns, yfit1, c = "black")
ax.scatter(ns, n1)
ax.plot(ns, yfit2, c = "green")
ax.scatter(ns, n2)
ax.plot(ns, yfit3, c = "orange")
ax.scatter(ns, n3)
ax.plot(ns, yfit4, c = "r")
ax.scatter(ns, n4)


plt.ylabel("nu, Hz")
plt.xlabel("n")
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
print(plf1[0],plf2[0],plf3[0],plf4[0])
fig.savefig("g1.png")

u2 = np.array([plf1[0]*plf1[0], plf2[0]*plf2[0], plf3[0]*plf3[0], plf4[0]*plf4[0]])
plfu = np.polyfit(ts, u2, 1)
yfitu = np.polyval(plfu, ts)
fig1, ax1 = plt.subplots(figsize = (13, 8), dpi = 400)
plt.ylabel("u^2, (m/s)^2")
plt.xlabel("T, N")
ax1.scatter(ts, u2, c = 'red')
ax1.plot(ts, yfitu, c = 'black')
ax1.grid(b=True, which='major', color='grey', linestyle='-')
ax1.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig1.savefig("g2.png")

print(plfu[0])