from juego import Juego


def main():
    jugador1 = input("Introduce el nombre del primer jugador: ")
    jugador2 = input("Introduce el nombre del segundo jugador: ")
    caras1 = int(input("Introduce el número de caras para el primer dado: "))
    caras2 = int(input("Introduce el número de caras para el segundo dado: "))
    caras3 = int(input("Introduce el número de caras per al tercer dado: "))
    lanzamientos = int(input("Introduce el número de lanzamientos: "))
    intermedios = input("¿Quieres ver los resultados intermedios por pantalla? (S/N): ")

    try:
        juego = Juego(jugador1, jugador2, caras1, caras2, caras3, lanzamientos, intermedios)
        juego.jugar()
        juego.mostrar_resultados()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
