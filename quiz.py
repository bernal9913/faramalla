text = "Bienvenido al test sobre el queso"

print(text + "\n" + "-" * len(text))
puntuacion = 0
opcion = input("""Pregunta 1: Que haces cuando ves un queso?
A - Salgo corriendo
B - Pruebo uno varios quesos
C - Me la como entera nadie se entera""")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

opcion = input("""Pregunta 2: Que haces cuando ves un queso?
A - Salgo corriendo
B - Pruebo uno varios quesos
C - Me la como entera nadie se entera""")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()