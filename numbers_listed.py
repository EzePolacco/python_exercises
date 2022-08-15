#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Numbers list

Crear una lista con varios números, luego ordenarlos de manera creciente y
devolver por pantalla la lista ordenada y cuál es el menor y cuál el mayor.
"""

numbers_list = []

for i in range(10):
    numbers = int(input("Enter any number you want: "))
    numbers_list.append(numbers)
    print(numbers_list)

if len(numbers_list) == 10:
    print("Process ended")

numbers_list.sort()

print(f"Sorted numbers list: {numbers_list}")
print(" ")
print(f"Smallest number: {min(numbers_list)}")
print(" ")
print(f"Biggest number: {max(numbers_list)}")
