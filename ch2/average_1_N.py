# -*- coding: utf-8 -*-

N = input(u'введите N: ')

def f(N):
    S = 0.0
    for i in range(1, N+1):
        S += i
    return S/N
print "Среднее значение =", f(N)        
        