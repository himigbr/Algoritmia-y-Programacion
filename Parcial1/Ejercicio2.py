from unittest.mock import patch

def Juegos():
    #preliminar
    Tit = 'Sala de Juegos IsaMig'
    LTit = (60 - len(Tit)) // 2
    Cliente = 1
    Total = 0
    ListClientes = []

    Precios = {
        '1. Menor de 5 años' : {'Precio' : 0, 'Cantidad' : 0},
        '2. Entre 5 y 18 años' : {'Precio' : 5, 'Cantidad' : 0},
        '3. Mayor de 18 años' : {'Precio' : 10, 'Cantidad' : 0}
    }

    #Bienvenida
    print('='*60)
    print(' '*LTit + Tit)
    print('='*60)

    #La magia
    print('Ingrese a continuacion la edad de/los Clientes')
    print('='*60)

    while True:
        edad = input(f'Edad del cliente {Cliente}: ').lower()
        if edad == 'total':
            break

        try:
            edad = int(edad)
        except ValueError:
            print('Edad invalida. Ingrese una edad valida o "total" para ver el total.')
            continue

        if edad < 0:
            print('Edad invalida. Ingrese una edad valida.')
        elif edad < 5:
            Precios['1. Menor de 5 años']['Cantidad'] += 1
        elif 5 <= edad <= 18:
            Precios['2. Entre 5 y 18 años']['Cantidad'] += 1
        else:
            Precios['3. Mayor de 18 años']['Cantidad'] += 1
        Cliente += 1

    Total = (
        Precios['1. Menor de 5 años']['Cantidad'] * Precios['1. Menor de 5 años']['Precio'] +
        Precios['2. Entre 5 y 18 años']['Cantidad'] * Precios['2. Entre 5 y 18 años']['Precio'] +
        Precios['3. Mayor de 18 años']['Cantidad'] * Precios['3. Mayor de 18 años']['Precio']
    )
    print('='*60)
    print('Usted ingreso:')
    print('='*60)
    for cat, info in Precios.items():
        print(f'{cat}: {info["Cantidad"]}')
    print('='*60)
    print(f'Total a pagar: ${Total}')
    print('='*60)

if __name__ == "__main__":
    modo = input("ingrese '1' para ejecutar en modo manual o '2' para ejecutar prueba: ")
    if modo == '1':
        Juegos()
    elif modo == '2':
        with patch('builtins.input', side_effect=['26', '18', '4', 'total']):
            Juegos()
    else:
        print("Modo invalido. Por favor ingrese '1' o '2' cuando vuelva a correr el script.")