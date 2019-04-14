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

print("Please select transit functions by picking one of numbers:\n \
       1. Piston-flow model.\n \
       2. Exponential model. \n \
       3. Dispersion model. \n")

model = int(input())

N = len(C_in)
C_out = np.zeros(N)
RMSE = 0
best_RMSE = math.inf
TT = [30]
best_tt = None

for tt in TT:
    for t in month:
        if(ground_truth[t] == 0):
            C_out[t] = 0
        else:
            C_out[t] = integral(C_in, t, tt, model)

    RMSE = np.sqrt(np.sum(np.square(ground_truth - C_out)) / N)
    if RMSE < best_RMSE:
        best_RMSE = RMSE
        best_tt = tt


for t in month:
    if(ground_truth[t] == 0):
            C_out[t] = 0
    else:
        C_out[t] = integral(C_in, t, best_tt, model)


plt.plot(month, ground_truth, label = 'ground truth')
plt.plot(month, C_out, label = 'model')
plt.title('Comparison model results with given data, tt = %1.1f' %best_tt)
plt.xlabel('month')
plt.ylabel('C')
plt.legend()    
plt.show()
print(best_RMSE)
print(best_tt)


