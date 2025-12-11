# Sistema de autenticación realista (LOGIN + INTENTOS + BLOQUEO)

import time

# Credenciales correctas
usuario_correcto = "abiezer_p"
contraseña_principal = "python2025"
contraseña_master = "master245" # Contraseña de emergencia

# Número máximo de intentos
intentos_maximos = 3
intentos_restantes = intentos_maximos

while intentos_restantes > 0:
    print(f"\n---SISTEMA DE AUTENTICACION---\n)")
    print(f"Intentos restantes: {intentos_restantes}")
    
    usuario_ingresado = input("Ingresa tu nombre de usuario aqui: ") 
    contraseña_ingresada = input("Ingresa tu contraseña aqui: ")
    
    if usuario_ingresado == usuario_correcto and contraseña_ingresada == contraseña_principal:
        print("✅ ¡Acceso concedido! Bienvenido al sistema.")
    
    elif usuario_correcto == usuario_ingresado and contraseña_ingresada == contraseña_master:
        print("⚠️ Has utilizado la contraseña de emergencia. Por favor, cambia tu contraseña principal después de iniciar sesión.")
    
    else:
        intentos_restantes -=1
        print(f"❌ credeciales incorrectos. Te quedan {intentos_restantes} intentos.")
        if intentos_restantes == 0:
            print("🔒 Haz agotado tus intentos. Tu cuenta a sido blooqueda temporalmente")
            time.sleep(10) # Bloqueo temporal de 10 segundos
            print("⏳ Puedes intentar iniciar sesión nuevamente ahora.")
            
# Validacion de espacios en blanco

    if not usuario_ingresado.strip() or not contraseña_ingresada.strip():
        print("❌ No puedes dejar espacios en blanco. Intenta de nuevo")
        continue # Vuelve al inicio sin restar intentos

# Verificacion de credenciales
    elif usuario_ingresado == usuario_correcto and (contraseña_ingresada == contraseña_principal or contraseña_ingresada == contraseña_master):
        print("✅ ¡Acceso concedido! Bienvenido al sistema.") # Aqui sales del bucle
        
    else:
        intentos_restantes -= 1
        print("Usuario o contraseña incorrectos. Intenta de nuevo.")
        if intentos_restantes == 0:
            print(f"🔒 Credenciales incorrectos. Te quedan {intentos_restantes} intentos.")
            time.sleep(10) # Bloqueo temporal de 10 segundos
            print("⏳ puedes intentar otra vez ahora.")
            
# Cuando intensos_restantes llega a 0:
    if intentos_restantes == 0:
        print("\, Cuenta bloqueada")
        print("Demaciados intentos fallidos.")
        print("Bloquenado el sistema por 10 segundos...")
        
        #cuenta regresiva
        for segundo in range(10, 0, -1): 
            print(f"Intenta de nuevo en {segundo} segundos...", end="\r")
            time.sleep(1)
            
        print("Puedes intentar iniciar sesión nuevamente ahora.")