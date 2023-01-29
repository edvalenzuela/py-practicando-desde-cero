
class Estudiante():
  def __init__(self, nombre, nota) :
    self.nombre = nombre
    self.nota = nota
  
  def imprimir(self):
    print('Nombre: {} \nNota: {}'.format(self.nombre, self.nota))
  
  def resultados(self):
    if self.nota < 4:
      print('Has reprobado')
    else :
      print('Has aprobado')

estudiante = Estudiante('Eduardo', 4)
estudiante.imprimir()
estudiante.resultados()