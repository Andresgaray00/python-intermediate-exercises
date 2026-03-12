siguiente_usuario = "si"

while siguiente_usuario.lower() == "si":

    mascota = input("¿que animal es tu mascota?: ").strip().lower()

    if mascota == "perro":
        print("concentrado para perros")

    elif mascota == "gato":
        print("comida para gatos")

    elif mascota == "conejo":
        print("heno o verduras para conejos")

    else:
        print("error: mascota no reconocida")

    siguiente_usuario = input("quieres ingresar una nueva mascota (si/no) ")

