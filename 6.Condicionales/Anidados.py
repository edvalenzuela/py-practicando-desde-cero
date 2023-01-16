nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

'''if nombre.lower() == "juan" and edad >= 18 :
	print("Tu eres juan") 
else :
	print("No eres juan")'''

if nombre.lower() == "juan" :
	if edad >= 18:
		print("Eres Juan y tienes mayoria de edad")
	else:
		print("Eres Juan, pero, NO tienes mayoria de edad")
else :
	print("Tu NO eres juan")