#EJERCICIO 02
#Si tenemos una cadena con un nombre y apellidos,
#realizar un programa que muestre las iniciales en minúsculas.
nom=str(input("Ingrese su nombre: "))
ape=str(input("Ingrese su apellido: "))
letra1 = nom[0]
letra1a = ape[0]

if letra1.upper() and letra1a.upper():
    print(letra1.lower(),letra1a.lower())
else:
    print(letra1.upper,letra1a.upper())
   
