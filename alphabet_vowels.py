#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Escribir un programa que almacene todas las letras del abecedario y 
luego elimine las vocales y nos devuelva una lista sin las vocales, 
sin modificar la original.
"""
from string import ascii_letters, ascii_lowercase

alphabet = list(ascii_lowercase)

alphabet.remove('a')
alphabet.remove('e')
alphabet.remove('i')
alphabet.remove('o')
alphabet.remove('u')


print(alphabet)


