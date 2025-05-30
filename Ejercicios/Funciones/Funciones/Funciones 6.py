# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_6: Crear una función que verifique si un numero dado 
# es par o impar. La función debe imprimir un mensaje indicando el resultado.

def verificar_par_o_impar(numero):
    if numero % 2 == 0:
        print("El numero es par.")
    else:
        print("El numero es impar.")

num = int(input("Ingrese un numero: "))
verificar_par_o_impar(num)
