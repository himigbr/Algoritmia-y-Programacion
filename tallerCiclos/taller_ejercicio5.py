'''
Este script cumple con la peticion del quinto ejercicio del taller
Simula el recorrido de un borracho en una ciudad cuadrada
Mediante un ciclo for de 100 pasos, el borracho elige una dirección al azar (Norte, Sur, Este, Oeste) y se mueve en esa dirección
Se imprime la dirección elegida y la posición actual del borracho después de cada paso
Y luego mostramos donde fue que se echo a dormir.
'''

import random # Importamos el módulo random para poder elegir direcciones al azar

# Inicializamos las coordenadas del borracho en el origen (0, 0) ***parido borracho
x = 0
y = 0
pasos_totales = 100
# El man no sabe ni pa donde ir
direcciones = ["Norte", "Sur", "Este", "Oeste"]

print(f"Inicio del recorrido en la intersección: ({x}, {y})")

for paso in range(1, pasos_totales + 1):
    direccion_elegida = random.choice(direcciones)
    
    if direccion_elegida == "Norte":
        y += 1
    elif direccion_elegida == "Sur":
        y -= 1
    elif direccion_elegida == "Este":
        x += 1
    elif direccion_elegida == "Oeste":
        x -= 1

    # Imprimimos la dirección elegida y la posición actual del borracho después de cada paso
    print(f"Paso {paso:3d}: {direccion_elegida:<5} -> Posición actual: ({x}, {y})")

# Aqui se echo a dormir
print(f"Recorrido finalizado tras {pasos_totales} intersecciones.")
print(f"Ubicación final del borracho: ({x}, {y})")