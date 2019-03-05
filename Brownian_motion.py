#!/usr/bin/env python
# coding: utf-8

# In[69]:


import numpy as np
import matplotlib.pyplot as plt
import time

get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = (14.0, 8.0)


# In[75]:


N = 1000
n_parts = 100

x = np.zeros((N, n_parts))
y = np.zeros((N, n_parts))

mu, sigma = 0, 1

for i in range(N - 1):
    dx = np.random.normal(mu, sigma, (1, n_parts))
    dy = np.random.normal(mu, sigma, (1, n_parts))
    x[i + 1, :] = x[i, :] + dx
    y[i + 1, :] = y[i, :] + dy


# In[73]:


plt.plot(x, y)
plt.xlabel('time step', fontsize=14)
plt.ylabel('particle motion', fontsize=14)
plt.title('Brownian motion for particles', fontsize=16)


# In[76]:


d_square = x**2 + y**2 
d_square = np.mean(d_square, axis=1)
plt.plot(range(N), d_square)
plt.ylabel('mean square of displacement', fontsize=14)
plt.xlabel('number of steps', fontsize=14)


