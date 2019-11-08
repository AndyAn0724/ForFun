# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:28:18 2019

Generate random correlated variables. 
    Use z1, z2, z3 ~ N(0, 1) to generate x1, x2, x3 (5000 samples) with the given covariance matrix & mu.

@author: andy.an
"""

import numpy as np
import matplotlib.pyplot as plt

# assume we want to generate x1, x2, x3, 5000 samples with covariance matrix & mu given.
mu = 0.1
cov = np.array([[1, 0.5, 0.3]
              , [0.5, 1, 0.8]
              , [0.3, 0.8, 1]])

# get cholesky decomp of cov = L * L.T (L is lower triangular)
l = np.linalg.cholesky(cov)

# get three indpendent random var ~ N(0,1)
n = 5000
z1 = np.random.normal(0, 1, n)
z2 = np.random.normal(0, 1, n)
z3 = np.random.normal(0, 1, n)

# now is the magic.
x_all = np.matmul(l, np.vstack((z1, z2, z3))) + mu

# checking
ck = np.cov(x_all)

plt.scatter(x_all[0,:].T, x_all[1,:].T, alpha=0.9)
plt.scatter(x_all[0,:].T, x_all[2,:].T, alpha=0.7)
plt.scatter(x_all[1,:].T, x_all[2,:].T, alpha=0.5)

