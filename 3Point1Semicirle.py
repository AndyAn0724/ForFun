# -*- coding: utf-8 -*-
"""
Question: 
    Assume 3 points on a circle. What is the probability of all points in one semi-circle?

Method 1: 
    Use triangle interior angle >= 90.
    3 points on a circle must give a triangle. 
    If the triangle is a Obtuse/Right triangle, then 3 points must be on one semi-circle.  

Method 2: generalized method.
   Use the relationships btw each angle.
   First sort all generated angles ascending. 
   All N points must be on the same semi-circle if: 
   1. angle_max - angle_min <= 180, OR
   2. angle_i - angle_i-1 >= 180.    
    
"""

import numpy as np 
import matplotlib.pyplot as plt
from math import cos, sin
import time as time


def M1_dist(theta1, theta2):
    """
    Given two points in theta: theta1, theta2, calculate the distance between points.
        dist = sqrt((cos.theta1 - cos.theta2)^2 + (sin.theta1 - sin.theta2)^2)
    """
    return np.sqrt(2 - 2*sin(theta1)*sin(theta2) - 2*cos(theta1)*cos(theta2))

def M1_cos_angle(d1, d2, d3):
    """
    Given three distance, d1, d2, d3, calculate the three inner angles of the triangle.
        c^2 = a^2 + b^2 - 2 * a * b * cos(theta)
    """
    cos1 = (d1*d1 + d2*d2 - d3*d3) / (2.0*d1*d2)
    cos2 = (d1*d1 + d3*d3 - d2*d2) / (2.0*d1*d3)
    cos3 = (d2*d2 + d3*d3 - d1*d1) / (2.0*d2*d3)
    return cos1, cos2, cos3

def M1(N, N_pnt):
    """
    Paras:
        N: number of iterations
        N_pnt: number of points to test on semi-circle (this method only support 3 points actually...)
    
    Method 1: 
        Use triangle interior angle >= 90.
        3 points on a circle must give a triangle. 
        If the triangle is a Obtuse/Right triangle, then 3 points must be on one semi-circle.           
    """
    # time it
    t1 = time.time()
    N_pnt = 3       # this method only support 3 points...
    n = 0           # counter
    bingo = 0.0     # bingo!
    
    while n < N:
        # generate N_pnt of theta randomly.
        x = np.random.rand(N_pnt) * 360.0
        
        ## let's do a plot if it's not too crazy...
        #if n < 6:
        #    plt.plot([cos(xi) for xi in x], [sin(xi) for xi in x])
        
        # assume a circle with radius = 1, calculate dist of each point-to-point
        d1 = M1_dist(x[0], x[1])
        d2 = M1_dist(x[0], x[-1])
        d3 = M1_dist(x[1], x[-1])
        
        # calculate all angles of triangle
        cos1, cos2, cos3 = M1_cos_angle(d1, d2, d3)
        if np.any(np.array([cos1, cos2, cos3]) <= 0):
            # if cos(theta) < 1, then it's a obtuse angle. 
            bingo += 1
            
        n += 1
    
    # time it
    t2 = time.time()
    
    return bingo/N, round(t2-t1, 4)
    

def M2(N, N_pnt):
    """
    Paras:
        N: number of iterations
        N_pnt: number of points to test on semi-circle (this method supports all.)
    
    Method 2: generalized method.
       Use the relationships btw each angle.
       First sort all generated angles ascending. 
       All N points must be on the same semi-circle if: 
       1. x_max - x_min <= 180, OR
       2. x_i - x_i-1 >= 180.        
    """    
    # time it
    t1 = time.time()
    n = 0           # counter
    bingo = 0.0     # bingo!
    
    while n < N:
        # generate N_pnt of theta randomly.
        x = np.random.rand(N_pnt) * 360.0
        x = np.sort(x)
        
        if np.any(np.append(np.diff(x) >= 180, (x[-1] - x[0]) <= 180)):
            bingo += 1
            
        n += 1
    
    # time it
    t2 = time.time()
    
    return bingo/N, round(t2-t1, 4)
    

if __name__ == "__main__":
    
    N = 10**5
    N_pnt = 10
    
    M1_est, M1_time = M1(N, N_pnt)
    M2_est, M2_time = M2(N, N_pnt)
    
    # print results
    print('Number of iterations:', N)
    print('Number of points:', N_pnt)
    print('Correct result:', N_pnt / 2**(N_pnt-1))
    
    if N_pnt == 3:
        # Method 1 only support N_pnt = 3.
        print('Simulated result (Method 1):', M1_est)
        print('Total time took (Method 1):', M1_time, 'seconds')
    
    print('Simulated result (Method 2):', M2_est)
    print('Total time took (Method 2):', M2_time, 'seconds')
    print('')
    
    
    print('Time testing for Method 2:')
    # do a time complexity test on Method 2
    N_all = 10**np.arange(2, 5)
    N_all = np.sort(np.append(N_all, 5*N_all))
    time_all = []
    
    for Ni in N_all:
        _, M2_time = M2(Ni, N_pnt)
        time_all.append(M2_time)
        print('Running Method 2 for {} iterations, took {} seconds.'.format(Ni, M2_time))
    
    plt.title('Time test of Method 2 | {} number of points.'.format(N_pnt))    
    plt.plot(N_all, np.array(time_all))
    plt.show()
    
    
    
    
    
    
    
