# Creando un conjunto de lenguajes de programación.
mis_lenguajes = {"Python", "JavaScript", "Python", "SQL"}
lenguajes_trabajo = {"Java", "C#", "Python", "C++", }

print(mis_lenguajes)  # Imprime: {'Python', 'JavaScript', 'SQL'} (sin duplicados, orden aleatorio)

# Imprimiendo la cantidad de lenguajes en comun usando la funcion intersection() 
print(mis_lenguajes.intersection(lenguajes_trabajo))  # Imprime: {'Python'} (elementos comunes)

# Imprimiendo la unión de ambos conjuntos usando la funcion union() y mostrando un mismo conjunto sin duplicados sumando ambos conjuntos
print(mis_lenguajes.union(lenguajes_trabajo)) # Imprime la unión de ambos conjuntos sin duplicados

# Dato extra sobre conjuntos:
#mis_lenguajes & lenguajes_trabajo  # Mismo resultado que .intersection()
#mis_lenguajes | lenguajes_trabajo  # Mismo resultado que .union()