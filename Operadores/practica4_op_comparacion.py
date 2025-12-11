# Sistema de calificaciones para aprobar un curso
nota_aprobacion = 70
nota_perfecta = 100
recuperacion = 70
nota_honores = 90

# Nota obtenida por el estudiante
nota_estudiante = 85

aprobo = nota_estudiante >= nota_aprobacion
print("¿El estudiante aprobó el curso?", aprobo)  # Debería imprimir True

estudiante_perfecto = nota_estudiante == nota_perfecta
print("¿El estudiante obtuvo una nota perfecta?", estudiante_perfecto)  # Debería imprimir False

estudiante_en_recuperacion = nota_estudiante == recuperacion
print("¿El estudiante está en recuperación?", estudiante_en_recuperacion)  # Debería imprimir False

estudiante_con_honores = nota_estudiante >= nota_honores
print("¿El estudiante obtuvo honores?", estudiante_con_honores)  # Debería imprimir False