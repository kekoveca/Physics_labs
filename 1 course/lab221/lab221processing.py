import matplotlib.pyplot as plt
import numpy as np
import math

t45 = np.loadtxt("t45.txt", dtype= float)
t105 = np.loadtxt("t105.txt", dtype= float)
t200 = np.loadtxt("t200.txt", dtype= float)
u45 = np.loadtxt("U45.txt", dtype= float)
u105 = np.loadtxt("U105.txt", dtype= float)
u200 = np.loadtxt("U200.txt", dtype= float)

a = math.log(u45[0]/u45[0])
b = math.log(u105[0]/u105[0])
c = math.log(u200[0]/u200[0])

for i in range(1, len(u45)):
    u45[i] = math.log(u45[i]/u45[0])

for i in range(1, len(u105)):
    u105[i] = math.log(u105[i]/u105[0])

for i in range(1, len(u200)):
    u200[i] = math.log((u200[i])/u200[0])

u45[0] = a
u105[0] = b
u200[0] = c

plf1 = np.polyfit(t45, u45, 1)
plf2 = np.polyfit(t105, u105, 1)
plf3 = np.polyfit(t200, u200, 1)

u1 = np.polyval(plf1, t45)
u2 = np.polyval(plf2, t105)
u3 = np.polyval(plf3, t200)

uu1 = -plf1[0]
uu2 = -plf2[0]
uu3 = -plf3[0]
np.savetxt("plfs.txt", [uu1, uu2, uu3])

np.savetxt("y1.txt", u45)
np.savetxt("y2.txt", u105)
np.savetxt("y4.txt", u200)

np.savetxt("f1.txt", u1)
np.savetxt("f2.txt", u2)
np.savetxt("f3.txt", u3)

ls = 9
v = 420
d1 = uu1*420*9/2 
d2 = uu2*420*9/2
d3 = uu3*420*9/2
print(d1, d2, d3)

ps = [760/(45.73), 760/106.68, 760/213.36]

leg1 = str("1/τ = {:.6f}".format(-plf1[0]))
leg2 = str("1/τ = {:.6f}".format(-plf2[0]))
leg3 = str("1/τ = {:.6f}".format(-plf3[0]))

plt.subplots(figsize = (8, 6), dpi = 400)
plt.plot(t45, u45, c = 'black', lw = 1, label = "45.73 Torr ")
plt.plot(t105, u105, c = 'black', lw = 1, label = "106.68 Torr ")
plt.plot(t200, u200, c = 'black', lw = 1, label = "213.36 Torr ")
plt.plot(t45, u1, linestyle = '--' , c = 'lime', label = leg1)
plt.plot(t105, u2, linestyle = '--' , c = 'purple', label = leg2)
plt.plot(t200, u3, linestyle = '--' , c = 'orange', label = leg3)

#plt.xlim([8, 260])
plt.ylim([-1.2, 0.2])
plt.ylabel("Ln(U/U0)")
plt.xlabel("Time, seconds")
plt.title("Ln(U/U0)(t)")
plt.legend()
plt.grid(b=True, which='major', color='grey', linestyle='-')
plt.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()

plt.savefig("first.png")

plfd2 = np.polyfit(ps, [d1, d2, d3], 1)
dfit = np.polyval(plfd2, ps)
atm = str("D0 = {:.6f} ".format(np.polyval(plfd2, 1)))

plt.subplots(figsize = (8, 6), dpi = 400)
plt.scatter(ps, [d1, d2, d3], c = 'black')
plt.plot(ps, dfit, c = 'black', label = atm)
plt.ylabel("D, sm^2/s")
plt.xlabel("1/P, atmospheres")
plt.legend()
plt.grid(b=True, which='major', color='grey', linestyle='-')
plt.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()

plt.savefig("second.png")


