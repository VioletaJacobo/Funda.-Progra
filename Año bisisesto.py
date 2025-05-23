'''
Clase:        Fundamentos de Programación
Tema:         Ejercicios
Ejercicio:    Año Bisiesto 
Descripción:  

Autor:        Violeta Jacobo
Fecha:        2025-05-22
Estado:       [ En progreso]
'''
año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")
