# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_13: Especializar las funciones del punto 1, 2 y 3 para 
# hacerlas reutilizables. Agregar validaciones.

def pedir_entero_validado():
    while True:
        try:
            return int(input("Ingrese un numero entero: "))
        except:
            print("Error. Debe ingresar un numero entero.")

def pedir_flotante_validado():
    while True:
        try:
            return float(input("Ingrese un numero con decimales: "))
        except:
            print("Error. Debe ingresar un nu" \
            "mero decimal.")

def pedir_cadena_validada():
    texto = input("Ingrese una cadena de texto: ")
    while texto.strip() == "":
        texto = input("No puede estar vacío. Ingrese una cadena: ")
    return texto

# Pruebas
e = pedir_entero_validado()
f = pedir_flotante_validado()
c = pedir_cadena_validada()

print("Entero:", e)
print("Flotante:", f)
print("Cadena:", c)
