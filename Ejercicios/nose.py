#Nombre y apellido: Thiago Custirino
#Evaluacion: Desarrollar una función que reciba una cadena de caracteres y verifique si todos los 
# caracteres en la cadena son números romanos, es decir, si pertenecen al conjunto de 
# símbolos: I, V, X, L, C, D, y M. La misma retorna un booleano que indica si todos los
#  carácteres son números romanos o no. La función deberá estar debidamente documentada. 
# Probar la función.

def es_romano(cadena):
    Romanos_Validos = ['I', 'V', 'X', 'L', 'C', 'D', 'M ']
    indice = 0
    while indice < len(cadena):
        caracter_valido = False
        j = 0
        while j < len(Romanos_Validos):
            if cadena[indice] == Romanos_Validos[j]:
                caracter_valido = True
            j = j + 1
        if caracter_valido == False:
            return False
        indice = indice + 1
    return True

print(es_romano("VAB")) 
print(es_romano("AXL"))
print(es_romano("XA"))
print(es_romano("IVLDC"))

