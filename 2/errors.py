# -*- coding: utf-8 -*-
# Программа для вычисления положения мяча при вертикальном движении
# с использованием функции

def y (t):
     v0 = 5       # Начальная скорость
     g = 9.81     # Ускорение свободного падения
     return v0*t - 0.5*g*t**2
	
t = 0.6      # Время
print y(t)
t = 0.9
print y()

# SyntaxError: invalid syntax
# IndentationError: expected an indented block
# IndentationError: unexpected indent
# SyntaxError: invalid syntax
# TypeError: y() takes no arguments (1 given)
# TypeError: y() takes exactly 1 argument (0 given)