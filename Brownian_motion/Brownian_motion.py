import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# set size for plots
plt.rcParams['figure.figsize'] = (14.0, 8.0)

# initial values
n_steps = 1000
n_parts = 100
mu, sigma = 0, 1

# booleans for drawing plots
plot_motion = False
plot_disp = True

# initialize x and y
x = np.zeros((n_steps, n_parts))
y = np.zeros((n_steps, n_parts))


for i in range(n_steps - 1):
    dx = np.random.normal(mu, sigma, (1, n_parts))
    dy = np.random.normal(mu, sigma, (1, n_parts))
    x[i + 1, :] = x[i, :] + dx
    y[i + 1, :] = y[i, :] + dy

if plot_motion:
    plt.plot(x, y)
    plt.xlabel('time step', fontsize=14)
    plt.ylabel('particle motion', fontsize=14)
    plt.title('Brownian motion for particles', fontsize=16)
    plt.show()

# mean square of displacement
disp = x**2 + y**2
disp_ms = np.mean(disp, axis=1)

if plot_disp:
    plt.plot(range(n_steps), disp_ms)
    plt.ylabel('mean square of displacement', fontsize=14)
    plt.xlabel('number of steps', fontsize=14)
    plt.show()


#We define time as number of discrete interval or steps (n_steps), so we could assume that t = 1, so time is the range of the n_step or N

d_square = x**2 + y**2 
mean_square = np.mean(d_square, axis=1)
plt.plot(mean_square)
plt.plot(range(n_step), 'or')

plt.title('Mean Square of Displacement versus Time n_step=1000 n_part=900', fontsize=16)
plt.ylabel('mean square of displacement', fontsize=14)
plt.xlabel('time', fontsize=14)
plt.grid(True)
red_patch = mpatches.Patch(color='red', label='Time')
blue_patch = mpatches.Patch(color='blue', label='Mean Square of Displacement')
plt.legend(handles=[red_patch,blue_patch])
