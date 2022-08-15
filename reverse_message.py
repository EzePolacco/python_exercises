#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Revese message

Pedir al usuario que ingrese un mensaje cualquiera, 
si el mensaje tiene más de 100 caracteres imprimirlo por pantalla, 
si tiene entre 50 y 100 caracteres imprimirlo al revés, 
si no se cumple ninguna de las opciones anteriores, 
por pantalla devolver un mensaje que diga "su mensaje es demasiado corto
"""

message = input("Please enter a message: ")

if len(message) > 100:
    print(message)
elif 50 <= len(message) <= 100:
    print(message[::-1])
else:
    print("Message is too short.")