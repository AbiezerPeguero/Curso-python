# Verificacion de edad para acceso a contenido restringido

edad = 18

puede_votar = edad >= 17
puede_conducir = edad >= 16
puede_beber_alcohol = edad >= 21

print("¿Puede votar?", puede_votar)  # Debería imprimir True
print("¿Puede conducir?", puede_conducir) # Debería imprimir True
print("¿Puede beber alcohol?", puede_beber_alcohol)  # Debería imprimir False