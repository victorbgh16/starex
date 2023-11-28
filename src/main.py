from src import calibrate, plot

calib_file = r'' + input('Enter path to calibration file: ')
# calib_file = r'data/Text_Calibration.csv'

data = calibrate.read_data(calib_file)

peak_height = float(input('Enter peak height here: '))

peaks = calibrate.find_peaks(data, peak_height)

print('Peaks are:\n', peaks)

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

plot.plot_raw_calibration(data, peaks)
plot.plot_calibration_data(data, calibrated)