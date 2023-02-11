#EJERCICIO 01
#Pide una cadena y un carácter por teclado y
#muestra cuantas veces aparece el carácter en la cadena.

frase=str(input("Ingrese una oración: "))
cara=str(input("Ingrese una letra: "))
cant=frase.count(cara)
print("La cantidad de veces que aparece ",cara," es ",cant)

#El atributo .count en frase.count se utiliza para contar el número de veces
#que aparece la letra en la oración y habiendo definido una variable para
#el resultado de número de veces que aparece.
