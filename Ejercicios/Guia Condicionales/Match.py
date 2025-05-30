# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio: Match
#Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
#En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
#Si es invierno: solo se viaja a Bariloche.
#Si es verano: se viaja a Mar del plata y Cataratas.
#Si es otoño: se viaja a todos los lugares.
#Si es primavera: se viaja a todos los lugares menos Bariloche.
 


estacion = input("Ingrese la estación del año (invierno, verano, otoño, primavera): ")
destino = input("Ingrese el destino (Bariloche, Mar del plata, Cataratas): ")

if estacion == "invierno":
    if destino == "bariloche":
        print("Se viaja")
    else:
        print("No se viaja")

elif estacion == "verano":
    if destino == "mar del plata" or destino == "cataratas":
        print("Se viaja")
    else:
        print("No se viaja")

elif estacion == "otoño":
    print("Se viaja") 

elif estacion == "primavera":
    if destino != "bariloche":
        print("Se viaja")
    else:
        print("No se viaja")

else:
    print("Estación no válida")
