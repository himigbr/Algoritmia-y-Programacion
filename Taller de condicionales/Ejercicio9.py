entrada = input("Ingrese la fecha actual (formato 'día, DD/MM'): ").strip()

# Separamos el día de la semana y la fecha
partes = entrada.split(",") # La funcion split() divide la cadena en partes usando la coma como separador
dia = partes[0].strip().lower() # Tomamos la primera parte (día de la semana) y la convertimos a minúsculas para facilitar la comparación
fecha = partes[1].strip() # Tomamos la segunda parte (fecha) y eliminamos espacios en blanco

# Separamos día (DD) y mes (MM)
dd_str, mm_str = fecha.split("/") # Usamos la misma funcion ahora para dividir la fecha en día y mes
d = int(dd_str) # Convertimos el día a un número entero
m = int(mm_str) # Convertimos el mes a un número entero

dias = ("lunes", "martes", "miércoles", "miercoles", "jueves", "viernes")

# Si ponen el dia que no es o el dia o el mes no son validos, mostramos un mensaje de error
if (dia not in dias) or (d < 1 or d > 31) or (m < 1 or m > 12):
    print("Se produjo un error.")
else:
    # Lunes (Inicial), Martes (Intermedio), Miércoles (Avanzado)
    if dia in ("lunes", "martes", "miércoles", "miercoles"):
        examenes = input("¿Se tomaron exámenes hoy? (s/n): ").strip().lower() # No nos complicamos con mayúsculas o minúsculas, solo nos interesa la respuesta
        if examenes in ("s", "si", "sí"):
            aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
            no_aprobados = int(input("Ingrese la cantidad de alumnos no aprobados: "))
            total_alumnos = aprobados + no_aprobados
            
            if total_alumnos > 0:
                porcentaje = (aprobados / total_alumnos) * 100
                print(f"Porcentaje de aprobados: {porcentaje:.2f}%")
            else:
                print("No se registraron alumnos evaluados.")

    # Jueves (Práctica hablada)
    elif dia == "jueves":
        asistencia = float(input("Ingrese el porcentaje de asistencia a clase (0 - 100): "))
        if asistencia > 50:
            print("asistió la mayoría")
        else:
            print("no asistió la mayoría")

    # Viernes (Inglés para viajeros)
    elif dia == "viernes":
        if (d == 1 and m == 1) or (d == 1 and m == 7):
            print("Comienzo de nuevo ciclo")
            cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel = float(input("Ingrese el arancel en $ por alumno: "))
            ingreso_total = cantidad_alumnos * arancel
            print(f"Ingreso total del ciclo: ${ingreso_total:.2f}")