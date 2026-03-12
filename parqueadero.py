continuar = "si"
while continuar.lower() == "si":
    horas = int(input("¿cuantas horas duraste?: "))
    if horas >1:
        horas_adicionales = horas - 1
        total_adicional = horas_adicionales * 3000
        total = 5000 + total_adicional 
    else: total = 5000
    print("el valor es de", total)
    continuar = input("Quieres saber otra hora?:  (si/no) ")