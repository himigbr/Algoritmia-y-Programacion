# Taller Diagramas de Flujo y Condiconales

## Ejercicio 1

Solicitar al usuario un número que este entre 10 y 50. Si el número es el 30, imprimir “Ganaste un premio” en el caso contrario “Perdiste”. ¿Qué pasaría si el usuario ingresa -10?

### *Respuesta:*

No cumple el rango esperado y por lo tanto el script devolverá 'Número fuera de rango'.

### Diagrama de Flujo

```mermaid
graph TD
    A([Inicio]) --> B[/Leer x/]
    B --> C{¿10 <= x <= 50?}
    C --> |No| D[/Imprimir 'Número fuera de rango'/]
    D --> Z([Fin])
    C --> |Sí| E{¿x == 30?}
    E --> |Sí| F[/Imprimir 'Ganaste un premio'/]
    E --> |No| G[/Imprimir 'Perdiste'/]
    F --> Z
    G --> Z
```

---

## Ejercicio 2

Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. Dado el caso que ambos sean iguales indicar que los dos son iguales.

### Diagrama de Flujo

```mermaid
graph TD
    A([Inicio]) --> B[/Leer n1, n2/]
    B --> C{¿n1 == n2?}
    C --> |Sí| D[/Imprimir 'Ambos números son iguales'/]
    C --> |No| E{¿n1 < n2?}
    E --> |Sí| F[/Imprimir 'n1 es el menor'/]
    E --> |No| G[/Imprimir 'n2 es el menor'/]
    D --> Z([Fin])
    F --> Z
    G --> Z
```

---

## Ejercicio 3

Preguntar al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

### Diagrama de Flujo

```mermaid
graph TD
    A([Inicio]) --> B[/Leer day/]
    B --> C{¿day == 'lunes'?}
    C --> |Sí| D[/Imprimir 'Es Lunes'/]
    C --> |No| E{¿dia == 'viernes'?}
    E --> |Sí| F[/Imprimir 'Es Viernes'/]
    E --> |No| G{¿dia == 'sábado' o 'domingo'?}
    G --> |Sí| H[/Imprimir 'FDS'/]
    G --> |No| I[/Imprimir 'Que dia es hoy?, Con quien estoy?'/]
    D --> Z([Fin])
    F --> Z
    H --> Z
    I --> Z
```

---

## Ejercicio 4

Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los
números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).NOTA: Para este caso no puede utilizar la función abs().

### Diagrama de Flujo

```mermaid
graph TD
    A([Inicio]) --> B[/Leer x/]
    B --> C{¿x < 0?}
    C --> |Sí| D[v_abs = x * -1]
    C --> |No| E[v_abs = x]
    D --> F[/Imprimir v_abs/]
    E --> F
    F --> Z([Fin])
```

---

## Ejercicio 5

Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

### Diagrama de Flujo

```mermaid
graph TD
    A([Inicio]) --> B[/Leer year/]
    B --> C{¿year % 4 == 0 AND year % 100 != 0 OR year % 400 == 0?}
    C --> |Sí| D[/Imprimir 'El año es bisiesto'/]
    C --> |No| E[/Imprimir 'El año no es bisiesto'/]
    D --> Z([Fin])
    E --> Z
```

---

## Ejercicio 6

Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.

### Diagrama de Flujo

```mermaid
graph TD
    A([Inicio]) --> B[/Leer texto/]
    B --> C{¿longitud texto != 1?}
    C --> |Sí| D[/Imprimir 'No se puede procesar el dato'/]
    D --> Z([Fin])
    C --> |No| E{¿texto es vocal 'a, e, i, o, u'?}
    E --> |Sí| F[/Imprimir 'es vocal'/]
    E --> |No| G[/Imprimir 'no es vocal'/]
    F --> Z
    G --> Z
```

---

## Ejercicio 7

Crear un programa en el cual al momento de ingresar un número. Si este número es múltiplo de 3 debe se sacar Fizz, si el número es múltiplo de 5 debe de sacar Buzz y en caso de que sea múltiplo de 3 y 5 sacar FizzBuzz,

### Diagrama de Flujo

```mermaid
graph TD
    A([Inicio]) --> B[/Leer x/]
    B --> C{¿x % 3 == 0 AND x % 5 == 0?}
    C --> |Sí| D[/Imprimir 'FizzBuzz'/]
    C --> |No| E{¿x % 3 == 0?}
    E --> |Sí| F[/Imprimir 'Fizz'/]
    E --> |No| G{¿x % 5 == 0?}
    G --> |Sí| H[/Imprimir 'Buzz'/]
    G --> |No| I[/Mostrar x/]
    D --> Z([Fin])
    F --> Z
    H --> Z
    I --> Z
```

---

## Ejercicio 8

Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibi-
lidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

### Diagrama de Flujo

```mermaid
graph TD
    A([Inicio]) --> B[/Leer candidato/]
    B --> C{¿candidato?}
    C --> |'A'| D[color = 'rojo']
    C --> |'B'| E[color = 'verde']
    C --> |'C'| F[color = 'azul']
    C --> |Otro| G[/Imprimir 'Opción errónea'/]
    G --> Z([Fin])
    D --> H[/Imprimir 'Usted ha votado por el partido ' + color/]
    E --> H
    F --> H
    H --> Z([Fin])
```

---