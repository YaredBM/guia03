#EJERCICIO 05
#Introducir una cadena de caracteres e indicar si es un palíndromo.
#Una palabra palíndroma es aquella que se lee igual adelante que atrás.


palabra=str(input("Ingrese una palabra: "))
reverso=palabra[::-1]
if palabra==reverso:
    print("La palabra es un palíndromo.")
else:
    print("No es un palíndromo")
#Se utiliza el [::-1] para indicar que la cadena debe escribirse de derecha
#a izquierda y de uno en uno, es decir, lado contrario al que fue escrita,
#indicando de esta manera variable=cadena[::-1]
