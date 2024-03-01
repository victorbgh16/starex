import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import calibrate
matplotlib.use('TkAgg')
# plt.style.use('dark_background')

# data = np.genfromtxt('../data/calib.csv', delimiter=';', skip_header=3)
data = np.genfromtxt('../data/NA Lampe OceanOptics schlecht.csv', delimiter=';')
data_na = np.genfromtxt('../data/na.dat', delimiter=';')

plt.rcParams.update({'font.size': 30})

plt.title("Kalibrationsspektrum")
plt.xlabel(r'Wellenlänge [nm]')
plt.ylabel(r'rel. Intensität [%]')
# data[:, 1] = data[:, 1] * 875.46

data_na[:, 1] = data_na[:, 1] / 875.46
# data[:, 1] = data[:, 1] / 800


# plt.plot(data[:, 0], data[:, 1], color='#09AD00', linewidth=2.5)
plt.plot(data_na[:, 0], data_na[:, 1], color='#09AD00', linewidth=2.2)
plt.show()
