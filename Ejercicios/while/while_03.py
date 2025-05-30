#Mostrar la suma de los números desde el 1 hasta el 10.

suma = 0 #iniciamos la suma en 0
numero = 1 #empezamos desde el número 1

while numero <= 10: #mientras el número sea menor o igual a 10 seguimos sumando
    suma += numero #vamos acumulando la suma
    numero += 1 #aumentamos el número en 1 para la proxima vez.

print("La suma de los números del 1 al 10 es:", suma)
