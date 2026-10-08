candidato = input("Ingrese su candidato (A, B o C): ").upper()

if candidato == "A":
    color = "rojo"
    print("Usted ha votado por el partido " + color)
elif candidato == "B":
    color = "verde"
    print("Usted ha votado por el partido " + color)
elif candidato == "C":
    color = "azul"
    print("Usted ha votado por el partido " + color)
else:
    print("Opción errónea")