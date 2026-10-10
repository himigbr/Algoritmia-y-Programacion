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

## Ejercicio 9

Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones sobre las clases de ese día. El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes se dicta el nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los jueves son para práctica hablada y los viernes se dicta inglés para viajeros. Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato “día, DD/MM”, donde [día] es un día de la semana, DD es el número de día y MM es el número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo día supere el número 31 o el mes supere el número 12, finalizar el programa indicando que se produjo un error. Debe permitirse que ingrese el día de la semana en minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>. Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron exámenes, pero eso sólo si se trata de los niveles inicial, intermedio o avanzado, ya que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el programa le mostrará el porcentaje de aprobados. Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a clase y el programa le indicará “asistió la mayoría” en caso de que la asistencia sea mayor al 50 % o “no asistió la mayoría” si no es así. Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del mes 7, se deberá imprimir “Comienzo de nuevo ciclo” y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego imprimir el ingreso total en $.

### Diagrama de Flujo

```mermaid
graph TD
    A([Inicio]) --> B[/Leer entrada 'dia, DD/MM'/]
    B --> C["dia_str, fecha_str = entrada.split(',')<br/>dia = dia_str.strip().lower()<br/>DD, MM = fecha_str.strip().split('/')<br/>d = int(DD), m = int(MM)"]
    C --> D{"¿dia not in dias_validos<br/>OR d < 1 OR d > 31<br/>OR m < 1 OR m > 12?"}
    D -- Sí --> E[/Imprimir 'Se produjo un error'/]
    E --> Z([Fin])
    D -- No --> F{"¿dia in ['lunes', 'martes', 'miercoles']?"}
    F -- Sí --> G[/Preguntar: '¿Hubo exámenes? s/n'/]
    G --> H{"¿hubo_examen == 's'?"}
    H -- Sí --> I[/Leer aprobados y no_aprobados/]
    I --> J["total = aprobados + no_aprobados<br/>porcentaje = (aprobados / total) * 100"]
    J --> K[/Imprimir porcentaje de aprobados/]
    H -- No --> Z
    K --> Z
    F -- No --> L{"¿dia == 'jueves'?"}
    L -- Sí --> M[/Leer porcentaje_asistencia/]
    M --> N{"¿porcentaje_asistencia > 50?"}
    N -- Sí --> O[/Imprimir 'asistió la mayoría'/]
    N -- No --> P[/Imprimir 'no asistió la mayoría'/]
    O --> Z
    P --> Z
    L -- No --> Q{"¿dia == 'viernes'?"}
    Q -- Sí --> R{"¿(d == 1 AND m == 1) OR (d == 1 AND m == 7)?"}
    R -- Sí --> S[/Imprimir 'Comienzo de nuevo ciclo'/]
    S --> T[/Leer cantidad_alumnos y arancel/]
    T --> U["ingreso_total = cantidad_alumnos * arancel"]
    U --> V[/Imprimir ingreso_total/]
    V --> Z
    R -- No --> Z
    Q -- No --> Z
```

---