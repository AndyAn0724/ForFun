# -*- coding: utf-8 -*-
"""
Question: 
    Assume 3 points on a circle. What is the probability of all points in one semi-circle?

Idea:
    3 points on a circle must give a triangle. 
    If the triangle is a Obtuse/Right triangle, then 3 points must be on one semi-circle. 


Generalization idea:
    Assume N points on a circle. What is the probability of all points in one semi-circle?
--> N points give 3Cn number of traingles... 
    If all of them are Obtuse/Right triangles. All points must be on one semi-circle.
    
"""

import numpy as np 
import matplotlib.pyplot as plt
from math import cos, sin
import time as time


def dist(theta1, theta2):
    """
    Given two points in theta: theta1, theta2, calculate the distance between points.
        dist = sqrt((cos.theta1 - cos.theta2)^2 + (sin.theta1 - sin.theta2)^2)
    """
    return np.sqrt(2 - 2*sin(theta1)*sin(theta2) - 2*cos(theta1)*cos(theta2))

def cos_angle(d1, d2, d3):
    """
    Given three distance, d1, d2, d3, calculate the three inner angles of the triangle.
        c^2 = a^2 + b^2 - 2 * a * b * cos(theta)
    """
    cos1 = (d1*d1 + d2*d2 - d3*d3) / (2.0*d1*d2)
    cos2 = (d1*d1 + d3*d3 - d2*d2) / (2.0*d1*d3)
    cos3 = (d2*d2 + d3*d3 - d1*d1) / (2.0*d2*d3)
    return cos1, cos2, cos3


if __name__ == "__main__":
    # time it
    t1 = time.time()
    
    # number of iterations
    N = 10**2
    # counter
    n = 0
    # bingo!
    bingo = 0.0
    
    while n < N:
        # generate 3 theta randomly.
        x = np.random.rand(3) * 360.0
        
        # let's do a plot if it's not too crazy...
        if n < 6:
            plt.plot([cos(xi) for xi in x], [sin(xi) for xi in x])
        
        # assume a circle with radius = 1, calculate dist of each point-to-point
        d1 = dist(x[0], x[1])
        d2 = dist(x[0], x[-1])
        d3 = dist(x[1], x[-1])
        
        # calculate all angles of triangle
        cos1, cos2, cos3 = cos_angle(d1, d2, d3)
        if np.any(np.array([cos1, cos2, cos3]) <= 0):
            # if cos(theta) < 1, then it's a obtuse angle. 
            bingo += 1
            
        n += 1
    
#    plt.axis('equal')
#    plt.savefig('Circle.png')
        
    # time it
    t2 = time.time()
    print('Number of iterations:', N)
    print('Final simulated result:', bingo / N)
    print('Total time took:', round(t2-t1, 4), 'seconds')
    
