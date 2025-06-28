from Validate import validate_number, validate_length

def get_int(mensaje, mensaje_error, minimo, maximo, reintentos):
    for _ in range(reintentos):
        try:
            numero = int(input(mensaje))
            if validate_number(numero, minimo, maximo):
                return numero
            else:
                print(mensaje_error)
        except:
            print(mensaje_error)
    return None

def get_float(mensaje, mensaje_error, minimo, maximo, reintentos):
    for _ in range(reintentos):
        try:
            numero = float(input(mensaje))
            if validate_number(numero, minimo, maximo):
                return numero
            else:
                print(mensaje_error)
        except:
            print(mensaje_error)
    return None

def get_string(mensaje, mensaje_error, largo_minimo, largo_maximo, reintentos):
    for _ in range(reintentos):
        texto = input(mensaje)
        if validate_length(texto, largo_minimo, largo_maximo):
            return texto
        else:
            print(mensaje_error)
    return None
