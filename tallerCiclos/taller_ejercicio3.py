'''
Este script cumple con la peticion del tercer ejercicio del taller
Es un poco complejo el entender los for anidados por la funcion range y el slicing (recortar)
Lo que hace es que el primer for controla el tamaño de la subcadena que queremos generar, desde 1 hasta n (n+1) 
Porque la funcion range es exclusiva del límite superior, osea que no lo toma en cuenta
El for anidado va cambiando el indice de inicio de la subcadena para obtener todos los resultados
Y la funcion append() agrega la subcadena generada a la lista de subcadenas.
'''

palabra = input("Ingrese una palabra: ").strip()
n = len(palabra)
subcadenas = []

# Este ciclo controla la longitud de las subcadenas que queremos generar, desde 1 hasta n (n+1) porque la funcion range es exclusiva del límite superior
for longitud in range(1, n + 1):
    # Cambia el indice de inicio de la subcadena desde 0 hasta n - longitud + 1 para evitar desbordamiento, es decir, para empezar en la r o en la u o en m como en el ejemplo
    for inicio in range(0, n - longitud + 1):
        sub = palabra[inicio : inicio + longitud] #Usamos slicing para obtener la subcadena desde el índice de inicio hasta el índice de inicio + longitud
        subcadenas.append(sub) #Agregamos la subcadena generada a la lista de subcadenas

print(f"\nSubcadenas de '{palabra}' ordenadas por longitud:")
for sub in subcadenas:
    print(sub)