from random import uniform #Usamos uniform de random para generar la lista de 24 muestras

def calcular_promedio(lista):
    return 0 if not lista else sum(lista)/len(lista) #Una forma corta de escribir un if else

def obtener_extremos(lista):
    return 0 if not lista else (min(lista), max(lista)) #devuelve una tupla con el minimo y el maximo

def contar_sobre_promedio(lista):
    if not lista: #Si no hay elementos en la lista devuelve 0
        return 0
    promedio = calcular_promedio(lista) #Reciclamos una funcion anterior para el promedio
    return len([x for x in lista if x > promedio]) #Itera sobre la lista y usa condicionales en una sola linea

#Probando las funciones
if __name__ == "__main__":
    lista = [uniform(0.95, 1.05) for _ in range(24)] #Siendo una subestacion, los valores son en pu
    lista = [round(x, 2) for x in lista] #Redondeamos a 2 decimales para verlo mejor
    print("\nlista:", lista)
    print(f"\nPromedio: {calcular_promedio(lista):.2f}")
    print(f"\nExtremos: {obtener_extremos(lista)}")
    print(f"\nSobre el promedio: {contar_sobre_promedio(lista)}", "\n")