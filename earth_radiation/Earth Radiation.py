import math
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import seaborn

##################################
# First part: calculating mean temperature on the Surface without atmosphere.

# Constants necessary for simulation
albedo_mean = 0.3  # Mean Albedo
solar_const = 1366  # Solar constant
sigma = 5.67 * 1e-8  # Stefan_Boltzmann constant as sigma

T_without_a = (solar_const * (1.0 - albedo_mean) / (4 * sigma))**(.25)
print('Mean temperature of the suface witout atmosphere effect: %.3f K.' % T_without_a)

##################################
# Second part: calculating mean temperature on the Surface with atmoshpere

# short wave radiation
t_a_short = 0.53
albedo_s = 0.19
albedo_a_short = 0.3

# long wage radiation
t_a_long = 0.06
albedo_a_long = 0.31

# constant c
c = 2.7

# Solving the non-linear equation of energy Balance Equation (WITH Atmosphere).
#  Model for mean T of atmosphere and mean T of surface.


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


T_a = fsolve(model, [0, 0])[1]
print('Mean temperature of the sufrace with atmosphere effect: %.3f K.' % T_a)
print('Absolute difference between mean T with and without atmoshpere: %.3f K.' % abs(T_a - T_without_a))

solar_ratio = np.arange(0.6, 1.3, 0.01)
solar_range = solar_const * solar_ratio

T_with_a = []
for solar_const in solar_range:
    T_with_a.append(fsolve(model, [0, 0])[1])

seaborn.scatterplot(T_with_a, solar_ratio)
plt.xlabel('Mean Temperature [K]')
plt.ylabel('Solar constant ratio')
plt.grid()
plt.show()

################################################
# Glaciation mechanism

Tc = 263  # Critical Temperature

T_glac_inc = []
T_glac_dec = []

solar_ratio = np.arange(0.5, 1.5, 0.01)
solar_range = solar_const * solar_ratio
albedo_range = np.arange(0.19, 0.65, 0.1)

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

seaborn.scatterplot(solar_ratio, T_glac_inc, label='increasing albedo')
seaborn.scatterplot(solar_ratio, T_glac_dec, label='deacresing albedo')
plt.ylabel('Mean Temperature [K]')
plt.xlabel('Solar constant ratio')
plt.grid()
plt.legend()
plt.show()
