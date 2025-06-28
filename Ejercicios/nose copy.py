#Nombre y apellido: Thiago Custirino
#Evaluacion: Desarrollar una función que reciba una cadena de caracteres y verifique si todos los 
# caracteres en la cadena son números romanos, es decir, si pertenecen al conjunto de 
# símbolos: I, V, X, L, C, D, y M. La misma retorna un booleano que indica si todos los
#  carácteres son números romanos o no. La función deberá estar debidamente documentada. 
# Probar la función.

def es_romano(cadena):
    Romanos_Validos = ['i', 'v', 'x', 'l', 'c', 'D', 'M']
    indice = 0
    while indice < len(cadena):
        caracteres_validos = False
        j = 0
        while j < len(Romanos_Validos)[j]:
            if caracteres_validos == True:
             return True
        j = + 1
    return True
print(es_romano("")) 
print(es_romano(""))
print(es_romano("i"))
print(es_romano(""))

