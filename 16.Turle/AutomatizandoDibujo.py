import turtle

s = turtle.Screen()
t = turtle.Turtle()
i = 0

'''for i in range(4):
  t.fd(100)
  t.rt(90)'''
  
resultado = input('Quieres imprimir una figura? ')

if resultado.lower() == "si":
	while i <= 100:
		t.speed(0)
		t.circle(i)
		i += 10
else:
  print("Oka")

turtle.done()