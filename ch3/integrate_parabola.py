# -*- coding: utf-8 -*-

from trapezoidal import trapezoidal as T
from rectangular import rectangular as R


f = lambda x: x*(x-1)
expected = 160/3.0
print "Формула трапеций:   ", "  Погрешность " 
print "Для n = 2  ", T(f, 2, 6, 2), "     ", abs(expected - T(f, 2, 6, 2))
print "Для n = 100", T(f, 2, 6, 100), "  ",  abs(expected - T(f, 2, 6, 100))
print "Формула прямоугольников:"
print "Для n = 2  ", R(f, 2, 6, 2), "     ", abs(expected - R(f, 2, 6, 2))
print "Для n = 100", R(f, 2, 6, 100), "  ",abs(expected - R(f, 2, 6, 100))
