from scipy import signal
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

def integral(C_in, t, integration_par, lamb):
    partial = None
    sum = 0
    dt = 0
    for i in range(t):
        g = distribution_function(t, integration_par)
        partial = C_in * g * math.exp(-lamb)
        sum += partial
    
    C = sum * dt
    return(C)

def distribution_function(t, integration_par):
    #Piston-flow model
    tt = mean_residence_time(integration_par, C)
    signal.unit_impulse(t, ((t - integration_par) - tt))
    return g

def mean_residence_time(integration_par, C):
    tt = None
    return tt