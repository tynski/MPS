import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# intput data
A = 0.1  # m
B = 0.02  # m

# NX, NY number of paritcles in rows and cols
nx = ny = 10
# dx, dy distance betweeb particles in rows and cols
dx = A / nx
dy = A / ny

# time grid
t_sim = 10  # s        TIME
dt = 1e-3  # s         Time step
nt = int(t_sim / dt)  # Number of time step

# first boundary condition
T1 = 100
T2 = 10

T = np.ones((nx, ny)) * T2

# heater placement
up_shift = int(0.5 * nx - 0.5 * B / dx)
down_shift = int(0.5 * ny + 0.5 * B / dx)
heater_size = (down_shift - up_shift) * dx
T[up_shift:down_shift, up_shift:down_shift] = 100

# material properties
#pick material to be tested
material = 'stainless steel'
if material == 'alumina':
    # alumina
    p = 2700  # kg/m^3
    cw = 900  # J/kgK
    K = 237  # W/mK
elif material == 'cooper':
    # cooper
    p = 8920  # kg/m^3
    cw = 380  # J/kgK
    K = 401  # W/mK
elif material == 'stainless steel':
    # stainless steel
    p = 7869  # kg/m^3
    cw = 450  # J/kgK
    K = 58  # W/mK
else:
    print('Non known material. Sorry :(')
    sys.exit()

# campure few plate states
fig, axes = plt.subplots(5, 1, figsize=(5, 8))
state = [0, int(nt / 4), int(nt / 2), int(3 * nt / 4), nt - 1]
no_plot = 0

for n in range(nt):
    # nx-1 and ny-1 beacuse we don't change boundary values
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            T_pref = T[i, j]
            dT1_num = T[i + 1, j] - 2 * T[i, j] + T[i - 1, j]
            dT2_num = T[i, j + 1] - 2 * T[i, j] + T[i, j - 1]
            const = (K * dt) / (cw * p)
            T[i, j] = T_pref + const / (dx**2) * dT1_num + const / (dy**2) * dT2_num

    if n in state:
        sns.heatmap(T, cmap=sns.color_palette("RdBu_r", 500), vmin=0, vmax=100, ax=axes[no_plot], linewidths=.1, linecolor='black')
        axes[no_plot].set_title("{:.2f}".format(state[no_plot] * dt) + '[s]')
        axes[no_plot].xaxis.set_ticks_position('none')
        axes[no_plot].yaxis.set_ticks_position('none')
        axes[no_plot].xaxis.set_ticklabels([])
        axes[no_plot].yaxis.set_ticklabels([])
        no_plot += 1

axes[no_plot - 1].set_xlabel('X')
axes[no_plot - 1].set_ylabel('Y')
plt.tight_layout()
plt.show()
