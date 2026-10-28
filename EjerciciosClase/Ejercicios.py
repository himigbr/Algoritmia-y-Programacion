#Ejercicio 1: Factorial de un número
def factorial(n):
    if n==0 or n==1:
        return 1 #El factorial de 0 y de 1 es igual a 1
    else:
        return n*factorial(n-1) #Por definición matemática n! = n * (n-1)!

#Ejercicio 2: Elevar al cuadrado los números pares de una lista 
def ElevaPares(lista):
    if not lista:
        return [] #Si la lista esta vacia, la retornamos vacia
    else:
        for p in range(len(lista)): #Se usa range para recorrer la lista por índices
            if lista[p]%2==0: #Si el modulo de la posición p es igual a 0, entonces es par
                lista[p] = lista[p]**2 #Elevamos al cuadrado los pares de la lista
        return lista

#Ejercicio 3: Suma recursiva de los elementos de una lista
def suma_recursiva(lista):
    if not lista:
        return 0 #Si la lista esta vacia, la suma es 0
    else:
        return lista[0] + suma_recursiva(lista[1:]) #Se suma el primer elemento de la lista [0] y se le suma la suma de los elementos restantes
        #Se hace slice [1:] para pasar el resto de la lista a la siguiente llamada recursiva

#Ejercicio 4: Invertir str
def invertir_cadena(texto):
    if len(texto) == 0:
        return print("\nLa cadena esta vacia") #Si la cadena esta vacia, se retorna un mensaje
    else:
        return texto[::-1] #Usamos slicing para retornar la cadena invertida (inicio:fin:paso) y el paso es -1 para recorrer la cadena de derecha a izquierda
    

lista = [0,1,2,3,4,5,6]
resultados = [factorial(n) for n in lista] #Una forma mas chevere de escribir el ciclo for
print("\nFactoriales:", resultados)
print("\nLista con pares elevados al cuadrado:", ElevaPares(lista.copy())) #Hacemos una copia de la lista para no modificar el puntero original
print("\nSuma recursiva de la lista:", suma_recursiva(lista))
print("\nCadena invertida:", invertir_cadena("Hola Mundo"))