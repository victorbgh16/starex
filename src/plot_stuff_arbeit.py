import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('TkAgg')

data = np.genfromtxt('../data/beteigeuze.csv', delimiter=';', skip_header=3)

plt.title("Unkalibriertes Spektrum")
plt.xlabel(r'$\lambda$')
plt.ylabel(r'rel. Intensität')

plt.plot(data[:, 0], data[:, 1], color='green', linewidth=0.7)
plt.show()