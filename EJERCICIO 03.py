#EJERCICIO 03
#Si tenemos una cadena con un nombre y apellidos, realizar un programa
#que muestre iniciales en mayúsculas y segunda letra en minúscula. 
#Ejemplo:  Javier Cibrián Torres  JaCiTo 

nom=str(input("Ingrese su primer nombre: "))
ape1=str(input("Ingrese su primer apellido: "))
ape2=str(input("Ingrese su segundo apellido: "))
letra1n=nom[0]
letra2n=nom[1]
letra1a1=ape1[0]
letra2a1=ape1[1]
letra1a2=ape2[0]
letra2a2=ape2[1]
print(letra1n+letra2n+letra1a1+letra2a1+letra1a2+letra2a2)

#Usamos el + en vez de , para concatenar las variables de las letras
#dando como resultado JaCiTo
