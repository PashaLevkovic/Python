# -*- coding: utf-8 -*-


from math import *

x3 = [0.0, 0.0, 2.0]
y3 = [0.0, 2.0, 0.0]
x4 = [0.0, 0.0, 2.0, 2.0]
y4 = [0.0, 2.0, 2.0, 0.0]
x5 = [0.0, 0.0, 2.0, 3.0, 3.0]
y5 = [0.0, 3.0, 3.0, 2.0, 0.0]


def polyarea(x,y):
    polyarea = 0
    for i in range(len(x)):
        if i+1 < len(x):
            polyarea += (x[i]+x[i+1])*(y[i]-y[i+1])
        else:
            polyarea += (x[i]+x[0])*(y[i]-y[0])
    return polyarea/2

print "Площадь треугольника = ", polyarea(x3,y3)
print "Площадь четырехугольника = ", polyarea(x4,y4)
print "Площадь пятиугольника = ", polyarea(x5,y5)
