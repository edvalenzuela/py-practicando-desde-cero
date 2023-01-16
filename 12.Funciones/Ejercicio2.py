
'''def factorial2() : 
	num = int(input('Ingresa tu numero entero y positivo: '))

	if num > 0:
		factorial2 = 1
		for i in range(1, num + 1) :
			factorial2 *= i
			print('resultado : {} x {} = {}'.format(i, num, factorial2))
	else:
		print('EL numero es negativo y no podemos proceder')

factorial2()'''

def factorial() : 
	from math import factorial
	num = int(input('Ingresa tu numero entero y positivo: '))

	if num > 0:
		print(factorial(num))
	else:
		print('EL numero es negativo y no podemos proceder')

factorial()