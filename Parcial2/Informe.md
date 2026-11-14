# Parcial 2

## Sección 1: Preguntas Teóricas

### Explica la diferencia conceptual entre un parámetro y un argumento en Python.

La principal diferencia entre argumento y parámetro radica en los momentos y lugares en donde se utilizan. Por un lado, el parámetro es aquel que se usa en el momento donde se define la función, siendo esta la variable que se encierra dentro del paréntesis y que funciona como una especie de molde o contenedor. Por otro lado, el argumento se usa cuando se llama a la función en otra parte del código, tras haberla definido anteriormente. El argumento es el valor real que toma el parámetro para ejecutar la función.

### ¿Qué es el alcance local de una variable dentro de una función?

El alcance local de una variable quiere decir que esta se crea y solo existe dentro de la función que la usa. Esta vive y muere en la ejecución de la función; una vez que esta termina de ejecutarse, la variable es eliminada y no se puede llamar en ningún momento posterior en el código, puesto que ya no existirá.

### Un error común al empezar a programar es confundir print() con return. ¿Cuál es la diferencia fundamental entre mostrar un resultado en pantalla con print() y devolverlo con return? ¿Por qué para conectar múltiples cálculos en un sistema de ingeniería es imprescindible el uso de return?

La diferencia radica en el destino y el propósito: print() se utiliza para mostrarle al humano algo que pueda interpretar; no guarda absolutamente nada, solo imprime un valor en pantalla que el programa no puede volver a usar como dato. Por otro lado, return es la forma en la que la computadora le entrega el resultado de una función al código, lo que permite pasarle ese dato a una variable o directamente a otra función para que trabaje con él.
El uso de return es imprescindible ya que permite mantener la automatización en la cadena de procesos que sigue un código. Como mencioné anteriormente, return sirve para pasar el resultado de una función a otra y así consecutivamente hasta que sea necesario.

### En programación funcional se promueve el principio DRY (Don’t Repeat Yourself ). Explica en qué consiste la modularidad y cómo el dividir un problema complejo de ingeniería en funciones pequeñas y especializadas facilita las pruebas del código (debugging) y la lectura del programa.

La modularidad consiste en dividir un programa en partes independientes y separadas llamadas "módulos" —que en el caso de Python llamaremos "funciones"—. Estas se encargan de hacer tareas individuales y bien definidas; así, en lugar de crear un código extenso y desordenado, se van creando "piezas" que dan forma a la estructura general.
Este proceso facilita la depuración, ya que es más fácil aislar un error en uno de los módulos y revisar las líneas de esa función específica, que tener que buscarlo por todo el programa. Por otro lado, las pruebas son más fáciles de ejecutar debido a que se pueden llamar las funciones individualmente y pasarles argumentos para verificar que cumplan con su correcto funcionamiento.
Además, este enfoque facilita la lectura del código, puesto que cada función tiene su tarea individual. Para un humano es mucho más sencillo leer calcular_algo() que descifrar varias líneas con operaciones complejas.

### ¿Cuales son los cuatro pilares del POO y se pueden usar en programación funcional?

Los cuatro pilares de la POO son:
- **Abstracción:** Nos dice que mostremos solo las características esenciales; se enfoca más en el "qué hace" y no en el "cómo se hace".
- **Encapsulamiento:** Se trata de agrupar los datos y los métodos que operan en una sola unidad, restringiendo así el acceso desde el exterior.
- **Herencia:** Es un mecanismo que permite que una clase nueva adquiera las propiedades y métodos de una ya existente.
- **Polimorfismo:** Es la capacidad de que varias clases respondan al mismo llamado de maneras diferentes.

En la programación funcional, los pilares de la POO no se pueden usar directamente en su forma original, pero sí existen algunos equivalentes. Sin embargo, la herencia y el encapsulamiento tradicional no se usan en la programación funcional, ya que esta última trabaja con datos inmutables y no con clases. Por otro lado, la abstracción es un concepto universal y el polimorfismo se puede adaptar a través de funciones genéricas.

### ¿Qué es el constructor o inicializador de una clase y que debe de definirse dentro de este?

El constructor es un método especial que se ejecuta automáticamente en el momento en el que se crea un nuevo objeto a partir de una clase. En Python, este método se define como \_\_init\_\_. Su propósito es preparar al objeto asignándole sus valores iniciales.
Dentro de este se deben definir las variables y características propias de ese objeto:
- self: Es el primer parámetro obligatorio que representa al objeto que se está creando y sirve para asociar las variables con el objeto.
- Parámetros de entrada: Las variables que recibirá el constructor con los datos iniciales.
- Asignación de atributos: Las líneas de código que guardan los datos dentro del objeto.

