'''
Clase:        Fundamentos de Programación
Tema:         Ejercicios
Ejercicio:    Calculadrora de impuestos 
Descripción:  

Autor:        Violeta Jacobo
Fecha:        2025-05-17
Estado:       [ En progreso]
'''




unit = int(input("Ingrese sus unidades consumidas: "))

value = 0  

if unit >= 0 and unit <= 100:
    value = 0
elif unit >= 101 and unit <= 200:
    value = (unit - 100) * 0.5
else:
    value = (100 * 0.5) + (unit - 200) * 1

print(f"Total a pagar: ${value:.2f}")