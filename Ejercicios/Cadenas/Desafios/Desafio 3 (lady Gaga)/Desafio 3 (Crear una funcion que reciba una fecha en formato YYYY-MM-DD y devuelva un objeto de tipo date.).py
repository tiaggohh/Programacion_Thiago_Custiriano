# Nombre y apellido: Thiago Custiriano
# Div: 211
# Desafio_3: Crear una funcion que reciba una fecha en formato YYYY-MM-DD y devuelva un objeto de tipo date.

from datetime import date

def formatear_fecha(fecha: str) -> date:
    partes = fecha.split("-")
    if len(partes) != 3:
        return None
    anio = int(partes[0])
    mes = int(partes[1])
    dia = int(partes[2])
    return date(anio, mes, dia)

# Ejemplo
print(formatear_fecha("2018-09-27"))  # 2018-09-27
