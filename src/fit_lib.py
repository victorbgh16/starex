import numpy as np

def calculate_fit(x, y, deg):
    coef = np.polyfit(x, y, deg)
    poly1d_fn = np.poly1d(coef)

    return coef, poly1d_fn


def get_slope(coef):
    (slope, coeff) = coef
    return slope