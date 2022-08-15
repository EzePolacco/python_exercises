#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Subjects and credits

Crear un programa que almacene el diccionario con
los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} 
y después muestre por pantalla los créditos de cada asignatura en el formato 
<asignatura> tiene <créditos> créditos, 
donde <asignatura> es cada una de las asignaturas del curso, 
y <créditos> son sus créditos. 
Al final debe mostrar también el número total de créditos del curso.

"""
subjects = {"Matemática": 6,
            "Física": 4,
            "Química": 5
            }
credit_total = 0
for subject, credit in subjects.items():
    print(f"{subject}:{credit}")
    credit_total += credit
