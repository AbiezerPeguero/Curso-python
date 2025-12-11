# Creando variables en Python

nombre = "Abiezer"
edad = 20
pais = "Republica Dominicana"
carrera = "ciencias de datos"

# Concatenando variables con f-strings

presentacion = f"Hola, mi nombre es {nombre}, tengo {edad} años de edad y soy de {pais}, y estoy estudiando {carrera}"

print(presentacion)

# Verificando informacion 

print("Abiezer" in presentacion) # Me devuelve True indicando que "Abiezer" si esta en la variable presentacion
print("programacion" in presentacion) # Me devuelve False indicando que "programacion" no esta en la variable presentacion
print("Francia" not in presentacion) # Me devuelve True indicando que "Francia" no esta en la variable presentacion