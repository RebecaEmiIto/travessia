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
        return cls(AcoesJogador.Selecionar_Indivíduo, (p1, p2))