#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contact book

Crear un programa que pregunte al usuario
su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje.
"""
print("Please, enter the followin data required")

data = {"Name": str(input("Name: ")),
        "Age": int(input("Age: ")),
        "Address": str(input("Address: ")),
        "Phone number": int(input("Phone number: "))}

print(data)