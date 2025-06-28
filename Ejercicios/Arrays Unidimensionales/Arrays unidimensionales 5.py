# Nombre y apellido: Thiago Custiriano
# Div: 211
# Arrays_Unidimensionales_5: Calcular y retornar el producto de todos los elementos de la lista.

def producto_lista(lista):
    producto = 1
    for i in lista:
        producto *= i
    return producto
