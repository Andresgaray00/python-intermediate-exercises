fresa = 0
vainilla = 0
chocolate = 0

for i in range(0, 5, 1):
    sabor = input("Ingresa el sabor de helado que desea: ")

    if sabor == "fresa":
        fresa += 1
    elif sabor == "vainilla":
        vainilla += 1
    else:
        chocolate += 1

print("fresa:", fresa)
print("vainilla:", vainilla)
print("chocolate:", chocolate)