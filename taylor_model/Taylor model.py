import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# set size for plots
plt.rcParams['figure.figsize'] = (14.0, 8.0)

# Parameters of the physical object:
l = 100 #length
w = 5 #width
d = 1  # depth

mean_flow_velocity = 0.1
dispersion_coefficient = 0.01
injection_point = 10
measurement_point = 90
amount_of_injected_tracer = 1

# input values
dx = 1e-1
dt = 1e-1
t_sim = 1000
nx = int(l / dx)
nt = int(t_sim / dt)

ca = mean_flow_velocity * dt / dx
cd = dispersion_coefficient * dt / np.square(dx)

#QUICKEST method
def quickest(c, c_r, c_l, c_ll):
    a0 = (cd * (1 - ca) - (ca / 6) * (np.square(ca) - 3 * ca + 2))
    a1 = (cd * (2 - 3 * ca) - (ca / 2) * (np.square(ca) - 2 * ca - 1))
    a2 = (cd * (1 - 3 * ca) - (ca / 2) * (np.square(ca) - ca - 2))
    a3 = (cd * ca + (ca / 6) * (np.square(ca) - 1))
    c_next = c + a0 * c_r - a1 * c + a2 * c_l + a3 * c_ll
    return c_next


# first boundary condition
c = np.zeros(nx)
# second boundary condtion
injection_point = int(injection_point / dx)
c0 = amount_of_injected_tracer / (w * d * dx)
c[injection_point] = c0

xm = int(measurement_point / dx)
flow_sum = 0
x = np.arange(0, nx)
t = np.arange(0, nt)
sum_c = []
measure_c = []

for i in t:
    for j in range(2, nx - 2):
        c[j] = quickest(c[j], c[j + 1], c[j - 1], c[j - 2])
    c[nx - 1] = c[nx - 2]  # right side-von Neumanncondition
    measure_c.append(c[xm])
    sum_c.append(sum(c))
    if i in list(range(1000, 10000, 1000)):
        plt.plot(x, c, label = 't = ' + str(i) + ' [s]')

plt.xlabel('Coordinate of the simulation node on the river [m]')
plt.ylabel('Concentration value in [kg/m3]')
plt.title('Spatial concentration in the river')
plt.legend()
plt.show()

plt.plot(t, measure_c)
plt.xlabel('time [s]')
plt.ylabel('Concentration value in [kg/m3]')
plt.title('Concentration distribution along simulation in ')
plt.show()

plt.plot(t, sum_c)
plt.xlabel('time [s]')
plt.ylabel('total mass of the tracer')
plt.title('Check for mass conversation law')
plt.show()
