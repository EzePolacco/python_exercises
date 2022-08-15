#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scalar product
Crear un programa que almacene los vectores (1,2,3) y (-1,0,2) 
en dos listas y muestre por pantalla su producto escalar.
"""

a = [1, 2, 3]

b = [-1, 0, 2]

print("Vector a:", a)
print("Vector b:", b)

sum = 0

for i in range(3):
    product = a[i]*b[i]
    
sum += product
print("Scalar product:", sum)