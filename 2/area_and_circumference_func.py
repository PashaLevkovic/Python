# -*- coding: utf-8 -*-


from math import *

r = input(u'Введите радиус: ')

def A(r):
    return pi * r ** 2
 
def C(r):
    return 2 * pi * r
  
print "площадь круга =", A(r) 
print "длина окружности =", C(r)   