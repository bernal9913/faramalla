#codigo de intro

#a = int(input("Inserte un numero: "))
#b = int(input("Inserte un numero: "))
#c = int(input("Inserte un numero: "))
a = 1
b = 2
c = 3
mayor = max(a,b,c)
menor = min(a,b,c)
print("El mayor de los numeros ingresados es: ", mayor)
print("El menor de los numeros ingresados es: ", menor)

print("El número mas grande entre {}, {} y {} es: {} y el mas pequenio es: {}".format(a,b,c,mayor,menor))



## ejercicio 1
# programa de conversiones
print("Programa para convertir grados farenheit a celsius")
a = int(input("Ingrese los grados farenheit: "))
calc = ((a-32)*5)/9
print("La temperatura en grados celsius es: {}".format(calc))
## ejercicio 2
# programa de conversion de euros a libras
print("Programa para convertir libras a euros")
a = float(input("Ingrese la cantidad de libras: "))
calc = a*1.19
print("El cambio total de: {}€ a: {}£".format(a,calc))