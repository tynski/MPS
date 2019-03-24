# Pow - sphere surface = 4 * pi * R^2
# Albedo - ratio reflected energy to incoming enery
#
# Solar switching consant for both points, two cases increasering as and deacresing albido as:
# as 0.19 -> 0.65
#
# Ts < (Tc = (-10C) critical temp)
#
# #1 Calculation for no atmosferic,
# #2 amosfere and compare
# #3 solar constant scenarios, glaciations mechanism
#
# plot solar range vs mean temp

import math
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import seaborn

albedo_mean = 0.3
solar_const = 1366  # W/m2
sigma = 5.67 * 1e-8  # W/m2K4
R = 6.371 * 1e3  # m
Tc = 263

# short wave radiation
t_a_short = 0.53
albedo_s = 0.19
albedo_a_short = 0.3

# long wage radiation
t_a_long = 0.06
albedo_a_long = 0.31

# just c XO
c = 2.7  # Wm-2K-1

# without atmosphere
T_without_a = (solar_const * (1 - albedo_mean) / (4 * sigma))**(.25)
print('Mean temperature on the suface witout atmosphere effect: %.3f' % T_without_a)

# model for Ta and Ts with atmosphere


def model(t):
    T_a = t[0]
    T_s = t[1]

    F = np.zeros((2,))
    a0 = (-1) * t_a_short * (1 - albedo_s) * solar_const / 4
    a1 = sigma * (1 - albedo_a_long)
    F[0] = a0 + c * (T_s - T_a) + a1 * T_s**4 - sigma * T_a**4
    b0 = (-1) * (1 - albedo_a_short - t_a_short + albedo_s * t_a_short) * solar_const / 4
    b1 = sigma * (1 - t_a_long - albedo_a_long)
    F[1] = b0 - c * (T_s - T_a) - b1 * T_s**4 + 2 * sigma * T_a**4

    return F


T2 = fsolve(model, [0, 0])[1]
print('Means temperature on the sufrace with atmosphere effect: %.3f' % T2)
print('Difference: %.3f' % abs(T2 - T_without_a))

solar_range = solar_const * np.arange(0.6, 1.3, 0.01)
albedo_range = np.arange(0.19, 0.65, 0.01)

# normal enviroment
T_with_a = []
for solar_const in solar_range:
    T_with_a.append(fsolve(model, [0, 0])[1])

T_glac_inc = []
T_glac_dec = []

# increasing albedo
for solar_const in solar_range:
    for albedo_a_short in albedo_range:
        temp = fsolve(model, [0, 0])[1]
        if temp < Tc:
            break

    T_glac_inc.append(temp)

# decreasing albedo
for solar_const in solar_range:
    for albedo_a_short in reversed(albedo_range):
        temp = fsolve(model, [0, 0])[1]
        if temp < Tc:
            break

    T_glac_dec.append(temp)

"""
for solar_const in solar_range:
    temp = fsolve(model, [0, 0])[1]
    if temp < Tc:
        albedo_s = 0.65

    T_glac_inc.append(temp)

for solar_const in solar_range:
    temp = fsolve(model, [0, 0])[1]
    if temp < Tc:
        albedo_s = 0.19

    T_glac_dec.append(temp)
"""
fig, axes = plt.subplots(1, 2)
seaborn.scatterplot(solar_range, T_with_a, ax=axes[0])
seaborn.scatterplot(solar_range, T_glac_inc, ax=axes[1])

#solar_fraction = int()
seaborn.scatterplot(solar_range, T_glac_dec, ax=axes[1])
plt.show()
