# Sistema de acceso usando operadores de comparación
usuario_registrado = "abiezer"
contrasena_registrada = "abiezer123"

# Datos ingresados por el usuario
usuario_ingresado = "abiezer"
contrasena_ingresada = "abiezer124"

# Verificando si el usuario y la contraseña son correctos
print(usuario_registrado == usuario_ingresado)  # Debería imprimir True
print(contrasena_ingresada == contrasena_registrada)  # Debería imprimir False
