#EJERCICIO 06
#Escribir funciones que dada una cadena de caracteres:
#•Imprima los dos primeros caracteres.
#•Imprima los tres últimos caracteres.
#•Imprima dicha cadena cada dos caracteres. Ej.: recta debería imprimir rca
#•Imprima la cadena en un sentido y en sentido inverso. Ej: reflejo imprime reflejoojelfer.


# Input the string from the user
frase = input("Ingresa una palabra o frase: ")
#Ultimos dos caracteres
ult_dos_caracteres = frase[:2]
print("Primeros dos caractéres:", ult_dos_caracteres)
#Ultimos dos caracteres
ult_tres_caracteres = frase[-3:]
print("Ultimos tres caracteres:", ult_tres_caracteres)
#Cada dos caracteres
print("Cada dos caracteres:", end=" ")
for i in range(0,len(frase),2):
    print(frase[i], end="")
print()
#Reflejo
print("Reverso e inverso:", frase+frase[::-1])

##Se puede utilizar el [::*valor], ya que de esta forma indicamos el principio
##o le final en que querramos partir una frase o palabra, Ejemplo:
##[:2]=empezará a contar desde la letra inicial y se detendrá en la numero 2
##ya que no posee el 
