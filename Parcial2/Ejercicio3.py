'''
Para implementar un sistema de inventario de componentes electronicos se usaron las funciones pedidas en el enunciado,
la forma en la que se manipula el inventario es mediante la indexacion de sus llaves y la manipulacion de sus valores,
que son a su vez diccionarios con las llaves cantidad y precio. dic[name] = {'cantidad': cant, 'precio': price}

Para el funcionamiento principal se implemento un ciclo while que permite al usuario elegir entre las diferentes funciones
del programa y se le pide al usuario que ingrese los datos necesarios para cada funcion, ademas de que se le da la opcion 
de salir del programa.
'''

def agregar_componente(dic, name, cant, price):
    if name in dic:
        dic[name]['cantidad'] += cant
        dic[name]['precio'] = price
    else:
        dic[name] = {'cantidad': cant, 'precio': price}

def eliminar_componente(dic, name):
    if name in dic:
        del dic[name]
    else:
        print(f"El componete '{name}' no existe en el diccionario.") #Por si el componente no existe en el diccionario

def calcular_valor_total(dic):
    total = 0
    for comp in dic.values(): #Recorremos los valores del diccionario y los vamos multiplicando y sumando al total
        total += comp['cantidad'] * comp['precio']
    return total

def mostrar_inventario(dic):
    if not dic: #Por si el diccionario esta vacio
        return "el inventario esta vacio"
    inventario = "inventario:\n"
    for name, comp in dic.items(): #Recorremos el diccionario y vamos agregando los componentes al string inventario
        inventario += f"{name}: Cantidad: {comp['cantidad']}, Precio: {comp['precio']}\n"
    return inventario

#Funcionamiento principal
if __name__ == "__main__":
    inventario = {}
    while True:
        print("\nOpciones:")
        print("1. Agregar componente")
        print("2. Eliminar componente")
        print("3. Calcular valor total del inventario")
        print("4. Mostrar inventario")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            name = input("Ingrese el nombre del componente: ")
            cant = int(input("Ingrese la cantidad: "))
            price = float(input("Ingrese el precio: "))
            agregar_componente(inventario, name, cant, price)
            print(f"Componente '{name}' agregado/actualizado.")
        
        elif opcion == '2':
            name = input("Ingrese el nombre del componente a eliminar: ")
            eliminar_componente(inventario, name)
        
        elif opcion == '3':
            total = calcular_valor_total(inventario)
            print(f"Valor total del inventario: {total}")
        
        elif opcion == '4':
            print(mostrar_inventario(inventario))
        
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")