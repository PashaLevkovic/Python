# -*- coding: utf-8 -*-

from random import *

x = []
for i in range(6):
    x.append(uniform(0,10))
    
print x  

def sort(x):
    for i in range(len(x)-1):
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                s = x[j]
                x[j] = x[j+1]
                x[j+1] = s
    return x            
            
print sort(x)