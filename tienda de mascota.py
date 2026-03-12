mascota = input("¿que animal es tu mascota?:").strip().lower()

if mascota == "perro":
    print("pienso para perros")

elif mascota == "gato":
    print("pienso para gatos")

elif mascota == "conejo":
    print("heno o verduras para conejos")

else:
    print("error: mascota no reconocida")

