# Sistema de autenticación realista (LOGIN + INTENTOS + BLOQUEO)

import time

# Credenciales correctas
usuario_correcto = "abiezer_p"
contraseña_principal = "python2025"
contraseña_master = "master245" # Contraseña de emergencia

# Número máximo de intentos
intentos_maximos = 3
intentos_restantes = intentos_maximos

#Variable para ver si el acceso fue concedido
acceso_concedido = False

while intentos_restantes > 0 and not acceso_concedido:
    print(f"\n---SISTEMA DE AUTENTICACION---\n)")
    print(f"Intentos restantes: {intentos_restantes}")
    
# Pedir credenciales al usuario
    usuario_ingresado = input("Ingresa tu nombre de usuario aqui: ") 
    contraseña_ingresada = input("Ingresa tu contraseña aqui: ")
    
# Verificacion de espacio en blanco, paso 1
    if not usuario_ingresado.strip() or not contraseña_ingresada.strip():
        print("Error: No puedes dejar espacios en blanco. Intenta de nuevo.")
        continue # Vuelve al inicio sin restar intentos

# Verificacion de credenciales, paso 2
    if usuario_ingresado == usuario_correcto and (contraseña_ingresada == contraseña_principal or contraseña_ingresada == contraseña_master):
        # Acceso concedido, aqui definimos la variable de acceso
        if contraseña_ingresada == contraseña_master:
            print("Has ingresado la contraseña maestra. Acceso concedido.")
            print("Por favor, cambia tu contraseña principal despues de iniciar sesion.")
        else:
            print("Acceso concedido. Bienvenido/a!")
            
        acceso_concedido = True
        break # Salir del bucle
    
    #credenciales incorrectas.
    else:
        intentos_restantes -= 1
        
        if intentos_restantes > 0:
            print("Credenciales incorrectas. Verifica si es la contraseña o el usuario.")
            print(f"Te quedan {intentos_restantes} intentos.")
            
        else:
            # se agotaron los intentos
            print(f"\n Usuario  y/o contraseña incorrectos.")
            print("Has agotado todos tus intentos. El sistema se bloqueara por 10 segundos.")
            
        # Cuenta regresiva de bloqueo
            for segundo in range(10, 0, -1):
                print(f"Desbloqueo en {segundo} segundos...", end="\r")
                time.sleep(1)
                
            print("El sistema ha sido desbloqueado. Puedes intentar iniciar sesion nuevamente.")
            
            intentos_restantes = intentos_maximos # Reiniciar intentos
            
# Fin del sistema de autenticacion
if acceso_concedido:
    print("\n🎉 Haz iniciado sesión correctamente.")
    print("Puedes seguir usando el sistema")
else:
    print("\n⛔ No se pudo iniciar sesión.")