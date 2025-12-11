# Creando variable de un inventario de tienda electronica

producto1 = "Laptop Lenovo legion 5"
producto2 = "mouse inalambrico"
producto3 = "teclado mecanico"

# Concatenando variables con f-strings
inventario = f"inventario disponible: {producto1}, {producto2}, {producto3}"

# Verificando si un producto esta en el inventario

print("La laptop Lenovo Legion 5 esta en inventario?", "Laptop Lenovo legion 5" in inventario) # Me devuelve True indicando que la laptop si esta en el inventario
print("Esta 'celular' en el investario?", "celular" in inventario) # Me devuelve False indicando que el celular no esta en el inventario


# El codigo de abajo al ejecutarse tiene al final un .lower, esta funcion es porque .lower convierte todo a minusculas
# asi que la busqueda sera en minusculas y evitamos errores por mayusculas o minusculas ya que python es sensible a eso
# Es correcto usar .Lower cuando buscamos confirmar si un texto esta en una variable y no estamos seguros de las mayusculas o minusculas.

#print("Esta laptop en investario?", "Laptop Lenovo legion 5" in inventario.lower())