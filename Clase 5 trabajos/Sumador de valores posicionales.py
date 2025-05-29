'''
Clase:        Fundamentos de Programación
Tema:        Trabajo clase 8
Ejercicio:    Sumador de valores posicionales
Descripción:  Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2.


Autor:        Violeta Jacobo
Fecha:        2025-05-29
Estado:       [ Terminado ]
'''

numero = int(input("Ingrese un número: "))  
while numero >= 10:  
    suma = sum(int(digito) for digito in str(numero)) 
    print("La suma de los dígitos es:", suma)
    numero = suma
print("El resultado final es:", suma)