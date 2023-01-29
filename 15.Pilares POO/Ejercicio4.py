
class Marino():
  def hablar(self):
    print("Hola...")
    
class Pulpo(Marino):
  def hablar(self):
    print("Soy un pulpo")

class Foca(Marino):
  def hablar(self, mensaje):
    print(mensaje)
    
marino = Marino()
marino.hablar()
    
pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Hola, Soy una foca")