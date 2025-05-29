'''
Clase:        Fundamentos de Programación
Tema:         Ejercicios
Ejercicio:    !Adivina el numero!
Descripción:  Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
El programa debe seguir pidiendo números hasta que acierte. En cada
intento fallido el programa notificará al usuario si el número secreto es
mayor o menor al último valor ingresado.

Autor:        Violeta Jacobo
Fecha:        2025-05-29
Estado:       [ Terminado ]
'''
import random

numero = (input("Ingrese un numero entre 1 & 100: "))
aleatorio = random.randint(1,100)  
while True:
    if numero.isdigit():
        numero = int(numero)
    if numero <1  or numero > 100:
            print("El número debe estar entre 1 y 100. Inténtalo de nuevo.")
            continue 
    if numero < aleatorio:
        print("El número secreto es mayor")
        numero = input("Ingrese un numero entre 1 & 100: ")
    elif numero > aleatorio:
        print("El número secreto es menor")
        numero = input("Ingrese un numero entre 1 & 100: ")   
    elif numero == aleatorio:
        print("¡Felicidades! Has adivinado el número secreto.")
        break
    print("Fin del juego")