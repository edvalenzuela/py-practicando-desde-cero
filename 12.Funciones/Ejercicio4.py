
def total() :
	monto = float(input('Ingresa el valor del producto que estas pagando: '))
	iva = int(input('Ingrese el valor del IVA: '))


	if iva != 0 :
		if iva > 0 :
			totalPagar = ((monto * iva) / 100) + monto
			return totalPagar
		else :
			return 'El monto del IVA es negativo. No podemos avanzar'
	else:
		totalPagar = (monto * 0.21) + monto
		return totalPagar

print('El total de su monto es: ', total())