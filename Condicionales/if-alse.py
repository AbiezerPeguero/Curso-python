# Autenticación simple de usuario
usuario_ingresado = input("Ingresa tu usuario: ").lower() # Usamos .lower() para evitar problemas con mayúsculas/minúsculas

# La contraeña es solo numérica, pero si quisieramos que lleve letras, deberiamos usar solo input(), asi puede comibinar letras y numeros
contraseña_ingresada = int(input("Ingresa tu contraseña: "))

if usuario_ingresado == "abiezer_p" and contraseña_ingresada == 123456:
    print("Bienvenido a la plataforma")
else:
    print("Usuario o contraseña incorrecta intente de nuevo")