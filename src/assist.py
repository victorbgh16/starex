import numpy as np

data = np.genfromtxt('../data/NA Lampe OceanOptics schlecht.csv', delimiter=';')
data_na = np.genfromtxt('../data/na.dat', delimiter=';')
data_ne = np.genfromtxt('../data/neon_spektrum.csv', delimiter=';')
data_na_300_gitter = np.genfromtxt('../data/Na_300_Gitter.csv', delimiter=';')
data_na_vergleich = np.genfromtxt('../data/Na_Doppler_Vergleich_up.csv', delimiter=';')

curr = data[:, 1][0]
for e in data[:, 1]:
    if e > curr:
        curr = e

print(curr)

curr = data_na[:, 1][0]
for e in data_na[:, 1]:
    if e > curr:
        curr = e

print(curr)

curr = data_ne[:, 1][0]
for e in data_ne[:, 1]:
    if e > curr:
        curr = e

print(curr)

curr = data_na_300_gitter[:, 1][0]
for e in data_na_300_gitter[:, 1]:
    if e > curr:
        curr = e

print(curr)

curr = data_na_vergleich[:, 1][0]
for e in data_na_vergleich[:, 1]:
    if e > curr:
        curr = e

print(curr)