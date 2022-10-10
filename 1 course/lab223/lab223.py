import matplotlib.pyplot as plt
import numpy as np

q = np.array([0.0242788,
0.0972,
2.431272,
38.41552,
132.10408,
233.522,
888.483291])

r = np.array([14.72906404,
14.81481481,
14.8960396,
14.89414695,
14.89590329,
14.90651844,
14.9082242])

plt.subplots(figsize = (8, 6), dpi = 400)
plt.plot(q,r)
plt.grid(b=True, which='major', color='grey', linestyle='-')
plt.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()

plt.savefig("lab223.png")
