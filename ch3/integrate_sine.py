# -*- coding: utf-8 -*-

from trapezoidal import trapezoidal 
from rectangular import rectangular 
from math import *


f = lambda x: sin(x)

expected1 = 2
expected2 = 0
print "Метод трапеций: "
print "Для пи ", trapezoidal(f, 0, pi, 2), "Погрешность: ", abs(expected1 - trapezoidal(f, 0, pi, 2))
print "Для 2пи", trapezoidal(f, 0, 2*pi, 2),"          Погрешность: ", abs(expected2 - trapezoidal(f, 0, 2*pi, 2))
print "Метод прямоугольников: "
print "Для пи ", rectangular(f, 0, pi, 2), "Погрешность: ", abs(expected1 - rectangular(f, 0, pi, 2))
print "Для 2пи", rectangular(f, 0, 2*pi, 2),"          Погрешность: ", abs(expected2 - rectangular(f, 0, 2*pi, 2))
