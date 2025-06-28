# Nombre y apellido: Thiago Custiriano
# Div: 211
# Arrays_Unidimensionales_Desafío_1: Sistema de Recomendación de Productos

def productos_en_comun(lista1, lista2):
    comunes = []
    for producto in lista1:
        if producto in lista2 and producto not in comunes:
            comunes.append(producto)
    return comunes

def productos_exclusivos(lista1, lista2):
    exclusivos = []
    for producto in lista1:
        if producto not in lista2:
            exclusivos.append(producto)
    return exclusivos

def catalogo_total(lista1, lista2):
    total = []
    for producto in lista1:
        if producto not in total:
            total.append(producto)
    for producto in lista2:
        if producto not in total:
            total.append(producto)
    return total

def recomendar(lista_usuario, lista_otros):
    recomendados = []
    for producto in lista_otros:
        if producto not in lista_usuario and producto not in recomendados:
            recomendados.append(producto)
    return recomendados

# Listas predefinidas (podés cambiarlas por input si querés hacerlo manual)
usuario1 = ["celular", "auriculares", "notebook", "mouse"]
usuario2 = ["notebook", "mouse", "teclado", "monitor"]

print("Productos en común:", productos_en_comun(usuario1, usuario2))
print("Productos exclusivos de Usuario 1:", productos_exclusivos(usuario1, usuario2))
print("Productos exclusivos de Usuario 2:", productos_exclusivos(usuario2, usuario1))
print("Catálogo total:", catalogo_total(usuario1, usuario2))
print("Recomendaciones para Usuario 1:", recomendar(usuario1, usuario2))
print("Recomendaciones para Usuario 2:", recomendar(usuario2, usuario1))
