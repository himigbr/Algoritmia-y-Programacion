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
    
    opcion = input("\nIngrese su opción o topping deseado: ").strip().lower()
    
    # Condición de salida del ciclo
    if opcion in ("6", "terminar", "salir"):
        break
    elif opcion in ("1", "sin topping"):
        total_pedido += 1.90
        print(">> Añadido: 1 Helado sin topping ($1.90).")
    elif opcion in ("2", "frutas", "fruta"):
        total_pedido += 1.90 + 0.50
        print(">> Añadido: 1 Helado con Topping de Frutas ($2.40).")
    elif opcion in ("3", "granola"):
        total_pedido += 1.90 + 1.50
        print(">> Añadido: 1 Helado con Topping de Granola ($3.40).")
    elif opcion in ("4", "oreo"):
        total_pedido += 1.90 + 1.00
        print(">> Añadido: 1 Helado con Topping de Oreo ($2.90).")
    elif opcion in ("5", "brownie"):
        total_pedido += 1.90 + 0.75
        print(">> Añadido: 1 Helado con Topping de Brownie ($2.65).")
    else:
        print("⚠️ ¡Topping no disponible! Lo sentimos, ese topping no se encuentra en el menú.")

print("\n" + "=" * 45)
print(f"Total a pagar por su pedido: ${total_pedido:.2f}")
print("¡Muchas gracias por su compra! Que disfrute su helado.")
print("=" * 45)