
practica1 = float(input('Ingrese el valor de la practica 1: '))
practica2 = float(input('Ingrese el valor de la practica 2: '))
practica3 = float(input('Ingrese el valor de la practica 3: '))

examenParcial = float(input('Ingrese el valor del examen parcial: '))
examenFinal = float(input('Ingrese el valor del examen final: '))

promedioPractica = (practica1+practica2+practica3) / 3

promedioFinal = (promedioPractica + examenParcial * 2 + examenFinal * 3) / 6

print("El promedio final del estudiante es de:\n ", promedioPractica , "\n", "Y el promedio final es de:\n ", promedioFinal )