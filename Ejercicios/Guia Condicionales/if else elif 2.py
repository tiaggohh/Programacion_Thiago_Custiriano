# Nombre y apellido: Thiago Custiriano
# Div: 201
# Ejercicio IF_02: Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje 
# según el valor: 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
#4 y 5                ---> Aprobado, la nota es ...
#1, 2 y 3            ---> Desaprobado, la nota es ...

import random

nota = random.randint (1, 10)

if nota >= 6:
    print(f"Promocion directa, la nota es {nota}")
elif nota >= 4:
    print(f"Aprobado la nota es {nota}")
else:
    print(f"desaprobado la nota es {nota}")