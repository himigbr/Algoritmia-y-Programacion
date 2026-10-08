texto = input("Ingrese una letra: ")

if len(texto) != 1:
    print("No se puede procesar el dato")
else:
    if texto.lower() in ("a", "e", "i", "o", "u"):
        print("es vocal")
    else:
        print("no es vocal")