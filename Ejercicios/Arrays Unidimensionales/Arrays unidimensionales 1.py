# Nombre y apellido: Thiago Custiriano
# Div: 211
# Arrays_Unidimensionales_1:Desarrollar una función que permita crear un array de números con la cantidad
#  de elementos que establezca el parámetro recibido.

def crear_array(cantidad):
    lista = []
    for i in range(cantidad):
        lista.append(0)  # Se llena con ceros o cualquier valor por defecto
    return lista
