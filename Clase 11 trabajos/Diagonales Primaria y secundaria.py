'''
Clase:        Fundamentos de Programación
Tema:        Trabajo clase 11
Ejercicio:   Diagonal principal y secundaria
Descripcion: Dada una matriz cuadrada ingresada por el
usuario, crea dos listas, una con los
elementos de la diagonal principal y la otra
con los elementos de la diagonal
secundaria.

Autor:        Violeta Jacobo
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''

N = int(input())
l = []
for i in range(N):
    temp = list(map(int, input().split()))
    l.append(temp)


diagonal_principal = []
diagonal_secundaria = []

#print(l)
for i in range(N):
    for j in range(len(l[i])):
        if i == j:
            diagonal_principal.append(l[i][j])
            print(f"valor  en la posicion {i},{j} = {l[i][j]}")
        
        if i + j == len(l)-1:
            diagonal_secundaria.append(l[i][j])
            print(f"valor  en la posicion {i},{j} = {l[i][j]}")
            
# Imprime la diagonal principal
print(diagonal_principal)
print(diagonal_secundaria)