'''
Este programa cumple con la peticion del primer ejercicio del taller.
Se implementan algunas cosas interesantes como strip() que nunca lo hemos usadoy sirve para
eliminar los espacios en blanco al inicio y al final de la cadena ingresada por el usuario,
y lower() que convierte la cadena a minúsculas para que la comparación sea insensible a mayúsculas y minúsculas.

De resto, es un ciclo while que se va a repetir hasta que el usuario diga, ya no quiero mas.
'''

total_pedido = 0

print("=" * 45)
print("       🍦 BIENVENIDO A LA HELADERÍA MAS CHIMBA DE TODAS 🍦       ")
print("=" * 45)

while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Helado sin topping         -> $1.90")
    print("2. Helado con Topping Frutas  -> $2.40 ($1.90 + $0.50)")
    print("3. Helado con Topping Granola -> $3.40 ($1.90 + $1.50)")
    print("4. Helado con Topping Oreo    -> $2.90 ($1.90 + $1.00)")
    print("5. Helado con Topping Brownie -> $2.65 ($1.90 + $0.75)")
    print("6. Terminar pedido y pagar")

    #Con strip() eliminamos los espacios en blanco al inicio y al final de la cadena ingresada por el usuario, y con lower() convertimos la cadena a minúsculas para que la comparación sea insensible a mayúsculas y minúsculas
    opcion = input("\nIngrese su opción o topping deseado: ").strip().lower()
    
    # Condición de salida del ciclo
    if opcion in ("6", "terminar", "salir"):
        break
    elif opcion in ("1", "sin topping"):
        total_pedido += 1.90
        print("Elegiste 1 Helado sin topping ($1.90).")
    elif opcion in ("2", "frutas", "fruta"):
        total_pedido += 1.90 + 0.50
        print("Elegiste 1 Helado con Topping de Frutas ($2.40).")
    elif opcion in ("3", "granola"):
        total_pedido += 1.90 + 1.50
        print("Elegiste 1 Helado con Topping de Granola ($3.40).")
    elif opcion in ("4", "oreo"):
        total_pedido += 1.90 + 1.00
        print("Elegiste 1 Helado con Topping de Oreo ($2.90).")
    elif opcion in ("5", "brownie"):
        total_pedido += 1.90 + 0.75
        print("Elegiste 1 Helado con Topping de Brownie ($2.65).")
    else:
        print("⚠️ ¡Paila! En que mundo vivis? Eso no existe aqui, elegi otra cosa o si no te vas")

print("\n" + "=" * 45)
print(f"Total a pagar por su pedido: ${total_pedido:.2f}")
print("¡Mi Dios le pague! Que lo disfrute y trabaje pa que me compre mas.")
print("=" * 45)