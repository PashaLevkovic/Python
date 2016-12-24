# -*- coding: utf-8 -*-

from numpy import linspace
import matplotlib.pyplot as plt


L = linspace(1, 3, 3)
V = L**3
V1= L[0]**3
V2 = L[1]**3
V3 = L[2]**3
plt.plot(L,V)
plt.xlabel("L")
plt.ylabel("V")
plt.show()
print(V1, V[0])
print(V2, V[1])
print(V3, V[2])




