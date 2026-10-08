year = int(input("Ingrese un año: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): #Se usa el modulo para determinar mediante el residuo si es divisible entre 4 y no entre 100 o si es divisible entre 400
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")