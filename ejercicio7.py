def agregar_producto(inventario, producto):
    inventario.append(producto)


productos = ["arroz", "aceite"]
agregar_producto(productos, "café")

for producto in productos:
    print(producto)

#USAMOS UN FOR PARA QUE SE IMPRIMAN LOS PRODUCTOS SIN LOS CORCHETES Y COMILLAS, SOLO LOS NOMBRES DE LOS PRODUCTOS