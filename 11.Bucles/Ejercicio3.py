
i = 0
while( i < 10) :
	i+=1
	print(i)

for k in range(1, 11) :
	print(k)

rango = int(input('Ingresa el primer rango de numeros : '))
rango2 = int(input('Ingresa el segundo rango de numeros : '))

if(rango > rango2) : 
	print('El primer rango debe ser menor al segundo rango')
elif rango == rango2 :
	print('NO pueden ser iguales')
else :
	for j in range(rango, rango2 + 1) :
		print(j)

