#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Number list sorted 

Crear una lista con 10 números enteros cualquiera. 
Indicar cuál es el número mayor y cuál es el número menor. 
Si al menos hay 3 números mayores a 100, imprimir esos números, si no, 
imprimir los números menores a 50 que formen parte de la lista.

"""

numbers_list = [10, 4, 8, 112, 25, 101, 47, 879, 71, 66]
maximum = max(numbers_list)
minimum = min(numbers_list)
print(numbers_list)
print(maximum)
print(minimum)

over_100 = []

for i in numbers_list:
    if i > 100:
        over_100.append(i)
if len(over_100) >= 3:
    for numero in over_100:
        print(numero)
else: 
    for numero in numbers_list:
        if numero < 50:
            print(numero)
            