# Creando una  lista de diccionarios
productos = [
    {"nombre": "laptop", "precio": 110000, "cantidad": 5},
    {"nombre": "smartphone", "precio": 50000, "cantidad": 10},
    {"nombre": "teclado", "precio": 2500, "cantidad": 10}
]

# Imprimiendo el nombre del segundo producto
print(productos[1]["nombre"])  # Imprime: smartphone

# Calculando el precio total de todos los productos
precio_total = productos[0]["precio"] + productos[1]["precio"] + productos[2]["precio"]

print("Precio total de todos los productos:", precio_total)  # Imprime el precio total

# Agregando un nuevo producto a la lista de diccionarios
productos.append({"nombre": "monitor", "precio": 15000, "cantidad": 7})  

# Actualizando la cantidad del primer producto
productos[0]["cantidad"] = 15  

print("Practica terminada y lista de diccionarios actualizada:", productos)  # Imprime la lista de diccionarios actualizada