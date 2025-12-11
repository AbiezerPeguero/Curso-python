# Crear variables de mini perfil de redes sociales

usuario = "abiezer_dev"
biografia = "Cientifico de datos y entusiasta de la tecnologia"
ubicacion = "Republica Dominicana"
intereses = "Python, Machine Learning, Data Science"

# Concatenando variables con f-strings

perfil = f"Mi usuiario en IG es {usuario}\nBiogtafia: {biografia}\nintereses: {intereses}"

print("Esta \"Python\" en mis intereses?", "Python" in perfil) # Me devuelve True indidacando que Python si esta en mis intereses

# Si quiero hacer una comilla dentro de una cadena uso \"aqui el texto\", como en el codigo final de arriba
# ya que si no, python se confunde y piensa que es el final de la cadena

#Tambien puedo usar comillas simples (' ) por fuera de la cadena y comillas dobles (" ) por dentro de la cadena. Ejemplo: print('Esta "Python" en mis intereses?', "Python" in perfil)

# \n para saltos de línea
