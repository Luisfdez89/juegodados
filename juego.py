from dado import Dado

class Juego:
    def __init__(self, jugador1, jugador2, caras1, caras2, caras3, lanzamientos, intermedios):
        self.set_jugador1(jugador1)
        self.set_jugador2(jugador2)
        self.set_lanzamientos(lanzamientos)
        self.dado1 = Dado(caras1)
        self.dado2 = Dado(caras2)
        self.dado3 = Dado(caras3)
        self.intermedios = intermedios.lower() == 's'
        self.r1 = 0
        self.r2 = 0

    def set_jugador1(self, jugador1):
        if len(jugador1) > 20:
            raise ValueError("La longitud del nombre del jugador 1 no puede ser mayor de 20")
        self.jugador1 = jugador1

    def set_jugador2(self, jugador2):
        if len(jugador2) > 20:
            raise ValueError("La longitud del nombre del jugador 2 no puede ser mayor de 20")
        self.jugador2 = jugador2

    def set_lanzamientos(self, lanzamientos):
        if not 2 <= lanzamientos <= 100:
            raise ValueError("El número de lanzamientos debe estar entre 2 y 100")
        self.lanzamientos = lanzamientos

    def jugar(self):
        self.r1 = 0
        self.r2 = 0
        for x in range(self.lanzamientos):
            # jugador1
            s1, s2, s3 = self.dado1.lanzar(), self.dado2.lanzar(), self.dado3.lanzar()
            self.r1 += s1 + s2 + s3

            if self.intermedios:
                print(f"Lanzamiento {x + 1}:")
                print(f"{self.jugador1}: {s1} {s2} {s3} ({s1 + s2 + s3})")

            # jugador2
            s1, s2, s3 = self.dado1.lanzar(), self.dado2.lanzar(), self.dado3.lanzar()
            self.r2 += s1 + s2 + s3

            if self.intermedios:
                print(f"{self.jugador2}: {s1} {s2} {s3} ({s1 + s2 + s3})")
                print("")

    def mostrar_resultados(self):
        print("Resultados:")
        print(f"Jugador 1: {self.jugador1}")
        print(f"Jugador 2: {self.jugador2}")
        print(f"Número de lanzamientos: {self.lanzamientos}")
        print(f"Dados: {self.dado1.get_caras()}, {self.dado2.get_caras()} y {self.dado3.get_caras()}")
        print(f"Puntos jugador 1: {self.r1}")
        print(f"Puntos jugador 2: {self.r2}")
        if self.r1 > self.r2:
            print(f"El GANADOR es {self.jugador1} con {self.r1} puntos")
        elif self.r1 == self.r2:
            print("Ha habido un EMPATE")
        else:
            print(f"El GANADOR es {self.jugador2} con {self.r2} puntos")
