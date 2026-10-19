from unittest.mock import patch

def Hamburguesa():
    #Preliminares
    Tit = "Bienvenido a IsaMig Burger"
    Men = 'Menú'
    Menu = {
        '1. Hamburguesa sencilla' : 10000,
        '2. Hamburguesa doble' : 15000,
        '3. Hamburguesa Godzilla' : 20000,
        '4. Hamburguesa Supreme' : 25000,
        '5. Hamburguesa Perezosa' : 30000
    }
    LTit = len(Tit)
    LMen = len(Men)
    LTit = (60 - LTit) // 2
    LMen = (60 - LMen) // 2
    Total = 0
    ListBurger = []

    #Menú
    print('='*60)
    print(' '*LTit + Tit)
    print('='*60)
    print(' '*LMen + Men)
    print('='*60)
    for key, value in Menu.items():
        print(f'{key}: ${value}')
    print('='*60)

    #La magia 
    while True:
        option = input('Ingrese el número de la hamburguesa que desea ordenar (1-5) o "salir" para terminar: ')
        if option.lower() == 'salir':
            confirm = input(f'Usted ordeno: \n {", ".join(ListBurger)} \n ¿Su pedido es correcto? (y/n): ')
            if confirm.lower() == 'y':
                break
            else:
                print('Por favor vuelva a ingresar su pedido.')
                ListBurger.clear()
                Total = 0
                continue
        elif option not in ['1', '2', '3', '4', '5']:
            print('Opción inválida. Por favor, ingrese un número del 1 al 5 o "salir".')
            continue
        elif option == '1':
            Total += Menu['1. Hamburguesa sencilla']
            print(f'Se anadió una Hamburguesa sencilla. Total actual: ${Total}')
            ListBurger.append('Hamburguesa sencilla')
            continue
        elif option == '2':
            Total += Menu['2. Hamburguesa doble']
            print(f'Se anadió una Hamburguesa doble. Total actual: ${Total}')
            ListBurger.append('Hamburguesa doble')
            continue
        elif option == '3':
            Total += Menu['3. Hamburguesa Godzilla']
            print(f'Se anadió una Hamburguesa Godzilla. Total actual: ${Total}')
            ListBurger.append('Hamburguesa Godzilla')
            continue
        elif option == '4':
            Total += Menu['4. Hamburguesa Supreme']
            print(f'Se anadió una Hamburguesa Supreme. Total actual: ${Total}')
            ListBurger.append('Hamburguesa Supreme')
            continue
        elif option == '5':
            Total += Menu['5. Hamburguesa Perezosa']
            print(f'Se anadió una Hamburguesa Perezosa. Total actual: ${Total}')
            ListBurger.append('Hamburguesa Perezosa')
            continue

    print('='*60)
    print(f'Total a pagar: ${Total}')
    print('='*60)
    print('Gracias por su compra. ¡Vuelva pronto!')
    print('='*60)

if __name__ == "__main__":
    modo = input("ingrese '1' para ejecutar en modo manual o '2' para ejecutar prueba: ")
    if modo == '1':
        Hamburguesa()
    elif modo == '2':
        ''' 
        La prueba ejecutada aqui es que mi novia pidio una hamburguesa sencilla, pero como
        su sobrino es muy canson pidio el 6 que es una opcion que no esta en el menu, luego el programa
        le dijo que eso no estaba en el menu y selecciono la opcion 2 que es una hamburguesa doble,
        luego pidieron salir, el programa pregunto que si el pedido estaba correcto y dijeron que si,
        entonces el programa finalizo y mostro el total a pagar.
        '''
        input_sequence = ['1', '6', '2', 'salir', 'y']
        with patch('builtins.input', side_effect=input_sequence):
            Hamburguesa()
    else:
        print("Opción inválida. Por favor, ingrese '1' o '2' al volver a correr el script.")