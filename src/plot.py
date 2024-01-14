import matplotlib.pyplot as plt


def plot_raw_calibration(data, peaks):
    plt.title('Raw Calibration')

    plt.plot(data[:, 0], data[:, 1])

    plt.scatter(data[peaks[0], 0], data[peaks[0], 1])

    plt.show()


def plot_calibration_data(data, calibrated):
    plt.figure()
    plt.title('Calibration Data')
    plt.xlabel(r'$\lambda$ nm')
    plt.ylabel(r'$\sigma$')

    plt.plot(calibrated, data[:, 1])

    plt.show()


def plot_graph(title, x, y, xlabel='', ylabel='', linewidth=1):
    plt.title(title)
    plt.xlabel(r'' + xlabel)
    plt.ylabel(r'' + ylabel)

    plt.plot(x, y, linewidth=linewidth)
