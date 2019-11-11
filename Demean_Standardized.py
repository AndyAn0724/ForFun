# -*- coding: utf-8 -*-
"""
Trying to see Demean vs. Standardized.

@author: andy.an
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(1000, 2) +1.5

fig, ax = plt.subplots()

ax.scatter(x[:,0], x[:,1], label='Original', alpha=0.9)

# let's de-mean the x
x_demean = x - np.mean(x)
ax.scatter(x_demean[:,0], x_demean[:,1], label='De-meaned', alpha=0.7)

# let's see de-mean & de-std
x_stdized = (x - np.mean(x)) / np.std(x, axis=0)
ax.scatter(x_stdized[:,0], x_stdized[:,1], label='Standardized', alpha=0.5)

ax.legend()
ax.grid(True)

plt.savefig('Demean-Standardized.png')
plt.show()

