'''
Este script cumple con la peticion del cuarto ejercicio del taller
Aqui usamos diccionarios que es como una forma de generar una tabla de datos
Primero mediante un for analizamos el estudiante y su nota y luego mediante condicionales 
Le damos una calificacion segun su nota y lo guardamos en otro diccionario
En donde estara el nombre del estudiante como clave y la calificacion como valor.
'''

# Hacemos un diccionario con los nombres de los estudiantes y sus puntajes
student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60
}

#Hacemos un diccionario vacío para almacenar las calificaciones finales de los estudiantes
student_grades = {}

# Recorremos cada estudiante y su puntaje en el diccionario student_scores para asignarles una calificación basada en su puntaje
for estudiante, nota in student_scores.items():
    if nota >= 91:
        grade = "Outstanding"
    elif nota >= 81:
        grade = "Exceeds Expectations"
    elif nota >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"

    # Agregamos la calificación al diccionario student_grades con el nombre del estudiante como clave y la calificación como valor
    student_grades[estudiante] = grade

# Imprimimos los diccionarios originales y finales para ver los resultados
print("Diccionario original de notas (student_scores):")
print(student_scores)

print("\nDiccionario final de calificaciones (student_grades):")
print(student_grades)

# Imprimimos un resumen detallado de cada estudiante, su puntaje y la calificación asignada
print("\n--- Resumen Detallado ---")
for estudiante, grade in student_grades.items():
    print(f"- {estudiante}: {student_scores[estudiante]} pts -> {grade}")