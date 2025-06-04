import numpy as np

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

print("Dimensiones:", consumo.ndim)
print("Forma:", consumo.shape)
print("Tipo de dato:", consumo.dtype)
print("Consumo primer hogra:", consumo[0])
print("Consumo el miercoles (dia 3):", consumo[:, 2])



promedio_por_hogar = np.mean(consumo, axis=1)

promedio_por_dia = np.mean(consumo, axis=0)

total_consumo = np.sum(consumo)

print(promedio_por_dia)
print(promedio_por_hogar)
print(total_consumo)


#Maximo por hogar
maximos = np.max(consumo, axis=1)

#Minimo por hogar
minimos = np.min(consumo, axis=1)

#Desviacion estandar global
desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)


#Suma por hogar(semanal)
consumo_total_hogar = np.sum(consumo, axis=1)

#Indice del hogar con mayor consumo
indice_mayor_consumo = np.argmax(consumo_total_hogar)

#indice del hogar con mejor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mas_eficiente)
print (indice_mayor_consumo)

#suma por hogar (semana)
consumo_total_hogar =np.sum(consumo, axis=1)
print("Consumo total por hogar (semanal):", consumo_total_hogar)

#Compara cada hogar con un valor mayor a 100
altos = consumo_total_hogar > 100
#Filtrado de los hogares que cumplen la condicion 
consumo_mayor_100 = np.where(altos)[0]

print(f"Los hogares con consumo mayor a 100 son: {consumo_mayor_100}")

#aplicando normalizacion min-max al conjunto de datos 
consumo_normalizado = (consumo - np.min(consumo)) / (np.max(consumo) - np.min(consumo))

print(consumo_normalizado)

#-----------PARTE DE ANALISIS-------------------------------------
#. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
print("Consumo el viernes:", consumo[4,4])

#Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
print("Consumo de los ultimos 3 domingos:", consumo[-3:,6])

#Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
promedio_finde = np.mean(consumo[:, 5:7], axis=1)
print(f'El promedio de consumo durante los fines de semana es: {promedio_finde}')

#¿Qué día de la semana tiene la mayor desviación estándar entre hogares?
desviaciones_por_dia = np.std(consumo, axis=0)
dia_mayor_desviacion = np.argmax(desviaciones_por_dia)
valor_mayor_desviacion = desviaciones_por_dia[dia_mayor_desviacion]
print(f"El día de la semana con mayor desviación estándar entre hogares es el día {dia_mayor_desviacion} (índice),")
print(f"con una desviación estándar de {valor_mayor_desviacion:.2f}.")
print("Esto significa que ese día hay más variabilidad en el consumo entre los hogares.")


# Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
consumo_total_hogar = np.sum(consumo, axis=1)
indices_menor_consumo = np.argsort(consumo_total_hogar)[:3]
valores_menor_consumo = consumo_total_hogar[indices_menor_consumo]

print("Los 3 hogares con menor consumo total durante la semana son:")
for i in range(3):
    print(f" - Hogar {indices_menor_consumo[i]} con un consumo total de {valores_menor_consumo[i]:.2f}")

#Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
# Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
consumo_hogar_3 = consumo[2]
consumo_hogar_3_incrementado = consumo_hogar_3 * 1.10 
nuevo_total_hogar_3 = np.sum(consumo_hogar_3_incrementado)

print(f"Si el hogar 3 aumenta su consumo en un 10% cada día, su nuevo consumo total semanal sería: {nuevo_total_hogar_3:.2f}")




