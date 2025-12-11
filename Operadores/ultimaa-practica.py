# Calificaciones de estudiantes

nota_numerica = int(input("Ingrese la nota del estudiante: "))

# Primero verificamos si la nota es válida
if nota_numerica >100 or nota_numerica <0:
    print("Nota inválida. Por favor ingrese una nota entre 0 y 100.")
else:

# Asignamos la calificación basada en la nota numérica

    if nota_numerica >= 90:
        calificacion = "A"
    elif nota_numerica >= 80:
        calificacion = "B"
    elif nota_numerica >= 70:
        calificacion = "C"
    else:
        calificacion = "F"
    
    print(f"La calificación del estudiante es: {calificacion}")