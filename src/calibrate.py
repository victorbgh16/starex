from typing import Any

import numpy as np
import scipy


def read_data(file):
    return np.genfromtxt(file, delimiter=';', skip_header=3)


def find_peaks(data, peak_height):
    return scipy.signal.find_peaks(data[:, 1], height=peak_height)


def get_peak_indices(number_peaks):
    peaks_indices = []

    for i in range(1, number_peaks+1):
        peaks_indices.append(int(input(f'Enter index of peak {i}: ')))

    return peaks_indices


def generate_peak_distances(data, peaks, peak_indices):
    peak_distances = []

    for i in range(0, len(peak_indices)):
        if i + 1 < len(peak_indices):
            peak_distances.append(data[peaks[0][peak_indices[i + 1]], 0] - data[peaks[0][peak_indices[i]], 0])

    return peak_distances


def get_wavelengths(number_peaks):
    wavelengths = []

    for i in range(1, number_peaks + 1):
        wavelengths.append(float(input(f'Enter wavelength of peak {i}: ')))

    return wavelengths


def generate_wavelength_distances(wavelengths):
    wavelength_distances = []

    for i in range(0, len(wavelengths)):
        if i + 1 < len(wavelengths):
            wavelength_distances.append(wavelengths[i + 1] - wavelengths[i])

    return wavelength_distances


def calculate_wavelengths_per_x(peak_distances, wavelength_distances):
    return [x / peak_distances[ind] for ind, x in enumerate(wavelength_distances)]


def iterative_mean(inp: list) -> float:
    total = 0.0
    for i in range(0, len(inp)):
        total = total + ((inp[i] - total) / (i + 1))
    return total


def calibrate(data, peaks, wavelengths, average):
    return ((data[:, 0] - data[peaks[0][0], 0]) * average) + wavelengths[0]


def calibrate_real_data(data, wavelengths, average):
    return ((data[:, 0]) * average) + wavelengths[0]