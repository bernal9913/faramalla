print("Programa de eligibilidad de descuento")
edad = int(input("Ingrese su edad: "))
tipo_carnet = input("Ingrese su tipo de carnet: ")
# E = Estudiante
# P = Pensionado
# F = Familia grande
# N = Nada
if tipo_carnet == "N":
    print("Sin carnet")
    if edad < 10:
        print("Descuento aplicado por tener menos de 10 años")
    else:
        print("Edad no valida para descuento")
if tipo_carnet == "E":
    if 25 < edad < 35:
        print("Descuento aplicado por estudiante")
    else:
        print("Edad no valida para descuento")
if tipo_carnet == "P":
    if edad < 65:
        print("Descuento de pensionado aplicado")
    else:
        print("Edad no valida para descuento")
if tipo_carnet == "F":
    print("Descuento aplicado por ser culiador como su tata")