# Nombre y apellido: Thiago Custiriano
# Div: 211
# Desafio_3: Crear una funcion que reciba el titulo de un tema y devuelva una lista con los colaboradores.

def obtener_colaboradores(titulo: str) -> list:
    if " - " not in titulo:
        return []
    parte_artistas = titulo.split(" - ")[0]
    colaboradores = parte_artistas.split(" | ")
    return colaboradores

# Ejemplo
print(obtener_colaboradores("Bradley Cooper | Lukas Nelson - Shallow"))  # ['Bradley Cooper', 'Lukas Nelson']
