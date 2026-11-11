def promsim(dic):
    for k, v in dic.items():
        prom = sum(v) / len(v)
        print(f"{k}: {prom:.2f}")
    return

def prompon(dic):
    out = {}
    percent = (0.3, 0.3, 0.4)
    for k, v in dic.items():
        prom = sum((v[i] * percent[i] for i in range(len(v))))
        out[k] = prom
    return out

def prommax(dic):
    proms = prompon(dic)
    max_prom = max(proms.values())
    for k, v in proms.items():
        if v == max_prom:
            print(f"{k} tiene el promedio mas alto: {v:.1f}")
    return

def aprob(dic):
    proms = prompon(dic)
    for k, v in proms.items():
        if v >= 3.0: print(f"{k} aprobo con promedio: {v:.1f}")
    return

def Mcgonagal(dic):
    proms = prompon(dic)
    for k, v in proms.items():
        estado = "aprobo" if v >= 3.0 else "reprobo"
        print(f"{k} esta {estado} con promedio de {v:.1f} la clase de Mcgonagal")
    return

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