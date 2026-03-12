continuar = "si"
while continuar.lower() == "si": 

    edad = int(input("ingresa tu edad:"))

    if edad < 0:
        print("la edad no puede ser negativa")

    elif edad <= 17:
        print("clase juvenil")

    elif edad <= 59:
        print("clase general")

    else:
       print("clase senior")
    continuar = input("quieres ingresar otra edad: (si/no)")
