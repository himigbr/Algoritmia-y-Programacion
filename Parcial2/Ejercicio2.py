def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return "Error: Division por cero" if b==0 else a / b #Una condicion para evitar la division por cero

def factorial(n):
    if n < 0:
        return "El factorial de un negativo no esta definido" #Para evitar el calculo de un factorial negativo
    return 1 if n == 0 or n == 1 else n * factorial(n - 1) #Recursividad para calcular el factorial

def inversa(x):
    return "Error inversa de cero" if x==0 else 1/x #Para evitar la division por cero al calcular la inversa

def potencia(base, exponente): 
    if base == 0 and exponente == 0: #Para evitar indeterminacion
        return "Error: 0^0 no esta definido"
    if exponente % 1 != 0: #Para evitar el calculo con exponentes no enteros
        return "Error: La calculadora solo soporta exponentes enteros"
    resultado = 1
    if exponente < 0: #Para calcular la potencia de un numero con exponente negativo
        base = inversa(base) #calculamos la inversa de la base
        exponente = -exponente #Le cambiamos el signo al exponente
    for _ in range(exponente): #Multipicamos la base por si misma tantas veces como indique el exponente
        resultado = multiplicacion(resultado, base)
    return resultado

def raiz_cuadrada(x): #Usamos metodo de aproximacion binaria para calcular la raiz cuadrada de un numero (Idea de Gemini)
    if x < 0: #Para evitar indeterminaciones en los reales
        return "Raiz cuadrada de un numero negativo no esta definida"
    elif x == 0: #Raiz de cero es cero
        return 0
    else:
        liminf = 0 #Establecemos el limite inferior de la aproximacion
        limsup = x if x >= 1 else 1 #Establecemos el limite superior de la aproximacion, si x es menor que 1, el limite superior es 1
        contador = 0 #Un contador para evitar ciclos infinitos (Por si las moscas)
        while limsup - liminf > 1e-10: #Precision de 10 decimales
            candidato = multiplicacion((suma(liminf, limsup)), 0.5) #Calculamos el candidato a raiz cuadrada como el promedio de los limites inferior y superior
            if multiplicacion(candidato, candidato) < x: #Si el candidato al cuadrado es menor que x, actualizamos el limite inferior
                liminf = candidato
            else: #Si es el caso contratio, actualizamos el limite superior
                limsup = candidato
            contador += 1
            if contador == 100: #Si no se llega a un resultado en 100 iteraciones, se devuelve un error
                return "Error: No se pudo aproximar la raiz cuadrada"
        return round(candidato, 4)

#pruebas
if __name__ == "__main__":
    print("Suma: ", suma(2,3)) #Debe dar cinco
    print("Resta: ", resta(5,2)) #Debe dar tres
    print("Multiplicacion: ", multiplicacion(4,5)) #Debe dar veinte
    print("Division: ", division(10,2)) #Debe dar cinco
    print("Division por cero: ", division(10,0)) #Debe dar error
    print("Factorial: ", factorial(5)) #Debe dar 120
    print("Factorial negativo: ", factorial(-5)) #Debe dar error
    print("Inversa: ", inversa(4)) #Debe dar 0.25
    print("Inversa de cero: ", inversa(0)) #Debe dar error
    print("Potencia: ", potencia(2,3)) #Debe dar 8
    print("Potencia con exponente negativo: ", potencia(2,-3)) #Debe dar 0.125
    print("Potencia con base y exponente cero: ", potencia(0,0)) #Debe dar error
    print("Potencia con exponente no entero: ", potencia(2,0.5)) #Debe dar error
    print("Raiz cuadrada: ", raiz_cuadrada(16)) #Debe dar 4
    print("Raiz cuadrada de un numero negativo: ", raiz_cuadrada(-16)) #Debe dar error
    print("Raiz cuadrada de cero: ", raiz_cuadrada(0)) #Debe dar 0
    print("Raiz cuadrada de un numero menor que 1: ", raiz_cuadrada(0.25)) #Debe dar 0.5