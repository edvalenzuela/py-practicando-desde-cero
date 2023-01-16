
#3x^2-5x+2=0 x=1 x=2/3

from math import sqrt

A = int(input('Ingrese el valor de A: '))
B = int(input('Ingrese el valor de B: '))
C = int(input('Ingrese el valor de C: '))

x1 = 0
x2 = 0

if((B**2)-(4*A*C)) < 0 :
	print("No se puede realizar porque no se puede sacar raiz a un numero negativo")
else:
	x1 = (-B + sqrt((B**2)-(4*A*C)))/(2*A)
	x2 = (-B - sqrt((B**2)-(4*A*C)))/(2*A)
	print("La solucion es: \nx1=", x1, "\nx2=", x2)