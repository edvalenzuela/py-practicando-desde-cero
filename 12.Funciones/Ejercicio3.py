
def numeros() :

	num1 = float(input('Ingrese el primer numero: '))
	num2 = float(input('Ingrese el segundo numero: '))

	if num1 == num2 :
		return 0
	elif num1 > num2 :
		return 1
	else :
		return -1

print(numeros())