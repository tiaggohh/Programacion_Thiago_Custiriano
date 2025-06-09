# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Cadenas_6: Crear una funcion para contar cuantas veces aparece una subcadena dentro de una cadena.

def contar_subcadena(cadena, subcadena):
    return cadena.count(subcadena)


print(contar_subcadena("El pan del panadero", "pan"))  # 2
