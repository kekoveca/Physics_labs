import matplotlib.pyplot as plt
import numpy as np
import math


n1decr = np.loadtxt("n1decr.txt", dtype = float)
n1incr = np.loadtxt("n1incr.txt", dtype = float)
n2decr = np.loadtxt("n2decr.txt", dtype = float)
n2incr = np.loadtxt("n2incr.txt", dtype = float)
t1decr = np.loadtxt("t1decr.txt", dtype = float)
t1incr = np.loadtxt("t1incr.txt", dtype = float)
t2incr = np.loadtxt("t2incr.txt", dtype = float)
t2decr = np.loadtxt("t2decr.txt", dtype = float)

t2decr = t2decr - 91

P_ust = 0.00011
P_lim = 0.000072
P_fv = 0.0011
v = 1.303537


plf1 = np.polyfit(t1incr, n1incr, 1)
line1  = np.polyval(plf1, t1incr)

plf2 = np.polyfit(t2incr, n2incr, 1)
line2  = np.polyval(plf2, t2incr)

for i in range(len(line1)):
    diff1 = (line1[i] - n1incr[i])**2

for i in range(len(line2)):
    diff2 = (line2[i] - n2incr[i])**2

err1 = str(f"Deviation is {np.sqrt(np.sum(diff1)/(len(line1)+1))}, k = {plf1[0]}")
err2 = str(f"Deviation is {np.sqrt(np.sum(diff2)/(len(line2)+1))}, k = {plf2[0]}")

plt.subplots(figsize = (8, 6), dpi = 400)
plt.plot(t1incr, line1, c = 'green', lw = 1, label = err1)
plt.plot(t2incr, line2, c = 'black', lw = 1, label = err2)
plt.plot(t1incr, n1incr, c = 'green', lw = 1, linestyle = '--')
plt.plot(t2incr, n2incr, c = 'black', lw = 1, linestyle = '--')

plt.ylabel("P, torrs")
plt.xlabel("Time, seconds")
plt.title("Increasing of pressure")
plt.legend()
plt.grid(visible = True, which='major', color='grey', linestyle='-')
plt.grid(visible = True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()

plt.savefig("231graph1.png")



ln1decr = np.log((n1decr - P_lim)/n1decr[0])
ln2decr = np.log((n2decr - P_lim)/n2decr[0])

plfln1 = np.polyfit(t1decr, ln1decr, 1)
ln1 = np.polyval(plfln1, t1decr)

plfln2 = np.polyfit(t2decr, ln2decr, 1)
ln2 = np.polyval(plfln2, t2decr)

for i in range(len(ln1)):
    diffln1 = (ln1[i] - ln1decr[i])**2

for i in range(len(ln2)):
    diffln2 = (ln2[i] - ln2decr[i])**2

err1ln = str(f"Deviation is {(np.sqrt(np.sum(diffln1)/(len(ln1)+1))):.4f}, k = {(plfln1[0]):.4f}")

err2ln = str(f"Deviation is {(np.sqrt(np.sum(diffln2)/(len(ln2)+1))):.4f}, k = {(plfln2[0]):.4f}")

plt.subplots(figsize = (8, 6), dpi = 400)
plt.plot(t1decr, ln1, c = 'green', lw = 1, label = err1ln)
plt.plot(t1decr, ln1decr, c = 'green', lw = 1, linestyle = '--')

plt.plot(t2decr, ln2, c = 'black', lw = 1, label = err2ln)
plt.plot(t2decr, ln2decr, c = 'black', lw = 1, linestyle = '--')

plt.ylabel("log(P - P_lim/P_0), torrs")
plt.xlabel("Time, seconds")
plt.title("Decreasing of pressure")
plt.legend()
plt.grid(visible = True, which='major', color='grey', linestyle='-')
plt.grid(visible = True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()

plt.savefig("231graph2.png")

kln = np.mean([plfln1[0], plfln2[0]])
k = np.mean([plf1[0], plf2[0]])

W = -kln*v
print("W = ", W, " Л/c")

Q = v*k
print("Qн + Qд = ", Q, " торр*Л/c")

C = (4/3) * ((0.025**3)/(0.5))*np.sqrt((2*3.14*8.31*300)/(0.029)) * 1000
print("C = ", C, " Л/c")

kap = (4/3) * (0.0008**3)*np.sqrt((2*3.14*8.31*300)/(0.029))*(0.0011 - 0.00011)/0.108 * 1000
print("d(PV)/t = ",kap, " торр*Л/c")

W1 = kap/(0.00011 - P_lim)
print("W1 = ", W1, " Л/c")

sig = np.sqrt(2*(0.1/15.6)**2) * v
print(sig) 

sig1 = np.sqrt((sig/v)**2 + ((np.mean([np.sqrt(np.sum(diff1)/(len(line1)+1)), np.sqrt(np.sum(diff2)/(len(line2)+1))]))/k)**2)
sigln = np.mean([np.sqrt(np.sum(diffln1)/(len(ln1)+1)), np.sqrt(np.sum(diffln2)/(len(ln2)+1))])/kln

qsig = (P_lim*W - Q)*sig1
wsig = -W*sigln

print(wsig)
print(qsig)

print(P_lim*W - Q)
print(1.046*10**(-5)*4/11)