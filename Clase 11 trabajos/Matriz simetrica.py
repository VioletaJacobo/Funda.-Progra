'''
Clase:        Fundamentos de Programación
Tema:        Trabajo clase 11
Ejercicio:    Matriz simétrica
Descripcion:  Dada una matriz cuadrada ingresada por el
usuario, comprueba si la matriz cuadrada es
simétrica respecto a su diagonal principal.

Autor:        Violeta Jacobo
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''



n = int(input("Ingrese la dimensión de la matriz: "))


matriz = []


for i in range(n):
    fila = list(map(int, input(f"Ingrese los elementos de la fila {i+1}, separados por coma: ").split(',')))
    matriz.append(fila)


es_simetrica = True 


for i in range(n):
    for j in range(i + 1, n):
        if matriz[i][j] != matriz[j][i]:
            es_simetrica = False
            break 
    if not es_simetrica:
        break


if es_simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")