# Nombre y apellido: Thiago Custiriano
# Div: 211
# Cadenas_6: Contar cuántas veces aparece una subcadena dentro de otra.

def contar_subcadena(cadena, sub):
    contador = 0
    for i in range(len(cadena) - len(sub) + 1):
        if cadena[i:i+len(sub)] == sub:
            contador += 1
    return contador

#prueba
print(contar_subcadena("El pan del panadero", "pan"))  # 2
