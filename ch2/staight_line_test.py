# -*- coding: utf-8 -*-

from numpy import *
c = 2
tg = False
L = lambda x: 4*x + 1

def line(x):
    result = []
    for i in range(0, len(interval)):
        l = (L(x[i])-L(c))/(x[i]-c)
        result.append(l)
        if result[i] == result[i-1]:
            tg = True
    return result, tg
interval = []
interval = linspace(0,10,100)

result, tg = line(interval)
print result
if tg:
    print "Проверка выполнена: прямая"

