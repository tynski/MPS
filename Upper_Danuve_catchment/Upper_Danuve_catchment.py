import numpy as np
from utilities import *
import matplotlib.pyplot as plt

"""
loading data, i think this is the hardest part of whole laboratory
"""
opady_prn = open('opady.prn', 'r')
C_in  = extract_values(opady_prn.readlines())

dunaj_prn = open('dunaj.prn', 'r')
ground_truth = extract_values(dunaj_prn.readlines())

month = np.arange(0, 629)

plt.plot(month, C_in)
plt.show()

N = len(C_in)
C_out = np.zeros(N)
MSE = 0
best_MSE = math.inf
#TT = np.arange(15.0,25.0) Piston
TT = np.arange(1.0, 10.0)
best_tt = None

for tt in TT:
    for t in month:
        if(ground_truth[t] == 0):
            C_out[t] = 0
        else:
            C_out[t] = integral(C_in, t, tt)

    MSE = np.sum(np.square(ground_truth - C_out)) / N
    if MSE < best_MSE:
        best_MSE = MSE
        best_tt = tt


for t in month:
    if(ground_truth[t] == 0):
            C_out[t] = 0
    else:
        C_out[t] = integral(C_in, t, best_tt)


plt.plot(month, ground_truth)
plt.plot(month, C_out)
plt.show()
print(best_MSE)
print(best_tt)


