# Creando una lista de precios de productos en una tienda y comparándolos
tienda_1 = [12000, 25000, 18000, 30000]
tienda_2 = [15000, 22000, 18000, 28000]

mismo_precio = tienda_1[0] == tienda_2[0]
mas_barato = tienda_1[0] < tienda_2[0]
mismo_precio_segundo_producto = tienda_1[1] == tienda_2[1]
mas_caro = tienda_1[2] > tienda_2[2]

print("¿El primer producto tiene el mismo precio en ambas tiendas?", mismo_precio)  # Debería imprimir False
print("¿El primer producto es más barato en la tienda 2?", mas_barato)  # Debería imprimir True
print("¿El segundo producto tiene el mismo precio en ambas tiendas?", mismo_precio_segundo_producto)  # Debería imprimir False
print("¿El tercer producto es más caro en la tienda 2?", mas_caro)  # Debería imprimir False