import random
numero_ganador = random.randint(1, 10)
numero_elegido = int(input("Ingrese un numero del 1 al 10: "))
if numero_ganador == numero_elegido:
    print("Haz ganado!!")
if numero_elegido > 10 or numero_elegido < 10:
    print("te mamaste ")

print("El numero ganador era: {}".format(numero_ganador))