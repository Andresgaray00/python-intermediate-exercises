bebida = input ("que bebida deseas:")

cantidad = int(input("cuantas unidades desea:"))

if bebida == "cafe":

    total = 4000 * cantidad
    print("total a pagar:", total)

elif bebida == "te":
    total = 3500 * cantidad
    print("total a pagar:", total)

elif bebida == "jugo":
    total = 5000 * cantidad
    print("total a pagar:", total)

else:
    print("bebida no disponible")

