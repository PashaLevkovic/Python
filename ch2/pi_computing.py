# -*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt

N = input(u'введите N: ')

def PL(n):
    p = 0
    for i in range(n+1):
        p += 8.0/((4*i+1)*(4*i+3))
    return p
    
def PE(n):
    p = 0
    for i in range(1, n+1):
        p += 1.0/i**2
    return sqrt(6*p)
    
faultPL = [] 
faultPE = []

for i in range(1, N+1):
    faultPL.append(fabs(PL(i)-pi))
    faultPE.append(fabs(PE(i)-pi))
          
n = range(1, N+1)       
       
plt.plot(n, faultPL)
plt.plot(n, faultPE)
plt.xlabel(u'N')
plt.ylabel(u'Fault')
plt.show()
print "Погрешность способа Лейбница",fabs(PL(N) - pi)
print "Погрешность способа Эйлера  ",fabs(PE(N) - pi)
        