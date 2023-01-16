
print('Elige tu candidato [Candidato A Rojo] - [Candidato B Verde] - [Candidato C Azul] ')
opcion = input('Ingresa la opcion de tu candidato: ')

if(opcion.upper() == 'A'):
	print('Usted escogio el candidato Rojo: {}'. format(opcion))
elif(opcion.upper() == 'B'):
	print('Usted escogio el candidato Verde: {}'. format(opcion))
elif(opcion.upper() == 'C'):
	print('Usted escogio el candidato Azul: {}'. format(opcion))
else :
	print('Opcion erronea: {}'. format(opcion))