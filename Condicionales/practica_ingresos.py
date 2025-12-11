# Pidiendole al usuario que ingrese sus ingresos mensuales
ingresos_mensuales = int(input("Ingresa tus ingresos mensuales: $"))

# Validacion: solo verificamos el minimo, 10,000
if ingresos_mensuales < 10000:
    print("❌ Descalificado. Tus ingresos mensuales son insuficientes para aplicar, deben ser minimo 10,000.")
    
else:   
    # Procesamos los datos y damos retroalimentacion segun el nivel de ingresos (sin limites de ingreos altos)
    if ingresos_mensuales >= 100000:
        print("✅ ¡Excelente! Estas muy bien posicionado en la competencia.")
    elif ingresos_mensuales >= 50000:
        print("💼 Muy bien, tienes buenos ingresos competitivos para seguir creciendo.")   
    elif ingresos_mensuales >= 30000:
        print("👍 Bien, aun mantienes buen promedio para seguir creciendo.")
    elif ingresos_mensuales >= 10000:
        print("🙂 Aceptable, pero hay espacio para mejorar tus ingresos.")
        

