# -*- coding: utf-8 -*-

"""   
Crear un programa que pida al usuario ingresar 2 números por teclado
y devuelva por pantalla la suma de ellos en un renglón, 
la resta en otro, el producto en otros y la división en otro.
"""

number1 = float(input("Ingrese un número: "))

number2 = float(input("Ingrese otro número: "))


if type(number1) not in (float, int) or type(number2) not in (float, int):
    
    print("It must be numbers!")

elif str(float(number1)) != str(number1) or str(float(number2)) != str(number2):
    
    print("It must be numbers!")

else:
        
    add = number1 + number2
    print(f"Sum result:  {add}")
    
    subtraction = number1 - number2
    print(f"Subtraction result: {subtraction}")
    
    multiplication = number1 * number2
    print(f"Multiplication result: {multiplication}")
    
    division = number1/number2
    print(f"Division result: {division}")
    