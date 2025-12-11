# Ceando perfil de desarrollador con diccionario
mi_perfil = {
    "nombre" : "Abiezer",
    "edad" : 20,
    "lenguajes" : ["Python", "JavaScript", "C#"],
    "experiencia_años" : 3,
    "disponible" : False
}

print("lenguajes de programación:", mi_perfil["lenguajes"])  # Imprime la lista de lenguajes de programación

# cambiando la dissponibilidad del desarrollador a True
mi_perfil["disponible"] = True

# Agregando una nueva clave-valor al diccionario
mi_perfil["proyecto_actual"] = "desarrollando algoritmo de analisis de datos y machine learning y mercados financieros"  # Agregando una nueva clave-valor al 

print(mi_perfil)  # Imprime el diccionario actualizado con el nuevo proyecto perfil