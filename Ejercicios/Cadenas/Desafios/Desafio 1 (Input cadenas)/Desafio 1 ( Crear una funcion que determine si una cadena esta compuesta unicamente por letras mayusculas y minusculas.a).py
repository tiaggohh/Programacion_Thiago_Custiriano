# Nombre y apellido: Thiago Custiriano
# Div: 211
# Desafio_1: Verificación de Cadena Alfabética

cadena = "HolaMundo"
solo_letras = True

for c in cadena:
    if not ((ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122)):
        solo_letras = False

if solo_letras:
    print("La cadena tiene solo letras.")
else:
    print("La cadena tiene otros caracteres.")
