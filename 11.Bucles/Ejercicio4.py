
rango = int(input('Ingresa el primer rango de numeros : '))
rango2 = int(input('Ingresa el segundo rango de numeros : '))

if rango > rango2 : 
	print('El primer rango debe ser menor al segundo rango')
else:
	for j in range(rango, rango2  + 1) :
		if j % 2 != 0 :
			print(j) 
		continue