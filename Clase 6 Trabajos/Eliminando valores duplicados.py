'''
Clase:        Fundamentos de Programación
Tema:        Trabajo clase 9
Ejercicio:   Dada una lista ingresada por el usuario, elimina los elementos duplicados manteniendo la primera aparicion de cada numero.


Autor:        Violeta Jacobo
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

numeros_repetidos = []
numero_lista = input("Introduce un número: ")
lista = numero_lista.split()  

for numero in lista:
    if numero  not in  numeros_repetidos:
        numeros_repetidos.append(numero)
lista_final =str(numeros_repetidos).replace("[", "").replace("]", "").replace("'", "")
print(lista_final)

