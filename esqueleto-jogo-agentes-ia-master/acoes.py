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
    def SelecionarIndividuo(cls, p1, p2, direcao: DirecaoJangada):
        return cls(AcoesJogador.Selecionar_Indivíduo, (p1, p2))