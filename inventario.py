def agregar_producto(inventario, nombre, precio, cantidad):
    if nombre in inventario: 
        inventario [nombre]["cantidad"] = cantidad + 1 
        print ("unidad de producto agregada")
    else:
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}
        print ("producto agregado con exito")

def eliminar_producto(inventario, nombre):
    if nombre in inventario:
        del inventario [nombre]
        print ("producto eleminado")
    else:
        print ("no existe este producto")

def listar_productos(inventario, nombre):
    if not inventario :
        print ("el inventario esta vacio")
    else:
        for nombre, datos in inventario.items():
         print ("datos en inventario")





