hora = int(input("Que hora ingresastes: "))

if hora >= 6 and hora <= 11:
    print("jornada de mañana")

elif hora >= 12 and hora <= 17:
    print("jornada de tarde")

elif hora>= 18 and hora <= 22:
    print("jornada de noche")

else:
    print("fuera de horario")