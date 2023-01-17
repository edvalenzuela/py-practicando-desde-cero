
class A():
  def __init__(self):
    self.contador = 0
  
  def	incrementar(self):
    self.contador += 1
  
  def cuenta(self):
    return self.contador

""" a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador) #atributo """

class B():
  def __init__(self):
    self.__contador = 0 #encapsulando poner en privado un atributo y solo puede ser accedido desde la misma clase
  
  def	incrementar(self):
    self.__contador += 1
  
  def cuenta(self):
    return self.__contador

b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
print(b.__contador)