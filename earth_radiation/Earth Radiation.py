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

A = 0.3
S = 1366  # W/m2
sigma = 5.67 * 1e-8  # W/m2K4
R = 6.371 * 1e3  # m

# short wave radiation
t_a = 0.53
a_s = 0.11
a_a = 0.3
# long wage radiation
t_A = 0.6
a_A = 0.31

c = 2.7  # Wm-2K-1

# without atmosphere
T1 = (S * (1 - A) / (4 * sigma))**(.25)
print('Mean temperature on the suface witout atmosphere effect: %.3f' % T1)

# model for Ta and Ts with atmosphere


def model(t):
    T_a = t[0]
    T_s = t[1]

    F = np.zeros((2,))
    a0 = (-1) * t_a * (1 - a_s) * S / 4
    a1 = sigma * (1 - a_A)
    F[0] = a0 + c * (T_s - T_a) + a1 * T_s**4 - sigma * T_a**4
    b0 = (-1) * (1 - a_a - t_a + a_s * t_a) * S / 4
    b1 = sigma * (1 - t_A - a_A)
    F[1] = b0 - c * (T_s - T_a) - b1 * T_s**4 + 2 * sigma * T_a**4

    return F


T2 = fsolve(model, [0, 0])[1]
print('Means temperature on the sufrace with atmosphere effect: %.3f' % T2)
print('Difference: %.3f' % abs(T2 - T1))

S_range = S * np.arange(0.8, 1.2, 0.01)

T2 = []
for S in S_range:
    T2.append(fsolve(model, [0, 0])[1])

fig, axes = plt.subplots(1, 2)
seaborn.scatterplot(S_range, T2, ax=axes[0])

T_glac = []
a_range = np.arange(0.19, 0.65, 0.01)
for a_a in a_range:
    T_glac.append(fsolve(model, [0, 0])[1])

seaborn.scatterplot(a_range, T_glac, ax=axes[1])
plt.show()
