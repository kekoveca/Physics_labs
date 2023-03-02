import numpy as np

data = np.array([9,9,9,8,8,8,10,10,9,9,9,8,9,9,9,8])
print(f'{np.mean(data)} +- {np.std(data)/np.sqrt(len(data)):.2f}')