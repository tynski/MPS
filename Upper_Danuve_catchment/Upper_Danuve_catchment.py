import numpy as np
from extract import extract_values

"""
loading data, i think this is the hardest part of whole laboratory
"""
opady_prn = open('opady.prn', 'r')
records_opady  = extract_values(opady_prn.readlines())

dunaj_prn = open('dunaj.prn', 'r')
records_dunaj = extract_values(dunaj_prn.readlines())

    



