
'''
Este script cumple con la peticion del segundo ejercicio del taller
Es un poco complejo el entender los for anidados por la funcion range
Pero basicamente lo que hace es que va recortando la lista segun ordena el ultimo valor de esta
Por ejemplo si la lista es [10, 5, 7] lo que va a hacer es que compara el 10 con el 5
lo mueve a la derecha y luego compara el 10 con el 7 y lo mueve a la derecha
Luego recorta la lista y compara el 5 con el 7 y lo mueve a la derecha
Y alli termina el ciclo porque ya no hay mas valores que comparar.
'''

# Lista original
lista = [2, 4, 3, 1, 6, 7, 5, 8, 9, 10]

# Se guarda una copia de la lista para compararla al final con la lista ordenada usando la función predeterminada
lista_original = lista.copy()
n = len(lista)

print("Lista original desordenada:")
print(lista)

# 1. Empezamos el ordenamiento con lo mas lento de python, los ciclos for anidados
for i in range(n - 1): #Este primer ciclo se realiza para que la lista se recorte en cada iteración, ya que el último valor de la lista ya estará ordenado
    for j in range(n - 1 - i):
        if lista[j] > lista[j + 1]: # En este ciclo vamos numero por numero comparando el valor actual con el siguiente
            # Si el valor actual es mayor que el siguiente, se intercambian de posicion
            aux = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux
        #Sino entonces pasamos al siguiente valor en la lista para compararlo con el que sigue

print("\nLista ordenada manualmente con ciclos:")
print(lista)

# 2. Comprobamos la lista ordenada manualmente con la lista ordenada con la función predeterminada sorted()
lista_verificada = sorted(lista_original)

print("\nLista ordenada con la función predeterminada sorted():")
print(lista_verificada)

# Comprobamos la lista ordenada manualmente con la lista ordenada con la función predeterminada
if lista == lista_verificada:
    print("\n✅ Me dicen el mago, pero no el magono... de todos.")
else:
    print("\n❌ No funciono :'( vaya hagalo a mano mas bien.")