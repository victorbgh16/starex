import matplotlib
import matplotlib.pyplot as plt
from src import calibrate, plot
matplotlib.use('TkAgg')

calib_file = r'' + input('Enter path to calibration file: ')
# calib_file = r'data/calib.csv'

data = calibrate.read_data(calib_file)

peak_height = float(input('Enter peak height here: '))

peaks = calibrate.find_peaks(data, peak_height)

# print('Peaks are:\n', peaks)

(indices, heights) = peaks
peaks_x = []
for i in range(0, len(indices)):
    peaks_x.append(data[indices[i]][0])

peaks_y = heights['peak_heights']

print(f'Peak indices are: {indices}')
print(f'Peak x values are: {peaks_x}')
print(f'Peak heights are: {peaks_y}')

print('Peak 1 must be before peak 2 and so on\n')

number_peaks = int(input('Enter number of peaks you want to process: '))
peak_indices = calibrate.get_peak_indices(number_peaks)
peak_distances = calibrate.generate_peak_distances(data, peaks, peak_indices)

print(f'Peak distances are: {peak_distances}')
print('--------------------------------------')

wavelengths = calibrate.get_wavelengths(number_peaks)
wavelength_distances = calibrate.generate_wavelength_distances(wavelengths)

print(f'Wavelength distances are: {wavelength_distances}')
print('--------------------------------------')

wavelengths_per_x = calibrate.calculate_wavelengths_per_x(peak_distances, wavelength_distances)

average = calibrate.iterative_mean(wavelengths_per_x)

calibrated = calibrate.calibrate(data, peaks, wavelengths, average)
offset = calibrate.calculate_offset(data, peaks, wavelengths, average)

# plot.plot_raw_calibration(data, peaks)
# plot.plot_calibration_data(data, calibrated)

plot.plot_graph('Raw Calibration', data[:, 0], data[:, 1])
plt.scatter(peaks_x, peaks_y)
# plt.show()

plt.figure()
plot.plot_graph('Calibration Data', calibrated, data[:, 1], r'$\lambda$ nm', r'$\sigma$')
# plt.show()

# ---------------------------------------------------------------------------------------------------------------------

data_file = r'' + input('Enter path to data/measurement file: ')

real_data = calibrate.read_data(data_file)

calibrated_real_data = ((real_data[:, 0]) * average) + offset

plt.figure()
plot.plot_graph('Calibrated Data', calibrated_real_data, real_data[:, 1], r'$\lambda\,$nm', r'$\sigma')
plt.show()