## Sección 2: Ejercicios Prácticos

### Ejercicio 1

Para el primer ejercicio, usamos principalmente una función de la librería random para obtener los datos de la subestación, como una forma de simularlos; usando funciones de Python nativas se pudieron obtener los extremos. Para el caso del promedio sumamos todos los valores de la lista y los dividimos en el largo de la lista, y por último, para sacar solo los valores por encima del promedio, primero reciclamos la función para hallar el promedio y después recorremos la lista con el condicional comparando uno a uno los valores de la lista y los devolvemos para usarlos en alguna variable.

### Ejercicio 2

Para las funciones de suma, resta y multiplicación no fue algo muy complejo ya que usamos funciones nativas de Python; en cuanto a la división solo se agregó de más un condicional para evitar errores por división indefinida. Para el factorial sacamos un condicional que nos sirve para evitar operaciones indefinidas y usamos la recursividad de la misma función para reducir líneas y sacar el factorial fácilmente. En la inversa simplemente pasamos el número principal al denominador y además añadimos un condicional para evitar divisiones indefinidas. Para la potencia, reciclamos la función de multiplicación e iteramos en un ciclo for que nos permite multiplicar la base por las veces que se requiera basado en el exponente, pero solo con esto no fue suficiente ya que de ese modo no nos hubiera funcionado con decimales, así que añadimos la condición de que ese método solo funciona si el valor del número es módulo de 1 y, si no, entonces usamos la función nativa de Python para que nos resuelva el problema. En el caso de un exponente negativo, reciclamos la función para sacar las inversas y de nuevo usamos el ciclo for para multiplicar esas inversas las veces que sea necesario. Para la raíz cuadrada usamos el método de aproximación binaria que nos permite ir cerrando límites hasta aproximarnos lo más que podamos al valor de la raíz; vamos iterando y dependiendo de la condición del resultado vamos ajustando límites.

### Ejercicio 3

Para este ejercicio es simplemente implementar el manejo de índices de los diccionarios, que recordemos que a diferencia de las listas estos funcionan con llaves que en este caso son los nombres de los componentes, pero hay algo curioso y es que el valor no solo es uno en este caso sino que son dos, así que mediante otro diccionario le añadimos atributos a esa llave del diccionario y simplemente con las claves podemos empezar a indexar y añadir, eliminar e incluso operar sobre los atributos.

### Ejercicio 4

Para este ejercicio lo que necesitamos es iterar sobre los valores del diccionario para hacer las operaciones correspondientes; la gran ventaja es que los valores están en una lista y, al estar allí, es más fácil hacer operaciones con todos los valores sin necesidad de tener que iterar sobre las listas. Las iteraciones que se ven en el script son más que todo debido a la necesidad de sacar las llaves para mostrarlas en los resultados o cuando sea necesario. Cabe destacar que para las funciones que requieren de cálculos específicos, el promedio usado fue el ponderado para simular la hermosa universidad. Utilizamos además algunos índices para operar sobre los valores en los que había que hacer multiplicaciones u otras operaciones que se hayan requerido.

### Ejercicio 5

Para este ejercicio lo primero fue importar la función randint que nos devuelve un número entero al azar dentro de un rango que se le especifique. Para la función de elegir la dificultad usamos condicionales que, dependiendo de la selección del usuario, devolverán el número de intentos según la dificultad. Usamos randint para generar nuestro número aleatorio y lo devolvemos para usarlo en otra función. Para la función jugar usamos un ciclo for que tiene como límite de iteraciones el valor que nos devuelve la función de elegir dificultad y empezamos a iterar sobre los valores que el usuario va ingresando, haciendo uso de condicionales para saber si el valor ingresado está por debajo o por encima de la frecuencia secreta. Para guardar el historial implementamos la función with que básicamente nos dice que con x condición haga determinada acción y nos sirve para no tener que cerrar manualmente el archivo de texto en este caso.

### Ejercicio 6

En este ejercicio solo usamos dos funciones que nos cumplen todas las necesidades que se nos pide en el enunciado. La primera función nos identifica los ítems, se los enumera y se los muestra al usuario y, además de ello, recibe la entrada preguntando qué desea comprar; la función al final lo que hace es tomar el valor del producto seleccionado y lo devuelve para su posterior uso en la función de cobrar, la cual nos ayuda a verificar si lo que va a pagar el cliente es suficiente y, si así es, nos ayuda a saber cuánto hay que devolver, todo en una misma función.