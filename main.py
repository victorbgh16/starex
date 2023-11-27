import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy.signal
from scipy import signal
# matplotlib.use('TkAgg')

def iterative_mean(inp: list) -> float:
    total = 0.0
    for i in range(0, len(inp)):
        total = total + ((inp[i] - total) / (i + 1))
    return total

#calib_file = input("Input Calibration Data File:")

calib_file = r"Text_Calibration"
    #r"C:\Users\Simon\Desktop\SharpCap Captures\2023-11-24\Capture\19_16_30\Text_Calibration2"
    #r"C:\Users\Simon\Desktop\SharpCap Captures\2023-11-05\Capture\21_12_53\Neon_Calibrator_V1"


data = np.genfromtxt(calib_file, delimiter=";", skip_header=3)
peak_height = 0.5
peaks = scipy.signal.find_peaks(data[:, 1], height=peak_height)


print("Peaks:")
print(peaks)
print("Peak 2 must be after peak 1")
no_peaks = int(input("Enter number of peaks you want to process: "))

peaks_indices = []
for i in range(1, no_peaks+1):
    # peak1_index = int(input("Enter index of peak 1: "))
    # peak2_index = int(input("Enter index of peak 2: "))

    peaks_indices.append(int(input(f"Enter index of peak {i}: ")))

peak_distances = []
for i in range(0, len(peaks_indices)):
    if i+1 < len(peaks_indices):
        peak_distances.append(data[peaks[0][peaks_indices[i+1]], 0] - data[peaks[0][peaks_indices[i]], 0])


# peak_distance = data[peaks[0][peak2_index], 0] - data[peaks[0][peak1_index], 0]
# print("Peak distance of ", peak_distance)

print(f"Peak distances are: {peak_distances}")

print("--------------------------------------")

# wavelength_1 = float(input("Enter wavelength of peak 1:"))
# wavelength_2 = float(input("Enter wavelength of peak 2:"))

wavelengths = []
for i in range(1, no_peaks+1):
    # peak1_index = int(input("Enter index of peak 1: "))
    # peak2_index = int(input("Enter index of peak 2: "))

    wavelengths.append(int(input(f"Enter wavelength of peak {i}: ")))

wavelength_distances = []
for i in range(0, len(wavelengths)):
    if i+1 < len(wavelengths):
        wavelength_distances.append(wavelengths[i+1] - wavelengths[i])

print(f"Wavelength distances are: {wavelength_distances}")

print("--------------------------------------")

wavelengths_per_x = [x/peak_distances[ind] for ind, x in enumerate(wavelength_distances)]
# print("nm per x unit: ", wavelength_per_x)
# print("Offset in nm: ", wavelength_1)

average = iterative_mean(wavelengths_per_x)

#####
calibrated = ((data[:, 0] - data[peaks[0][0], 0]) * average) + wavelengths[0]


plt.plot(data[:, 0], data[:, 1])
plt.title("Raw Calibration")
plt.scatter(data[peaks[0], 0], data[peaks[0], 1])
plt.show()

plt.figure()
plt.title("Calibration Data")
plt.plot(calibrated, data[:, 1])
plt.xlabel(r"$\lambda$ nm")
plt.ylabel(r"$\sigma$")
plt.show()

#####
#data_file = input("Input Data File:")

data_file = r"C:\Users\Simon\Desktop\SharpCap Captures\2023-11-24\Capture\22_46_20\Text_Quecksilber_Test"
    #r"C:\Users\Simon\Desktop\SharpCap Captures\2023-11-24\Capture\19_16_30\Text_Natrium_Dampflampe"

real_data = np.genfromtxt(data_file, delimiter=";", skip_header=3)

calibrated_real_data = ((real_data[:, 0]) * wavelength_per_x) + wavelength_1
plt.figure()
plt.title("Calibrated Data")
plt.plot(calibrated_real_data, real_data[:, 1], label="plot 1")
plt.xlabel(r"$\lambda$ nm")
plt.ylabel(r"$\sigma$")
plt.show()


plt.figure()
plt.title("Calibrated Data")
plt.plot(calibrated_real_data, real_data[:, 1])
plt.xlabel(r"$\lambda$ nm")
plt.ylabel(r"$\sigma$")
plt.show()


#np.save("out", calibrated)

#neon = np.load("out.npy")