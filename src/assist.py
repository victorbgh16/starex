import numpy as np

data = np.genfromtxt('../data/NA Lampe OceanOptics schlecht.csv', delimiter=';')
data_na = np.genfromtxt('../data/na.dat', delimiter=';')

curr = data[:, 1][0]
for e in data[:, 1]:
    if e > curr:
        curr = e

print(curr)

curr_1 = data_na[:, 1][0]
for e in data_na[:, 1]:
    if e > curr_1:
        curr_1 = e

print(curr_1)
