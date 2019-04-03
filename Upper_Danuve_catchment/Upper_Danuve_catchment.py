import numpy as np
from utilities import *
import matplotlib.pyplot as plt

"""
loading data, i think this is the hardest part of whole laboratory
"""
opady_prn = open('opady.prn', 'r')
tritium_concentration_precipitation  = extract_values(opady_prn.readlines())

dunaj_prn = open('dunaj.prn', 'r')
tritium_concentration_Dunaj = extract_values(dunaj_prn.readlines())

months = np.arange(1, 630)

plt.plot(months, tritium_concentration_precipitation)
plt.show()

plt.plot(months, tritium_concentration_Dunaj)
plt.show()
