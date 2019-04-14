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

def disper(t, ti, tt):
    pe = 5.2
    sqrt = np.sqrt((4 * math.pi * pe * (t - ti)) / tt)
    exp = np.exp( (-1) * np.square((1.0 - (t - ti)) / tt) / (4 * pe * (t - ti) / tt))
    disp = np.reciprocal(sqrt) * np.reciprocal(t - ti) * exp
    return disp

def integral(C_in, t, tt, model):
    partial = 0
    dt = 1
    decay = math.log(2) / (12.32 * 12) #labmda

    for ti in range(t):
        g = tranist_func(t, ti, tt, model)
        partial += C_in[ti] * g * math.exp(-decay*(t - ti))
    
    C = partial * dt
    return(C)

def tranist_func(t, ti, tt, model):
    #Piston-flow model
    if(model == 1):
        g = driac((t - ti) - tt) #now impuls is 1, should it be inf?
    #Exponential model
    elif(model == 2):
        g = np.exp(-(t-ti)/tt) / tt
    elif(model == 3):
        g = disper(t, ti, tt)

    return g
