#Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio.
#  Mostrar la suma y el promedio por pantalla.


contador = 0
suma = 0

while contador < 5:
    numero = int(input("Ingrese un número: "))
    suma = suma + numero  
    contador = contador + 1  

promedio = suma / 5

print("La suma de los números es:", suma)
print("El promedio de los números es:", promedio)
