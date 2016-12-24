# -*- coding: utf-8 -*-

from math import *

r = 10.6
a = 1.3
b = 0

def S(r):
    return pi * r ** 2

while a*b < S(r):
    b += 1
    
b -= 1    
    
print "наибольшее вохможное b =", b
   
    
    