# Nombre y apellido: Thiago Custiriano
# Div: 211
# Desafio_3: Crear una funcion que reciba el titulo de un tema y devuelva el nombre del tema sin los colaboradores.

def obtener_nombre_tema(titulo: str) -> str:
    if " - " not in titulo:
        return titulo
    return titulo.split(" - ")[1]

# Ejemplo
print(obtener_nombre_tema("Bradley Cooper | Lukas Nelson - Shallow"))  # Shallow
