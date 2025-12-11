# Comparando precio de productos en una tienda
precio_producto_1 = 10000
precio_producto_2 = 15000

# Verificando cuál producto es más caro, si ambos tienen el mismo precio y si el producto 2 es más barato que el producto 1
producto_mas_caro = precio_producto_1 > precio_producto_2 
mismo_precio = precio_producto_1 == precio_producto_2 
mas_barato = precio_producto_2 < precio_producto_1

print("¿El producto 1 es más caro que el producto 2?", producto_mas_caro)  # Debería imprimir False
print("¿Ambos productos tienen el mismo precio?", mismo_precio)  # Debería imprimir False
print("¿El producto 2 es más barato que el producto 1?", mas_barato)  # Debería imprimir False

