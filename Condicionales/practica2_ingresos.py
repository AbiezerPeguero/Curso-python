# Variable de control para el bucle
datos_correctos = False

while not datos_correctos:
    # Pedimos los ingresos
    ingresos_mensules = int(input("Ingresa tus ingresos mensuales: $"))
    
    if ingresos_mensules < 10000:
        print("❌ Descalificado. Tus ingresos mensuales son insuficientes para aplicar, deben ser minimo 10,000.")
        print("Intente nuevamente.\n")
        continue # Volver al inicio del bucle si los datos son incorrectos
    
    if ingresos_mensules >= 500000:
        print(f"\n⚠️ Alerta: El monto ingresado (${ingresos_mensules}) es muy alto")
        confirmacion = input("¿Estás seguro de que este es el monto correcto? (si/no): ").lower()
        
        if confirmacion == "no":
            print("OK. Vamos a intentarlo de nuevo.\n")
            continue # Volver al inicio del bucle si el usuario no confirma
        
        elif confirmacion == "si":
            print("✅ Monto confirmado. Continua...\n")  
            datos_correctos = True # Salir del bucle
        else:
            print("Respuesta no válida. Supongo que los datos no son correctos, corrigelos.\n")
            continue # Volver al inicio del bucle si la respuesta no es válida
    else:
        # Si el monto esta entre 10,000 y 499,999 no hay alerta
        datos_correctos = True # Salir del bucle si los datos son correctos
        
print("---Evaluacion de Ingresos---")

if ingresos_mensules >= 100000:
    print("✅ ¡Excelente! Estas muy bien posicionado en la competencia.")
    
elif ingresos_mensules >= 50000:
    print("💼 Muy bien, tienes buenos ingresos competitivos para seguir creciendo.")

elif ingresos_mensules >= 30000:
    print("👍 Bien, aun mantienes buen margen para seguir.")
else:
    # Entre 10,000 y 29,999
    print("🙂 Aceptable, pero hay espacio para mejorar tus ingresos.")