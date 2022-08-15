#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Currency

Crear un programa que guarde en una variable
el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo 
o un mensaje de aviso si la divisa no está en el diccionario.
"""



currency = {"Euro": "€",
            "Dollar": "$",
            "Yen": "¥"}

currency_query = str(input("Please, enter currency: ")).capitalize()

for key, value in currency.items():
    if currency_query == key:
        print("Selected currency:", value)
if currency_query not in currency:
    print("Currency selected not available")