
class Calculadora():
  
  def __init__(self):
    self.num1 = int(input('Número 1: \n')) 
    self.num2 = int(input('Número 2: \n'))
  
  def suma(self):
    print("{} + {} =".format(self.num1, self.num2),(self.num1 + self.num2))
  
  def resta(self):
    print("{} - {} =".format(self.num1, self.num2),(self.num1 - self.num2))
  
  def multiplicacion(self):
    print("{} x {} =".format(self.num1, self.num2),(self.num1 * self.num2))
  
  def division(self):
    try:
      print("{} / {} =".format(self.num1, self.num2),(self.num1 / self.num2))
    except ZeroDivisionError:
      print("No se puede dividir entre cero")

calculadora = Calculadora()
calculadora.division()