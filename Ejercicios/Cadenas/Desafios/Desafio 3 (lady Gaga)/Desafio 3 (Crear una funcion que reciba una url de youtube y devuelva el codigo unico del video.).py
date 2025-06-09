# Nombre y apellido: Thiago Custiriano
# Div: 211
# Desafio_3: Crear una funcion que reciba una url de youtube y devuelva el codigo unico del video.

def obtener_codigo(url: str) -> str:
    if "v=" in url:
        partes = url.split("v=")
        codigo = partes[1].split("&")[0]
        return codigo
    return ""

# Ejemplo
print(obtener_codigo("https://www.youtube.com/watch?v=bo_efYhYU2A"))  # bo_efYhYU2A
