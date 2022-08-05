dolar_euro = 0.91
libra_euro = 1.18
total = 0
cantidad = float(input("Introduzca la cantidad: "))
opcion = input("""Como desea hacer la conversion de divisa?
A - Dolar a Euro
B - Euro a Dolar
C - Libra a Euro
D - Euro a Libra
""")
if opcion == "A":
    total = cantidad * dolar_euro
elif opcion == "B":
    total = cantidad / dolar_euro
elif opcion == "C":
    total = cantidad * libra_euro
elif opcion == "D":
    total = cantidad / libra_euro
else:
    print("Cambio de divisa no valido")
    exit()
print("El cambio total es: {}".format(total))