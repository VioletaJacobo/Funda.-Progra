'''
Clase:        Fundamentos de Programación
Tema:        Trabajo clase 11
Ejercicio:    Juego del entorno

Descripcion:  Dada una matriz binaria ingresada por el
usuario, verifica para cada celda de una
matriz binaria cuántos elementos con valor
de 1 hay en las celdas vecinas (arriba, abajo,
izquierda, derecha, diagonales).


Autor:        Violeta Jacobo
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''

num_filas = int(input("Ingrese la cantidad de filas de la matriz: "))
num_columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
matriz_binaria = []
for fila in range(num_filas):
    entrada_fila = input(f"Ingrese los números de la fila {fila} separados por coma: ")
    fila_valores = list(map(int, entrada_fila.split(",")))
    matriz_binaria.append(fila_valores)

desplazamientos_vecinos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
matriz_vecinos = []
for fila in range(num_filas):
    fila_vecinos = []
    for columna in range(num_columnas):
        contador_unos = 0
        for dx, dy in desplazamientos_vecinos:
            vecino_fila, vecino_columna = fila + dx, columna + dy
            if 0 <= vecino_fila < num_filas and 0 <= vecino_columna < num_columnas:
                if matriz_binaria[vecino_fila][vecino_columna] == 1:
                    contador_unos += 1
        fila_vecinos.append(contador_unos)
    matriz_vecinos.append(fila_vecinos)

for fila in matriz_vecinos:
    print(fila)