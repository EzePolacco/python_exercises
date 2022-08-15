#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Numbers list

Crear un programa que pregunte al usuario 5 números enteros 
y devuelva una lista con ellos.
"""

numbers = []

for i in range (5):
    insert = input("Type any number you want: ")
    numbers.append(insert)
    print("Numbers list")
    print(numbers)
if len(numbers) == 5:
    print("Process ended")