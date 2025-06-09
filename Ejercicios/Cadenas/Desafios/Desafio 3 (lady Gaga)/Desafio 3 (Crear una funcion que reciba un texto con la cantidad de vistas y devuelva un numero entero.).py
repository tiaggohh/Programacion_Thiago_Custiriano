# Nombre y apellido: Thiago Custiriano
# Div: 211
# Desafio_3: Crear una funcion que reciba un texto con la cantidad de vistas y devuelva un numero entero.

def convertir_vistas_numerico(vistas: str) -> int:
    if "millones" in vistas:
        numero_str = vistas.replace(" millones", "").strip()
        if numero_str.isdigit():
            return int(numero_str) * 1_000_000
    return 0

# Ejemplo
print(convertir_vistas_numerico("1900 millones"))  # 1900000000
