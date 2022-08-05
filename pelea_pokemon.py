import random
import os
print("Pelea belica de pokemon")
vida_inicial_pikachu = 50
vida_inicial_squirtle = 50
vida_pikachu = 50
vida_squirtle = 50
while vida_squirtle > 0 and vida_pikachu > 0:
    os.system('clear')
    barra_vida_squirtle = int(vida_squirtle * 10 / vida_inicial_squirtle)
    barra_vida_pikachu = int(vida_pikachu * 10 / vida_inicial_pikachu)
    print("Squirtle: " + "#" * barra_vida_squirtle + " {} ".format(vida_squirtle))
    print("Pikachu: " + "#" * barra_vida_pikachu + " {} ".format(vida_pikachu))
    opcion = input("""
    Que deseas hacer?:
    A - Placaje
    B - Pistola agua
    C - Burbuja
    """)
    if opcion == "A":
        print("Haz usado placaje")
        vida_pikachu -= 10
    elif opcion == "B":
        print("Haz usado pistola agua")
        vida_pikachu -= 20
    elif opcion == "C":
        print("Haz usado burbuja")
        vida_pikachu -= 9
    ataque_pikachu = random.randint(1,3)
    if ataque_pikachu == 1:
        print("Pikachu ha usado Bola Voltio")
        vida_squirtle -= 10
    elif ataque_pikachu == 2:
        print("Pikachu ha usado Onda Trueno")
        vida_squirtle -= 11
    elif ataque_pikachu == 3:
        print("Pikachu tuvo miedo y salto turno")

if vida_squirtle > vida_pikachu:
    print("Squirtle ha ganado")
else:
    print("Pikachu ha ganado")