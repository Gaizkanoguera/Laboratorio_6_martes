def agregar_producto(inventario, nombre, precio, cantidad):
    if nombre in inventario: 
        inventario [nombre]["cantidad"] = cantidad + 1 
        print ("unidad de producto agregada")
    else:
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}
        print ("producto agregado con exito")

        

