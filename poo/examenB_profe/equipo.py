
class Equipo:
    def __init__(self, nome):
        self.__empatados = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def ganhados(self):
        return self.__ganhados

    @property
    def perdidos(self):
        return self.__perdidos

    @property
    def empatados(self):
        return self.__empatados

    def get_puntos(self):
        return self.__ganhados * 3 + self.__empates

    def add_vitoria(self):
        self.__ganhados += 1

    def add_perdido(self):
        self.__perdidos += 1

    def add_empate(self):
        self.__empates += 1

    def get_encontros_xogados(self):
        return self.__ganhados + self.__empates + self.__perdidos

