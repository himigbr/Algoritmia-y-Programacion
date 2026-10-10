# Taller de Ciclos

### Ejercicio 1

Escribir un programa para el siguiente problema: Un usuario quiere comprar un helado en una conocida marca de comida rápida y desea saber cuánto le costará en función del topping que elija. **NOTA**: Puede escoger o no un topping. Si desea topping, solo puede seleccionar uno.

|||
|---|---|
|Helado sin topping|$1.90|
|Topping de Frutas|$0.50|
|Topping de Granola|$1.50|
|Topping de Oreo|$1.00|
|Topping de Brownie|$0.75|

En caso de que el usuario pida un topping que no se encuentra en el menú, sacar un mensaje en donde se le informe que no hay el topping solicitado. Para finalizar agregar el valor final que debe pagar el usuario si se al momento de hacer uno o varios pedidos. **NOTA**: Sea creativo con el mensaje que le va a mostrar al usuario.

#### Diagrama de flujo

```mermaid
graph TD
    A([Inicio]) --> B["total_pedido = 0"]
    B --> C[/Mostrar menú de pedidos/]
    C --> D[/Leer opción o topping/]
    D --> E{"¿opción == 'terminar' o 'salir'?"}
    E -->|Sí| K[/Imprimir total a pagar/]
    K --> Z([Fin])
    E -->|No| F{"¿opción seleccionada?"}
    F -->|'Sin topping'| M["total += 1.90"]
    F -->|'Frutas'| G["total += 1.90 + 0.50"]
    F -->|'Granola'| H["total += 1.90 + 1.50"]
    F -->|'Oreo'| I["total += 1.90 + 1.00"]
    F -->|'Brownie'| J["total += 1.90 + 0.75"]
    F -->|Otro| L[/Imprimir 'Topping no válido'/]
    M --> C
    G --> C
    H --> C
    I --> C
    J --> C
    L --> C
```

### Ejercicio 2

Escriba un programa para que la siguiente lista [2,4,3,1,6,7,5,8,9,10] se ordene de menor a mayor (orden ascendente). Implementar con ciclos y posteriormente usar una función predeterminada de Python para verificar el funcionamiento del mismo.

#### Diagrama de flujo

```mermaid
graph TD
    A([Inicio]) --> B["lista = [2, 4, 3, 1, 6, 7, 5, 8, 9, 10]<br/>n = len(lista)"]
    B --> C[i = 0]
    C --> D{¿i < n - 1?}
    D -- Sí --> E[j = 0]
    E --> F{"¿j < n - 1 - i?"}
    F -- No --> K[i = i + 1]
    K --> D
    F -- Sí --> G{"¿lista[j] > lista[j + 1]?"}
    G -- Sí --> H["aux = lista[j]<br/>lista[j] = lista[j + 1]<br/>lista[j + 1] = aux"]
    G -- No --> J[j = j + 1]
    H --> J
    J --> F
    D -- No --> L[/Imprimir lista/]
    L --> M["lista_verificada = sorted(lista_original)"]
    M --> N[/Imprimir lista_verificada/]
    N --> O{"¿lista == lista_verificada?"}
    O -- Sí --> P[/Imprimir mensaje de éxito/]
    O -- No --> Q[/Imprimir mensaje de error/]
    P --> Z([Fin])
    Q --> Z
```

### Ejercicio 3

Escriba un programa que lea una palabra e imprima todas las subcadenas, ordenadas por longitud. Por ejemplo, si el usuario introduce “rum”, el programa imprime:

r  
u  
m  
ru  
um  
rum  

#### Diagrama de flujo

```mermaid
graph TD
    A([Inicio]) --> B[/Leer palabra/]
    B --> C["n = len(palabra)<br/>resultado = [ ]"]
    C --> D["longitud = 1"]
    D --> E{"¿longitud <= n?"}
    E -->|No| J[/Imprimir resultado/]
    J --> Z([Fin])
    E -->|Sí| F["inicio = 0"]
    F --> G{"¿inicio <= n - longitud?"}
    G -->|No| I["longitud = longitud + 1"]
    I --> E
    G -->|Sí| H["sub = palabra[inicio : inicio + longitud]<br/>resultado.append(sub)"]
    H --> K["inicio = inicio + 1"]
    K --> G
```

### Ejercicio 4

Usted tiene acceso a la base de datos de “student_scores” en un formato de diccionario donde las llaves son los nombres de los estudiantes y los valores son las notas de ellos.

Al finalizar el programa, se debe tener un diccionario denominado “student_grades”, que contiene los nombres de los estudiantes como llaves y los siguientes mensajes como valores:

|||
|---|---|
|Harry|88|
|Ron|78|
|Hermione|95|
|Draco|75|
|Neville|60|

- Scores 91 - 100: Grade = “Outstanding”
- Scores 81 - 90: Grade = “Exceeds Expectations”
- Scores 71 - 80: Grade = “Acceptable”
- Scores 70 or lower: Grade = “Fail”

#### Diagrama de flujo

```mermaid
graph TD
    A([Inicio]) --> B["student_scores = {'Harry': 88, 'Ron': 78, ...}<br/>student_grades = { }"]
    B --> C["Para cada estudiante, nota en student_scores"]
    C --> D{"¿Quedan estudiantes por evaluar?"}
    D -->|No| K[/Imprimir student_grades/]
    K --> Z([Fin])
    D -->|Sí| E{"¿nota >= 91?"}
    E -->|Sí| F["grade = 'Outstanding'"]
    E -->|No| G{"¿nota >= 81?"}
    G -->|Sí| H["grade = 'Exceeds Expectations'"]
    G -->|No| I{"¿nota >= 71?"}
    I -->|Sí| J["grade = 'Acceptable'"]
    I -->|No| L["grade = 'Fail'"]
    F --> M["student_grades[estudiante] = grade"]
    H --> M
    J --> M
    L --> M
    M --> C
```

### Ejercicio 5

Un borracho se desplaza por una ciudad que tiene distribución de calles tipo Manhattan (cuadrícula de calles y carreras) y elige al azar hacia dónde ir al llegar a cada intersección.

Puede elegir al azar entre una de cuatro direcciones. Se podría pensar de manera equivocada que en promedio el borracho no se desplaza mucho de su posición inicial porque las elecciones se anulan estadísticamente entre sí, pero en realidad no es así. Represente las ubicaciones como pares ordenados enteros (x, y) e implemente un programa que muestre el paseo del borracho después de recorrer 100 intersecciones, comenzando en (0, 0), e imprima la ubicación final.

#### Diagrama de flujo

```mermaid
graph TD
    A([Inicio]) --> B["x = 0, y = 0<br/>paso = 0"]
    B --> C{"¿paso < 100?"}
    C -->|No| I[/Imprimir posición final 'x, y'/]
    I --> Z([Fin])
    C -->|Sí| D["Elegir dirección al azar:<br/>['Norte', 'Sur', 'Este', 'Oeste']"]
    D --> E{"¿dirección elegida?"}
    E -->|'Norte'| F1["y = y + 1"]
    E -->|'Sur'| F2["y = y - 1"]
    E -->|'Este'| F3["x = x + 1"]
    E -->|'Oeste'| F4["x = x - 1"]
    F1 --> P[/Imprimir paso, dirección y posición 'x, y'/]
    F2 --> P
    F3 --> P
    F4 --> P
    P --> H["paso = paso + 1"]
    H --> C
```