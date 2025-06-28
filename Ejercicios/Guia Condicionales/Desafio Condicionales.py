def calcular_factura(metros_cubicos, tipo_cliente):
    CARGO_FIJO = 7000
    COSTO_POR_M3 = 200
    IVA = 0.21
    
    subtotal_consumo = metros_cubicos * COSTO_POR_M3
    total_sin_ajustes = CARGO_FIJO + subtotal_consumo
    bonificacion = 0
    recargo = 0
    
    if tipo_cliente == "Residencial":
        if metros_cubicos < 30:
            bonificacion = 0.10
        elif metros_cubicos > 80:
            recargo = 0.15
        
        if total_sin_ajustes < 35000:
            total_sin_ajustes *= 0.95  # Descuento adicional del 5%
    
    elif tipo_cliente == "Comercial":
        if metros_cubicos > 300:
            bonificacion = 0.12
        elif metros_cubicos > 150:
            bonificacion = 0.08
        elif metros_cubicos < 50:
            recargo = 0.05
    
    elif tipo_cliente == "Industrial":
        if metros_cubicos > 1000:
            bonificacion = 0.30
        elif metros_cubicos > 500:
            bonificacion = 0.20
        elif metros_cubicos < 200:
            recargo = 0.10
    
    # Aplicar bonificación o recargo
    total_ajustado = total_sin_ajustes
    if bonificacion:
        total_ajustado -= subtotal_consumo * bonificacion
    if recargo:
        total_ajustado += subtotal_consumo * recargo
    
    # Aplicar IVA
    total_final = total_ajustado * (1 + IVA)
    
    # Mostrar resultados
    print(f"Tipo de Cliente: {tipo_cliente}")
    print(f"Consumo: {metros_cubicos} m³")
    print(f"Subtotal Consumo: ${subtotal_consumo:.2f}")
    print(f"Cargo Fijo: ${CARGO_FIJO:.2f}")
    print(f"Total sin ajustes: ${total_sin_ajustes:.2f}")
    if bonificacion:
        print(f"Bonificación aplicada: -${subtotal_consumo * bonificacion:.2f}")
    if recargo:
        print(f"Recargo aplicado: +${subtotal_consumo * recargo:.2f}")
    print(f"Total con ajustes: ${total_ajustado:.2f}")
    print(f"IVA (21%): +${total_ajustado * IVA:.2f}")
    print(f"Total a pagar: ${total_final:.2f}")

# Solicitar datos al usuario
tipo_cliente = input("Ingrese el tipo de cliente (Residencial, Comercial, Industrial): ")
metros_cubicos = float(input("Ingrese la cantidad de metros cubicos consumidos: "))

calcular_factura(metros_cubicos, tipo_cliente)
