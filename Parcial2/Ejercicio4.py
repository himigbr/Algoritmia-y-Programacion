def promsim(dic): #Sacamos el promedio simple de cada estudiante y lo mostramos en pantalla
    for k, v in dic.items(): #Ciclo for para recorrer el diccionario y mostrar el promedio de cada estudiante
        prom = sum(v) / len(v) #Sacamos el promedio sumando las notas de la lista y dividiendo entre la cantidad de notas
        print(f"{k}: {prom:.2f}") #imprimimos el nombre del estudiante y su promedio con 2 decimales
    return #No devolvemos nada ya que solo queremos mostrar el promedio en pantalla

def prompon(dic): #Sacamos el promedio ponderado de cada estudiante y lo devolvemos en un diccionario
    out = {} #Creamos un diccionario vacio para guardar los promedios ponderados
    percent = (0.3, 0.3, 0.4) #Creamos una tupla que nos servira para operar sobre la lista de notas de cada estudiante
    for k, v in dic.items(): #Iteramos sobre los items del diccionario para sacar el promedio de cada estudiante
        prom = sum((v[i] * percent[i] for i in range(len(v)))) #Multiplicamos el valor de cada nota por su porcentaje correspondiente  usando range y len para iterar sobre la lista de notas y sumamos los resultados
        out[k] = prom #Guardamos el promedio ponderado en el diccionario out con la llave del nombre del estudiante
    return out #Devolvemos el diccionario con los promedios ponderados para que pueda ser usado en otras funciones

def prommax(dic): #Sacamos el promedio mas alto de todos los estudiantes y lo mostramos en pantalla
    proms = prompon(dic) #Sacamos el promedio ponderado de cada estudiante y lo guardamos en un diccionario
    max_prom = max(proms.values()) #Sacamos el promedio mas alto usando la funcion max sobre los valores del diccionario de promedios ponderados
    for k, v in proms.items(): #Iteramos sobre los promedios para buscar la clave del valor del promedio mas alto
        if v == max_prom: #Cuando encuentre la clave entonces:
            print(f"{k} tiene el promedio mas alto: {v:.1f}") #Imprima esa clave y el promedio mas alto con 1 decimal
    return

def aprob(dic): #Sacamos los estudiantes que aprobaron y los mostramos en pantalla
    proms = prompon(dic) #Sacamos el promedio ponderado de cada estudiante y lo guardamos en un diccionario
    for k, v in proms.items(): #Iteramos sobre los promedios para buscar los estudiantes que aprobaron
        if v >= 3.0: print(f"{k} aprobo con promedio: {v:.1f}") #Imprimimos solo los estudiantes con promedio mayor o igual a 3
    return #No devolvemos nada ya que solo queremos mostrar los estudiantes aprobados en pantalla

def Mcgonagal(dic): #Funcion bonus
    proms = prompon(dic) #Sacamos promedio ponderado de cada estudiante y lo guardamos en un diccionario
    for k, v in proms.items(): #Iteramos sobre los promedios para buscar los estudiantes que aprobaron y los que reprobaron
        estado = "aprobo" if v >= 3.0 else "reprobo" #Un if else rapido para asignar el estado del estudiante segun su promedio
        print(f"{k} esta {estado} con promedio de {v:.1f} la clase de Mcgonagal") #Imprimimos el estado del estudiante con su promedio
    return #No devolvemos nada ya que solo queremos mostrar el estado de los estudiantes en la clase de Mcgonagal en pantalla

notas = {
    "Harry": [3.8, 4.0, 4.2],
    "Ron": [3.2, 3.8, 2.8],
    "Hemione": [5.0, 5.0, 5.0],
    "Daco": [4.5, 4.2, 5.0],
    "Nevil": [2.5, 3.0, 3.2]
}

#Prueba de las funciones
print("\nPromedio simple: ")
promsim(notas)
print("\nPromedio ponderado: ")
for k, v in prompon(notas).items():
    print(f"{k}: {v:.2f}")
print("\nEstudiante con promedio más alto: ")
prommax(notas)
print("\nEstudiantes aprobados: ")
aprob(notas)
print("\nEstado de los estudiantes en la clase de Mcgonagal: ")
Mcgonagal(notas)