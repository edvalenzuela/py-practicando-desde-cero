import math

def areaCuadrado(base, altura) :
	return base * altura

print(areaCuadrado(10, 10))

def areaCirculo(radio) :
	area = math.pi * pow(radio, 2)
	return area

print(areaCirculo(10))