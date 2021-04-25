from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
    Selecionar_Indivíduo = 'SelecionarIndividuo'

class Individuo(Enum):
    Pai = 'Pai'
    Mae = 'Mãe'
    Filho1 = 'Filho1'
    Filha1 = 'Filha1'
    Filho2 = 'Filho2'
    Filha2 = 'Filha2'
    Policial = 'Policial'
    Prisioneira = 'Prisioneira'

@dataclass
class AcaoJogador():
    tipo: str
    parametros: tuple = tuple() 

    @classmethod
    def SelecionarIndividuo(cls, p1: Individuo, p2: Individuo) -> 'AcaoJogador':
        print(f'{p1} & {p2}')
        return cls(AcoesJogador.Selecionar_Indivíduo, (p1, p2))

    def Validacao(self, p1: int, p2: int):
        if p1 == "Pai":
            if p2 == "Filha1" or p2 == "Filha2":
                return False
        elif p1 == "Mae":
            if p2 == "Filho1" or p2 == "Filho2":
                return False
        elif p1 == "Prisioneira":
            if p2 != "Policial":
                return False
