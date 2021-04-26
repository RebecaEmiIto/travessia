class ProblemaTravessia:
    @staticmethod
    def estado_inicial(*argd, **kwargs) -> EstadoTravessia:
        t0 = {'Esquerda': ['Pai', 'Mãe', 'Filho1', 'Filha1', 'Filho2', 'Filha2', 'Policial', 'Prisioneira'],
              'Direita': []}
    @staticmethod
    def teste_objetivo(estado: EstadoTravessia)