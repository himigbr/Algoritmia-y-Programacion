day = input("Ingrese un día de la semana: ").lower()

if day == "lunes":
    print("Es Lunes")
elif day == "viernes":
    print("Es Viernes")
elif day in ("sábado", "sabado", "domingo"):
    print("FDS")
else:
    print("Que dia es hoy?, Con quien estoy?")