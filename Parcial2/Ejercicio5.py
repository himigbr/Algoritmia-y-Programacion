from random import randint as rd #Importamos la funcion randint de la libreria random para generar el numero entero aleatorio

def elegir_dificultad():
    print("Selecciona la dificultad del juego:")
    print("1. Facil")
    print("2. Medio")
    print("3. Dificil")
    while True:
        try: #Para que el programa no falle ni se detenga por un error en la entrada del usuario
            dificultad = int(input("Ingrese el número correspondiente a la dificultad: "))
            if dificultad in [1, 2, 3]: #Algunos condicionales para que la funcion devuelva el numero de intentos
                if dificultad == 1:
                    print("Has seleccionado dificultad Fácil. Tendrás 10 intentos.")
                    return 10
                elif dificultad == 2:
                    print("Has seleccionado dificultad Media. Tendrás 6 intentos.")
                    return 6
                else:
                    print("Has seleccionado dificultad Difícil. Tendrás 3 intentos.")
                    return 3
            else:
                print("Por favor, ingrese un número válido (1, 2 o 3).")
        except ValueError: #Para que el programa no se detenga si el usuario ingresa un string
            print("Entrada inválida. Por favor, ingrese un número.")

def generar_numero():
    return rd(1, 100) #Usamos la funcion randint para generar el numero aleatorio entre 1 y 100

def jugar(intentos):
    intentojuego = 0 #Variable para contar los intentos
    FrecSec = generar_numero() #Generamos el numero secreto
    print("\n¡Comienza el juego!") #Un lindo mensaje
    for intento in range(intentos): #Usamos el ciclo for para que itere el numero de intentos segun la dificultad elegida
        intentojuego += 1
        while True: #Usamos while para que el programa siga pidiendo un numero hasta que el usuario ingrese uno valido
            try: #Para que el programa no falle si el usuario ingresa un string
                adivinanza = int(input(f"Intento {intento + 1}/{intentos}: Adivina la frecuencia de resonancia (1-100) Hz: ")) #Aqui es donde el usuario intenta adivinar
                if 1 <= adivinanza <= 100: #Si el numero es valido rompe el ciclo while y continua con el juego
                    break
                else: #Si el numero es invalido imprime un mensaje y vuelve a pedir el numero
                    print("Por favor, ingrese un número entre 1 y 100.")
            except ValueError: #Para que el programa no se detenga si el usuario ingresa un string
                print("Entrada inválida. Por favor, ingrese un número.")

        #Condicionales para dar pistas al usuario sobre si su adivinanza es mayor o menor que la frecuencia secreta
        if adivinanza < FrecSec:
            print("La frecuencia es mas alta. Intenta de nuevo.")
        elif adivinanza > FrecSec:
            print("La frecuencia es mas baja. Intenta de nuevo.")
        else:
            resultado = True #Si el usuario adivinar creamos una variable de para guardar el resultado, en este caso booleana
            print(f"¡Felicidades! Has adivinado la frecuencia secreta: {FrecSec} Hz") #Si el usuario adivina la frecuencia secreta le mostramos un lindo mensaje de felicidades
            return resultado, intentojuego  #Aca el return funciona como un break para salir del ciclo for y terminar el juego y ademas devuelve los datos para el historial

    print(f"Lo sentimos, no has adivinado la frecuencia secreta: {FrecSec} Hz")
    resultado = False 
    return resultado, intentojuego #Devolvemos el resultado y el numero de intentos para guardarlos en el historial

def guardar_historial(resultado, intentos):
    '''Para esta funcion usamos with para que el archivo solo se abra y se cierre cuando se ejecute la funcion,
    ademas usamos el modo "a" para que el archivo se abra en modo append y no se borre lo que ya estaba escrito'''

    if resultado:
        with open("historial_juego.txt", "a") as archivo: #Si el usuario gana, guardamos el resultado en un archivo de texto
            archivo.write(f"Resultado: Ganado, Intentos: {intentos}\n")
    else:
        with open("historial_juego.txt", "a") as archivo: #Si el usuario pierde, guardamos el resultado en un archivo de texto
            archivo.write(f"Resultado: Perdido, Intentos: {intentos}\n")

if __name__ == "__main__": #Para que el programa solo se ejecute si es el archivo principal y no si es importado
    print("\n¡Bienvenido al juego de sintonia e inspección!")#Mensaje de bienvenida
    print("Debes adivinar la frecuencia de resonancia secreta del filtro.")
    print("\nPero primero")
    intentos = elegir_dificultad() #Llamamos las funciones para arrancar el programa
    resultado, intentos = jugar(intentos)
    guardar_historial(resultado, intentos) #Guardamos el resultado en el historial