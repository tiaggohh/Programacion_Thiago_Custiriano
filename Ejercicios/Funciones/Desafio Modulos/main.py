from Input import get_int, get_float, get_string

entero = get_int("Ingrese un numero entre 1 y 100: ", "Numero inválido.", 1, 100, 3)
print("Numero entero ingresado:", entero)

decimal = get_float("Ingrese un decimal entre 0.0 y 10.0: ", "Numero inválido.", 0.0, 10.0, 3)
print("Numero decimal ingresado:", decimal)

texto = get_string("Ingrese su nombre (3 a 10 letras): ", "Texto inválido.", 3, 10, 3)
print("Cadena ingresada:", texto)
