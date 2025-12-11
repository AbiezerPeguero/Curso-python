# Creando una lista, se usa corchetes [] y puede ser modificada.
lista = ["Abiezer Peguero", "Ciencias de Datos", True, 1.85, 20] 

#print(lista[1])  # Imprime: Ciencias de Datos. Esto es porque los índices comienzan del 0 al 9 y no se cuenta desde el 1.

# Creando una tupla, se usa paréntesis () y no puede ser modificada.
tupla = ("Abiezer Peguero", "Ciencias de Datos", True, 1.85, 20) 

#print(tupla[2]) # Imprime: True. Esto es porque los índices comienzan del 0 al 9 y no se cuenta desde el 1.

# Modifica el valor en la posición 3 de la lista.
lista[3] =  "2.00"  

# Esto generará un error porque las tuplas no pueden ser modificadas.
#tupla[3] =  "2.00" 


# Creando un conjunto, se usa llaves {} y no permite elementos duplicados, se ordenan de forma aleatoria.
# No se puede acceder a los elementos por índice, y no permite elementos duplicados.
conjunto = {"Abiezer", "Inteligencia Artificial", True, 1.85, "Abiezer"}

#print(conjunto[2])  Esto generará un error porque los conjuntos no permiten acceso por índice.

# Creando un diccionario, se usa llaves {}.
# Permite acceder a los elementos mediante claves (keys) en lugar de índices, osea, acceder por  el  nombre del elemento y no por su posición.
diccionario = {
    'nombre' : "Abiezer",
    'curso' : "Ciencias de Datos",
    'futuro' : "Ingeniero de Datos",
    'dato_duplicado' : "Abiezer"
}

print(diccionario['curso'])  # Imprime: Ciencias de Datos.  