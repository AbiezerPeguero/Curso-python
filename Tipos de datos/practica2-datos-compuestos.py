# Creando una tupla de coordenadas geográficas (latitud, longitud).
coordenadas_santo_domingo = (18.4861, -69.9312)

# Imprimiendo la latitud (primer elemento de la tupla).
print(coordenadas_santo_domingo[0])  # Imprime: 18.4861 (latitud)

# Intentando modificar la longitud (segundo elemento de la tupla).
#coordenadas_santo_domingo[1] = -70.0000    
#print(coordenadas_santo_domingo) # Esto generará un error porque las tuplas no pueden ser modificadas.

# Creando una nueva tupla con las coordenadas de otra ciudad.
coordenadas_santiago = (19.4417, -70.6970)
print(coordenadas_santiago)  # Imprime: (19.4417, -70.6970)

# Mostrando ambas coordenadas
print("Coordenadas de Santo Domingo:", coordenadas_santo_domingo)
print("Coordenadas de Santiago:", coordenadas_santiago)