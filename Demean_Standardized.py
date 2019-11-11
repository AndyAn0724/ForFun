# -*- coding: utf-8 -*-
"""
Trying to see Demean vs. Standardized.

@author: andy.an
"""

import numpy as np
import matplotlib.pyplot as plt

num_point = 50
x = np.sort(np.random.rand(num_point) * 6.0 + 1.0)
#x = np.linspace(1, 6, num_point)
noise = np.random.randn(num_point) * 3.0

# let's draw: y = ax + b + noise
a = 8
b = 2
y = a * x + b + noise

fig, ax = plt.subplots()
ax.scatter(x, y, label='Original', alpha=0.9)

# let's de-mean the x
x_demean = x - np.mean(x)
y_demean = y - np.mean(y)
ax.scatter(x_demean, y_demean, label='De-meaned', alpha=0.7)

# let's see de-mean & de-std
x_stdized = (x - np.mean(x)) / np.std(x, axis=0)
y_stdized = (y - np.mean(y)) / np.std(y, axis=0)
ax.scatter(x_stdized, y_stdized, label='Standardized', alpha=0.5)

ax.legend()
ax.grid(True)

plt.savefig('images\Demean-Standardized.png')
plt.show()

