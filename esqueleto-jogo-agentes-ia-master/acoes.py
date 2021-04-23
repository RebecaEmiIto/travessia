from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
    Selecionar_Indivíduo = 'SelecionarIndividuo'

class DirecaoJangada(Enum):
    Direita = 'Direita'
    Esquerda = 'Esquerda'

@dataclass
class AcaoJogador():
    tipo: str
    parametros: tuple = tuple() 

    @classmethod
    def SelecionarIndividuo(cls, p1: str, p2: str, direcao: DirecaoJangada) -> 'AcaoJogador':
        return cls(AcoesJogador.Selecionar_Indivíduo, (p1, p2, direcao))

    def Validacao(self, p1: str, p2: str):
        if p1 == "Pai":
            if p2 == "Filha1" or p2 == "Filha2":
                return False
        elif p1 == "Mae":
            if p2 == "Filho1" or p2 == "Filho2":
                return False
        elif p1 == "Prisioneira":
            if p2 != "Policial":
                return False


