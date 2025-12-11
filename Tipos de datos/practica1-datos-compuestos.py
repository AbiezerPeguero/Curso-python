# Creando una lista con los nombres de 5 compañeros de clase.
estudiantes = ["luis", "ana", "maria", "jose", "carlos"]

# Imprimiendo el nombre del tercer estudiante (índice 2).
print(estudiantes[2])  # Imprime: maria

# Cambiando el nombre del segundo estudiante.
estudiantes[1] = "abiezer"
print(estudiantes)  # Imprime: ['luis', 'abiezer', 'maria', 'jose', 'carlos']

# Agregando un nuevo estudiante al final de la lista usando .append()
estudiantes.append("santiago")
print(estudiantes)  # Imprime: ['luis', 'abiezer', 'maria', 'jose', 'carlos', 'santiago']