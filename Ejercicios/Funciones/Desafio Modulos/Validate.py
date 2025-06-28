def validate_number(numero, minimo, maximo):
    # Verifica si el número está dentro del rango permitido
    return minimo <= numero <= maximo

def validate_length(cadena, largo_minimo, largo_maximo):
    # Verifica si la cadena tiene una longitud válida
    return largo_minimo <= len(cadena) <= largo_maximo
