
def medida(*tupla) :
	for i in tupla :
		print(i)
	return len(tupla)

print(medida(1, 2, 3, 4, 5))