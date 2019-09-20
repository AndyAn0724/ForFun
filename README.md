# ForFun
Some cool pet projects. :) 

## 3Point1Semicircle: 
This is a cool probability problem. 
### Question: 
    Assume 3 points on a circle. What is the probability of all points in one semi-circle?
![Circle3](images/CircleWith3Points.png)    

### Method 1:
3 points on a circle must give a triangle. 
If the triangle is a Obtuse/Right triangle, then 3 points must be on one semi-circle. 


### Method 2 (generalized to N points):
    Assume N points on a circle. What is the probability of all points in one semi-circle?

1. We could still use Method 1 idea to generalize, but it's not very efficient: N points give 3Cn number of traingles... If all of them are Obtuse/Right triangles. All points must be on one semi-circle.
2. We could think about the relationship between angles we generated: 
    First sort all generated angles ascendingly. Then, all N points must be on the same semi-circle if: 
    1. x_max - x_min <= 180, OR
    2. x_i - x_i-1 >= 180. 

![Circle](images/Circle.png)
