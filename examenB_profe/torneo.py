from equipo import Equipo


class Torneo:
    def __init__(self, nome: str, num_max_equipos: int):
        self.__nome = nome
        self.__equipos = []
        self.__num_max_equipos = num_max_equipos
        self.__num_equipos = 0

    @property
    def nome(self):
        return self.__nome

    def get_equipo(self, nome):
        for equipo in self.__equipos:
            if equipo.nome == nome:
                return equipo
        return None

    def add_equipo(self, equipo):
        if len(self.__equipos) < self.__num_max_equipos:
            if not equipo in self.__equipos:
                self.__equipos.append(equipo)
                return len(self.__equipos) -1
            else:
                return -1
        else:
            return -1

    def rexistrar_encotro(self, encontro_resultado):
        """Celta-Rayo 4-2"""
        encontro, resultado = encontro_resultado.split()
        nome_local, nome_visitante = encontro.split('-')
        r_local, r_visitante = resultado.split('-')
        local = self.get_equipo(nome_local)
        visitante = self.get_equipo(nome_visitante)
        if local is not None and visitante is not None:
            if int(r_local) > int(r_visitante):
                local.add_victoria()
                visitante.add_derrota()
            elif int(r_local) < int(r_visitante):
                local.add_derrota()
                visitante.add_victoria()
            else:
                local.add_empate()
                visitante.add_empate()
        else:
            raise ValueError("Un dos equipos non esta na lista do torneo")

    def importar_resultados_ficheiro2(self, ruta):
        """ """
        with open(ruta, 'r') as ficheiro:
            for linha in ficheiro:
                espazo1 = linha.index(" ")
                espazo2 = linha.index(" ", espazo1+1)
#                 TODO: terminar

if __name__ == "__main__":
    t = Torneo("Tutextren", 4)
    e = Equipo("Turolense")
