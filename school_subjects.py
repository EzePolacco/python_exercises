#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
School subjects

Crear un programa que almacene en una lista las siguientes materias: 
Historia, Matemática, Lengua y Geografía. 
Luego devolver por pantalla la última materia almacenada.
"""

subjects = []
    
for i in range (4):
    subject_enter = input("Insert a subject name: ")
    subjects.append(subject_enter)
    print("Subjects list")
    print(subjects)
    print(subjects[-1])
    
if len(subjects) == 4:
    print("Process ended")

        