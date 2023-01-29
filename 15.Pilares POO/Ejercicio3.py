
class Fabrica():
  def __init__(self, llantas, color, precio):
    self.llantas = llantas
    self.color = color
    self.precio = precio

class Carro(Fabrica):
  def datos(self):
    print("La cantidad de llantas es de: ", self.llantas)
    print("El color del carro es: ", self.color)
    print("El precio del carro es de: $", self.precio)

class Moto(Fabrica):
  def datos(self):
    print("La cantidad de llantas de la moto: ", self.llantas)
    print("El color de la moto es: ", self.color)
    print("El precio de la moto es de: $", self.precio)
  
carro = Carro(2, 'Negro', 4000)
carro.datos()