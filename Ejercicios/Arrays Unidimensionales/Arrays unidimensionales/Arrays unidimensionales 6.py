# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_6: Crear una función que verifique si un número dado 
# es par o impar. La función debe imprimir un mensaje indicando el resultado.

def verificar_par_o_impar(numero):
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")

num = int(input("Ingrese un número: "))
verificar_par_o_impar(num)
