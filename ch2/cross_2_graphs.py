# -*- coding: utf-8 -*-

from math import *
import numpy as np

N = input(u'Введите количество точек : ')
e = input(u'Введите точность: ')

def f(x):
    return x
    
def g(x):
    return x ** 2

x = np.linspace(-4, 4, N)
T = 0

for i in range(len(x)):
    if fabs(f(x[i]) - g(x[i])) < e:
        T = x[i]

print T        