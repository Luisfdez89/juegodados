import random


class Dado:
    __caras_permitidas = [4, 6, 8, 10, 12, 20, 120, 200, 300]

    def __init__(self, caras):
        self.__caras = None
        self.set_caras(caras)

    def lanzar(self):
        return random.randint(1, self.__caras)

    def get_caras(self):
        return self.__caras

    def set_caras(self, caras):
        if caras in self.__caras_permitidas:
            self.__caras = caras
        else:
            raise ValueError(f"Número de caras incorrecto: {caras}. Debe ser uno de {self.__caras_permitidas}")
