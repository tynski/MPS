import numpy as np
import matplotlib.pyplot as plt

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
