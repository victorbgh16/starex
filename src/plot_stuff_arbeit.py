import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import calibrate
matplotlib.use('TkAgg')
# plt.style.use('dark_background')

# data = np.genfromtxt('../data/calib.csv', delimiter=';', skip_header=3)
data = np.genfromtxt('../data/na_lampe_supi_dupi.csv', delimiter=';')
data_na = np.genfromtxt('../data/na.dat', delimiter=';')
data_ne = np.genfromtxt('../data/neon_spektrum.csv', delimiter=';')
data_unkal = np.genfromtxt('../data/betaigeuze_text.csv', delimiter=';')
data_ne_plakat = np.genfromtxt('../data/calib.csv', delimiter=';')
data_na_300_gitter = np.genfromtxt('../data/Na_300_Gitter.csv', delimiter=';')
data_na_vergleich = np.genfromtxt('../data/Na_Doppler_Vergleich_up.csv', delimiter=';')

plt.rcParams.update({'font.size': 27})

plt.title("Star'æx mit 2400 L/mm")
plt.xlabel(r'Wellenlänge [nm]')
plt.ylabel(r'rel. Intensität [%]')
# data[:, 1] = data[:, 1] * 875.46

data_na[:, 1] /= 875.46
data[:, 1] *= 1.02880658436214
data_ne[:, 1] /= 403.06
data_unkal[:, 0] *= 1.05967484725052
data_na_300_gitter[:, 1] /= 3986.810
data_na_vergleich[:, 1] /= 2694.89

peaks = calibrate.find_peaks(data_ne_plakat, 0.025, 100)

(indices, heights) = peaks
peaks_x = []
for i in range(0, len(indices)):
    peaks_x.append(data_ne_plakat[indices[i]][0])

peaks_y = heights['peak_heights']


# plt.plot(data[:, 0], data[:, 1], color='red', linewidth=2.5, label='Laborspektrometer')
# plt.plot(data_na[:, 0], data_na[:, 1], color='#09AD00', linewidth=2.2, label="Star'æx")
# plt.plot(data_ne[:, 0], data_ne[:, 1], color='#09AD00', linewidth=2.2)
# plt.plot(data_unkal[:, 0], data_unkal[:, 1], color='#09AD00', linewidth=2)
# plt.plot(data_ne_plakat[:, 0], data_ne_plakat[:, 1], color='#09AD00', linewidth=2)
# plt.scatter(peaks_x, peaks_y, color='#09AD00', s=75)
# plt.plot(data_na_300_gitter[:, 0], data_na_300_gitter[:, 1], color='#09AD00', linewidth=1.5)
plt.plot(data_na_vergleich[:, 0], data_na_vergleich[:, 1], color='#09AD00', linewidth=1.5)


# plt.legend(loc="upper right")
plt.show()
