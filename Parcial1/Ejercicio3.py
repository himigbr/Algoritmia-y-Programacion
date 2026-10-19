#Es un buble infinito, para detenerlo se debe precionar Ctrl + C en la terminal

import time #Importamos time para la simulacion de tiempos

spinner = ['/', '-', '\\', '|'] #Creamos un spinner para que el funcionamiento se pueda apreciar
BolsasEmpacadas = 0 #Iniciamos un contador de bolsas empacadas
time.sleep(2) #Espera inicial

while True:
    SensorChuspa = True #Simulamos la detección del sensor
    if SensorChuspa == True:
        print("Se Detecto una bolsa, iniciando proceso...")
        time.sleep(3) #Simulamos el tiempo de espera para iniciar el proceso

        TInicioFill = time.time() #Guardamos el tiempo de inicio del proceso
        i = 0 #Variable cambiante para que el spinner funcione correctamente
        while (time.time() - TInicioFill) < 9: #Tiempo de llenado de la bolda
            print(f"\rLlenando bolsa {spinner[i % 4]}", end="", flush=True) #Comandos necesarios para que se sobreescriba la misma linea y se vea la animacion
            time.sleep(0.5) #Tiempo de actualización del spinner
            i += 1
        print("\nBolsa llena, iniciando proceso de sellado...")
        time.sleep(3)

        TInicioSeal = time.time() #Tiempo de inicio de proceso de sellado
        i = 0 #Variable cambiante para que el spinner funcione correctamente
        while (time.time() - TInicioSeal) < 6: #Tiempo de sellado de la bolda
            print(f"\rSellando bolsa {spinner[i % 4]}", end="", flush=True)
            time.sleep(0.5) #Tiempo de actualización del spinner
            i += 1
        print("\nBolsa sellada, iniciando proceso de empacado...")
        time.sleep(3)

        TInicioPack = time.time() #Tiempo de inicio del proceso de empacado
        i = 0 #Variable cambiante para que el spinner funcione correctamente
        while (time.time() - TInicioPack) < 9: #Tiempo de empacado de la bolda
            print(f"\rEmpacando bolsa {spinner[i % 4]}", end="", flush=True)
            time.sleep(0.5)
            i += 1
        print(f"\nBolsas empacadas: {BolsasEmpacadas + 1}")
        BolsasEmpacadas += 1
        time.sleep(3)

    else:
        print("\rNo se detecto ninguna bolsa, esperando...", end="", flush=True) #Por si se simula que no hay bolsa
        time.sleep(3)