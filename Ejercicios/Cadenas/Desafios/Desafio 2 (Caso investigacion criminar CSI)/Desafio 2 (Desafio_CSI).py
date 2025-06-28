# Nombre y apellido: Thiago Custiriano
# Div: 211
# Desafio_CSI: Comparar ADN de la escena del crimen con muestras de sospechosos.

from Sospechosos import sospechosos, muestras

muestra_crimen = "CGTTTAATG"
culpable = "SON TODOS INOCENTES"

for i in range(len(muestras)):
    if muestra_crimen in muestras[i]:
        culpable = sospechosos[i]
        break

print("Resultado de la investigacion:")
print(culpable)
