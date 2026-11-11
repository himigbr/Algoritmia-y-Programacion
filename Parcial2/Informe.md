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



### Ejercicio 2



### Ejercicio 3



### Ejercicio 4



### Ejercicio 5



### Ejercicio 6