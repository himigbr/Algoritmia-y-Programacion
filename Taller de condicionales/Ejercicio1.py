x = float(input("Ingrese un número entre 10 y 50: "))

if 10 <= x <= 50:
    if x == 30:
        print("Ganaste un premio")
    else:
        print("Perdiste")
else:
    print("Número fuera de rango")