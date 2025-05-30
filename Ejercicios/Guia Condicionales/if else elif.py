# Nombre y apellido: Thiago Custiriano
# Div: 201
# Ejercicio IF_01: A partir del ingreso de la altura en centímetros de un jugador de baloncesto, 
# el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes
#  parámetros:

altura = input("Ingrese su altura en cm: ")
altura = int(altura)

if altura >= 200:
    print("Su posicion es Ala-Pívot o Pívot")
elif altura >= 180  :
        print("Su posicion es Alero")
elif altura >160 :
        print("Su posicion es Escolta")
else:
        print("Su posicion es Base ")