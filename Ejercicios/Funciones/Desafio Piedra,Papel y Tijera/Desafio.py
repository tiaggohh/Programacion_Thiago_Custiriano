# Nombre y apellido: Thiago Custiriano
# Div: 211
# Desafio:Piedra,Papel o Tijera

import random

def mostrar_elemento(eleccion):
    if eleccion == 1:
        return "Piedra"
    elif eleccion == 2:
        return "Papel"
    elif eleccion == 3:
        return "Tijera"
    else:
        return "Opcion invalida"

def verificar_ganador_ronda(jugador, maquina):
    if jugador == maquina:
        return "Empate"
    elif (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
        return "Jugador"
    else:
        return "Maquina"

def verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):
    if aciertos_jugador == 2 or aciertos_maquina == 2:
        return False
    elif ronda_actual >= 3:
        return False
    else:
        return True

def verificar_ganador_partida(aciertos_jugador, aciertos_maquina):
    if aciertos_jugador > aciertos_maquina:
        return "Jugador"
    elif aciertos_maquina > aciertos_jugador:
        return "Maquina"
    else:
        return "Empate"

def entrada_jugador():
    while True:
        try:
            eleccion = int(input("Elegí: 1-Piedra, 2-Papel, 3-Tijera: "))
            if eleccion in [1, 2, 3]:
                return eleccion
            else:
                print("Número invalido. Intenta de nuevo.")
        except:
            print("Eso no es un número. Intenta otra vez.")

def jugar_piedra_papel_tijera():
    ronda = 0
    aciertos_jugador = 0
    aciertos_maquina = 0

    while verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda):
        ronda += 1
        print(f"\n--- Ronda {ronda} ---")

        jugador = entrada_jugador()
        maquina = random.randint(1, 3)

        print("Jugador eligio:", mostrar_elemento(jugador))
        print("Maquina eligio:", mostrar_elemento(maquina))

        resultado = verificar_ganador_ronda(jugador, maquina)

        if resultado == "Jugador":
            aciertos_jugador += 1
            print("🏆 Ganaste esta ronda.")
        elif resultado == "Maquina":
            aciertos_maquina += 1
            print("💀 La maquina gano esta ronda.")
        else:
            print("😐 Empate.")

        print(f"Marcador → Jugador: {aciertos_jugador} - Maquina: {aciertos_maquina}")

    ganador = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
    if ganador == "Empate":
        print("\nSe empato en 3 rondas. ¡A jugar una mas hasta que haya ganador!")
        return jugar_piedra_papel_tijera()  # Usamos recursion para repetir si empataron
    else:
        print("\n🎉 Ganador de la partida:", ganador)
        return ganador


jugar_piedra_papel_tijera()
