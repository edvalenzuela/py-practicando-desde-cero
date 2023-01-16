
class FabricaTelefonos():
	marca = 'Huawei'
	color = 'Negro'
	memoriaRam = 32
	almacenamiento = 128

	def llamar(self, mensaje):
		return mensaje
	
	def escucharMusica(self):
		print('Estas escuchando Musica')

telefono = FabricaTelefonos()
telefono.marca
telefono.color
telefono.memoriaRam
telefono.almacenamiento
telefono.llamar

print(telefono.almacenamiento)
print(telefono.llamar('Hola, ¿Con quien hablo?'))
telefono.escucharMusica()