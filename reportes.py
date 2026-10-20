
def stock_bajo(inventario, limite):

    return [nombre for nombre, datos in inventario.items() if datos["cantidad"] < limite]


def valor_total(inventario):
  
    return sum(datos["precio"] * datos["cantidad"] for datos in inventario.values())


def nombres_en_mayuscula(inventario):
    
    return sorted([nombre.upper() for nombre in inventario.keys()])

if __name__ == "__main__":
    inventario_prueba = {
        "lapiz": {"precio": 1.5, "cantidad": 100},
        "cuaderno": {"precio": 4.0, "cantidad": 30},
        "regla": {"precio": 2.0, "cantidad": 5},
    }