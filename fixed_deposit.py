#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""    
Crear un programa que calcule cuánto dinero tendré al cabo de un mes
si deposito hoy 2000 en el banco y el interés mensual es de 5%, 
y luego devuelva por pantalla ese valor.

Opción 1 : sin IF
Opción 2 : con IF

"""
# Algorithm without IF
"""
print("Please, insert amount to deposit. Only an integer number.")
print("---------------------------------------------------------")
capital = int(input("Amount to deposit: "))

month_rate = 0.05 # 5% per month
print(f"Month rate: {month_rate}")
term = 1 # Months
print(f"Term: {term} month/s")
print("---------------------------------------------------------")
print(" ")
print("Calculating...")
print(" ")
profit = capital * month_rate * term

print(f"If you deposit ${capital} for a period of {term} month/s you will obtain ${profit} of profit.")

total = capital * (1 + month_rate) * term

print(" ")
print(f"After {term} month/s you will obtain a total of ${total} (${capital} deposited + ${profit} interest).")
print(" ")

"""

# Algorithm with IF


print("Please, insert amount to deposit. Only an integer number.")
capital = float(input("Amount to deposit: "))
print("---------------------------------------------------------")
print("Please, indicate term in months.")
term = float(input("Term: "))
print("---------------------------------------------------------")
month_rate = 0.37 # 5% per month
print(f"Month rate: {month_rate}")
print("---------------------------------------------------------")


if type(capital) not in (float, int) or type(term) not in (float, int):
    if str(float(capital)) != str(capital) or str(float(term)) != str(term):
        print("It must be numbers!")


elif capital > 0 and term >= 1:
    
    print(" ")
    print("Calculating...")
    print(" ")
    print("Result:")
    print(" ")
    profit = round((capital * month_rate * term), 4)

    print(f"If you deposit ${capital} for a period of {term} month/s you will obtain ${profit} of profit.")

    total = round((capital * (1 + month_rate) * term), 4)

    print(" ")
    print(f"After {term} month/s you will obtain a total of ${total} (${capital} deposited + ${profit} interest).")
    print(" ")
    
    
else: print("The selected term does not generate interest.")