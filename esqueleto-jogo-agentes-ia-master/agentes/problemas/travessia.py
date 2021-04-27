from typing import Sequence, Set
from dataclasses import dataclass

@dataclass
class Personagens:
    p1: str
    p2: str

    def __hash__(self) -> int:
        return hash(self.p1) + hash(self.p2)
    
    def __str__(self) -> str:
        return f'Pessoa 1: ({self.p1} || Pessoa 2: {self.p2})'

@dataclass
class EstadoTravessia:
    tabuleiro: Personagens

@dataclass
class Mover:
    personagens: Personagens

    def __str__(self) -> str:
        return f'Mover({self.personagens} para o outro lado do Rio)'

class ProblemaTravessia:

    @staticmethod
    def estado_inicial(*argd, **kwargs) -> EstadoTravessia:
        t0 = {'Esquerda': ['Pai', 'Mãe', 'Filho1', 'Filha1', 'Filho2', 'Filha2', 'Policial', 'Prisioneira'],
              'Direita': []}
        return t0[kwargs.get('nivel', 'completo')]
    
    @staticmethod
    def acoes(estado: EstadoRestaUm) -> Sequence[Mover]:
        acoes_possiveis = list()
        for bolinha in estado.tabuleiro:
            x, y = bolinha.x, bolinha.y

            if Bolinha(x+1,y) in estado.tabuleiro and Bolinha(x+2,y) not in estado.tabuleiro:
                x_max = 3 if abs(y) < 2 else 1
                if x+2 <= x_max:
                    acoes_possiveis.append(Mover(bolinha, 'direita'))
            
            if Bolinha(x-1,y) in estado.tabuleiro and Bolinha(x-2,y) not in estado.tabuleiro:
                x_min = -3 if abs(y) < 2 else -1
                if x-2 >= x_min:
                    acoes_possiveis.append(Mover(bolinha, 'esquerda'))
            
            if Bolinha(x,y+1) in estado.tabuleiro and Bolinha(x,y+2) not in estado.tabuleiro:
                y_max = 3 if abs(x) < 2 else 1
                if y+2 <= y_max:
                    acoes_possiveis.append(Mover(bolinha, 'cima'))
            
            if Bolinha(x,y-1) in estado.tabuleiro and Bolinha(x,y-2) not in estado.tabuleiro:
                y_min = -3 if abs(x) < 2 else -1
                if y-2 >= y_min:
                    acoes_possiveis.append(Mover(bolinha, 'baixo'))
        
        return acoes_possiveis
    
    @staticmethod
    def resultado(estado: EstadoRestaUm, acao: Mover) -> EstadoRestaUm:
        estado_resultante = EstadoRestaUm(set(estado.tabuleiro))
        x, y = acao.bolinha.x, acao.bolinha.y
        
        estado_resultante.tabuleiro.discard(acao.bolinha)
        if acao.direcao == 'cima':
            estado_resultante.tabuleiro.discard(Bolinha(x, y+1))
            estado_resultante.tabuleiro.add(Bolinha(x, y+2))
        
        elif acao.direcao == 'baixo':
            estado_resultante.tabuleiro.discard(Bolinha(x, y-1))
            estado_resultante.tabuleiro.add(Bolinha(x, y-2))

        elif acao.direcao == 'direita':
            estado_resultante.tabuleiro.discard(Bolinha(x+1, y))
            estado_resultante.tabuleiro.add(Bolinha(x+2, y))
        
        elif acao.direcao == 'esquerda':
            estado_resultante.tabuleiro.discard(Bolinha(x-1, y))
            estado_resultante.tabuleiro.add(Bolinha(x-2, y))
        
        else:
            raise ValueError("Movimento especificado inválido, cheater!")
        
        return estado_resultante
    
    @staticmethod
    def teste_objetivo(estado: EstadoRestaUm) -> bool:
        return len(estado.tabuleiro) == 1
    
    @staticmethod
    def custo(inicial: EstadoRestaUm, acao: Mover, 
              resultante: EstadoRestaUm) -> int:
        """Custo em quantidade de jogadas"""
        return 1