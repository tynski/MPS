import numpy as np
import math

def extract_values(data):
    records = []
    record = None
    for x in data:
        value = ''
        for i in range(len(x) - 2, 0,-1):
            if x[i] == ' ':
                break
            value += x[i]
        record = float(value[::-1]) #reverse string and cast into float
        records.append(record)
    return records

def driac(x):
    if x <= 1e-4:
        return 1
    return 0

def integral(C_in, t, tt):
    partial = 0
    dt = 1
    decay = math.log(2) / (12.32 * 12) #labmda

    for ti in range(t):
        g = distribution_function(t, ti, tt)
        partial += C_in[ti] * g * math.exp(-decay*(t - ti))
    
    C = partial * dt
    return(C)

def distribution_function(t, ti, tt):
    model = 'Piston'

    #Piston-flow model
    if(model == 'Piston'):
        g = driac((t - ti) - tt) #now impuls is 1, should it be inf?

    #Exponential model
    if(model == 'Exp'):
        g = np.exp(-(t-ti)/tt) / tt

    return g
