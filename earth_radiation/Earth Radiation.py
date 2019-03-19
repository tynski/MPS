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

A=0.3
S=1366 #W/m2 
sigma=5.67*1e-8 #W/m2K4
R  = 6.371*1e3 #m
T = 255.9 #K

#short wave radiation
t_a = 0.53
a_s = 0.11
a_a = 0.3
#long wage radiation
t_A = 0.6
a_A = 0.31

c = 2.7 #Wm-2K-1

# without atmosphere
Powz = 4*math.pi*R**4 
Psi = S*Powz/4*(1-A)
Pz = sigma*T**4*Powz
print(Powz - Pz)
T = (S*(1-A)/(4*sigma))**(.25)
print(T)

# model for Ta and Ts with atmosphere
def model(t):
    T_a = t[0]
    T_s = t[1]
    
    F = np.zeros((2,))
    a0 = (-1) * t_a * (1 - a_s) * s / 4
    a1 = sigma * (1 - a_A)
    F[0] = a0 + c*(T_s-T_a) + a1 * T_s**4 -sigma * T_a**4
    b0 = (-1) * (1 - a_a - t_a + a_s * t_a) * s / 4
    b1 = sigma * (1-t_A-a_A)
    F[1] = b0 - c * (T_s - T_a) - b1 * T_s**4 + 2 * sigma * T_a**4
    
    return F

s = S
print(np.mean(fsolve(model, [0,0])))

S_range = S * np.arange(0.8, 1.2, 0.01)

T2 = []
for s in S_range:
    T2.append(np.mean(fsolve(model, [0,0])))

seaborn.scatterplot(S_range, T2)

s = S

