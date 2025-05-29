'''
Clase:        Fundamentos de Programación
Tema:         Ejercicios
Ejercicio:    Identificador de contraseña segura 
Descripción:  

Autor:        Violeta Jacobo
Fecha:        2025-05-16
Estado:       [ En progreso]
'''


contraseña ="Contrasena2025"
x = input("Introduce la contraseña: ")
digitos_contra= len(x) >= 8

for e in contraseña:
    if e.isdigit():  
        digitos_contra = True
        
    else:
        digitos_contra = False
if digitos_contra == True:
    print("La contraseña es segura")