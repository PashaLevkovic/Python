# -*- coding: utf-8 -*-

from random import *

N = input(u"Введите N: ")
p = []

def rand(n):
    M = 0
    for i in range(0, n):
        p.append(randint(1,6)) 
        if p[i] == 6:
            M += 1
    return M
    
print "Вероятность выпадения 6:",rand(N)/float(N) 
print "Массив:",p       

