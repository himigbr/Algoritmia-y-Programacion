def selitem(dic): #Funcion para identificar que es lo que el cliente desea comprar y devolver el precio del producto
    itemno = 1 # Variable para enumerar los productos en el diccionario
    print("¿Qué producto deseas comprar?\n") #Mensajito para el usuario
    for k, v in dic.items(): #Ciclo for para recorrer el diccionario y mostrar los productos y sus precios
        print(f"{itemno}. {k}: ${v}")
        itemno += 1 #Se va sumando 1 a la variable itemno para enumerar los productos, sirve para cualquier cantidad de productos que se agreguen al diccionario

    item = int(input("\nIngrese el número del producto que desea comprar: ")) #Aqui el usuario ingresa el nro del producto que quiere comprar
    while True: #Cilo para que el programa siga pidiendo un numero hasta que el usuario ingrese uno valido
        try:
            if item in range(1, itemno-1): #El range sirve para indicarle al programa que el usuario solo puede ingresar un numero entre 1 y la cantidad de productos que hay en el diccionario, si el usuario ingresa un numero valido rompe el ciclo while y continua con el programa
                break
            else: #Si ingresa un numero invalido imprime un mensaje y vuelve a pedir el numero
                print(f"Por favor, ingrese un número válido entre 1 y {itemno - 1}.")
                item = int(input("Ingrese el número del producto que desea comprar: "))
        except ValueError: #Para que el programa no se detenga si el usuario ingresa un string
            print("Entrada inválida. Por favor, ingrese un número.")
            item = int(input("Ingrese el número del producto que desea comprar: "))


    itemname = list(dic.keys())[item - 1] #Creamos una lista unicamente con la clave del diccionario que el usuario selecciono indexando la entrada del usuario y restando 1 para que coincida con el indice de la lista
    itemprice = dic[itemname] #indexamos el diccionario con la clave que se selecciono para obtener el precio del producto
    print(f"\nHas seleccionado: {itemname} con un precio de ${itemprice}.") #Mensaje de seleccion del producto y su precio
    return itemprice #Devolvemos el precio del producto para que pueda ser usado en la funcion cobrar

def cobrar(price): #Funcion para cobrar el producto seleccionado por el usuario y devolver el cambio si es necesario, ademas se comprueb que el usuario ingrese un monto valido y suficiente para pagar el producto
    while True: #Ciclo para para que el programa siga pidiendo un monto hasta que el usuario ponga uno valido y ademas suficiente
        try: #Intente cobrar el producto, si el usuario ingresa un string el programa no se detendra y le pedira que ingrese un numero
            pago = int(input("Ingrese el monto a pagar: "))
            if pago >= price: #Verificamos que el monto ingresado sea suficiente para pagar el producto, si es asi calculamos el cambio y mostramos un mensaje de pago recibido y el cambio
                cambio = pago - price #Guardamos el valor del cambio
                print(f"\nPago recibido: ${pago}. Su cambio es: ${cambio}.")
                break #Rompemos el ciclo while para que el programa continue con el resto del codigo
            else: #Si el monto no es suficiente vuelva y cobre
                print(f"El monto ingresado es insuficiente. El precio del producto es ${price}.")
        except ValueError: #Si ingresa un string el programa no se detendra y le pedira que ingrese un numero
            print("Entrada inválida. Por favor, ingrese un número.")
    return #Detenemos la funcion para que no devuelva nada, ya que el cambio se muestra en pantalla y no es necesario devolverlo
    
items = {"Cocacola": 4000,
         "Pepsi": 3500,
         "Fanta": 3000,
         "Sprite": 2500,
         "Agua": 2000}

if __name__ == "__main__": #Si el archivo se ejecuta directamente, se ejecuta el codigo dentro del if, si se importa como modulo no se ejecuta
    print("Bienvenido a la dispensadora de bebidas\n") #Mensajito de bienvenida
    #Ejecutamos las funciones para que el usuario pueda seleccionar un producto y pagar por el
    price = selitem(items)
    cobrar(price)