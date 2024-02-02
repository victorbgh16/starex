import calibrate
import plot
from matplotlib import pyplot as plt
import numpy as np

calib_file = r'' + input('Enter path to calibration file: ')

data = calibrate.read_data(calib_file)

peak_height = float(input('Enter peak height here: '))
peak_distance = float(input('Enter peak distance here: '))

peaks = calibrate.find_peaks(data, peak_height, peak_distance)

(indices, heights) = peaks
peaks_x = []
for i in range(0, len(indices)):
    peaks_x.append(data[indices[i]][0])

peaks_y = heights['peak_heights']

print(f'Number of peaks is: {len(indices)}')
print(f'Peak indices are: {indices}')
print(f'Peak x values are: {peaks_x}')
print(f'Peak heights are: {peaks_y}')

plot.plot_graph('Raw Calibration', data[:, 0], data[:, 1])
plt.scatter(peaks_x, peaks_y)
plt.show()

number_peaks = int(input('Enter number of peaks you want to process: '))
peak_indices = calibrate.get_peak_indices(number_peaks)

wavelengths = calibrate.get_wavelengths(number_peaks)

# plt.title = 'Calibration Fit'
# plt.scatter(wavelengths, peaks_x)
# plt.show()


coef = np.polyfit(wavelengths, peaks_x, 1)
poly1d_fn = np.poly1d(coef)

(slope, coeff) = coef
print(f'The slope of the found fit is: {slope}')

plt.plot(wavelengths, peaks_x, 'bo', wavelengths, poly1d_fn(wavelengths), '--r')
plt.show()