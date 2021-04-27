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
        estado_resultante = EstadoTravessia(set(estado.tabuleiro))
        p1, p2 = acao.personagem.p1, acao.personagem.p2
        stado_resultante.tabuleiro.add(Personagens(p1, p2))

        if pessoa1 == 'Pai' or pessoa1 == 'Mãe' or pessoa1 == 'Policial' \
            or pessoa2 == 'Pai' or pessoa2 == 'Mãe' or pessoa2 == 'Policial':

                if self.cont % 2 == 0: # Jangada na esquerda
                    # Seleção de 2 pessoas da Esquerda
                    if (pessoa1 in self.t1['Esquerda'] and pessoa2 in self.t1['Esquerda']):
                        self.t1['Esquerda'].remove(pessoa1)
                        self.t1['Esquerda'].remove(pessoa2)
                        self.t1['Direita'].insert(0, pessoa1)
                        self.t1['Direita'].insert(0, pessoa2)

                        # Confere se a jogada é valida,
                        # se sim a Jangada vai para o outro lado, 
                        # senão, retorna erro
                        if self.ValidacaoDireitaEsquerda() is True:
                            self.cont += 1
                        else:
                            self.t1['Direita'].remove(pessoa1)
                            self.t1['Direita'].remove(pessoa2)
                            self.t1['Esquerda'].insert(0, pessoa1)
                            self.t1['Esquerda'].insert(0, pessoa2)
                            raise ValueError("Movimento especificado inválido, cheater!")
                    # Seleção de 1 pessoa da Esquerda
                    elif (pessoa1 in self.t1['Esquerda'] and pessoa2 is None):
                        self.t1['Esquerda'].remove(pessoa1)
                        self.t1['Direita'].insert(0, pessoa1)
                        
                        # Confere se a jogada é valida
                        if self.ValidacaoDireitaEsquerda() is True:
                            self.cont += 1
                        else:
                            self.t1['Direita'].remove(pessoa1)
                            self.t1['Esquerda'].insert(0, pessoa1)
                            raise ValueError("Movimento especificado inválido, cheater!")
                    else:
                        raise ValueError("Movimento especificado inválido, cheater!")
                
                else: # Jangada na direita
                    # Seleção de 2 pessoas da Direita
                    if (pessoa1 in self.t1['Direita'] and pessoa2 in self.t1['Direita']):
                        self.t1['Direita'].remove(pessoa1)
                        self.t1['Direita'].remove(pessoa2)
                        self.t1['Esquerda'].insert(0, pessoa1)
                        self.t1['Esquerda'].insert(0, pessoa2)
                        
                        # Confere se a jogada é valida
                        if self.ValidacaoDireitaEsquerda() is True:
                            self.cont += 1
                        else:
                            self.t1['Esquerda'].remove(pessoa1)
                            self.t1['Esquerda'].remove(pessoa2)
                            self.t1['Direita'].insert(0, pessoa1)
                            self.t1['Direita'].insert(0, pessoa2)
                            raise ValueError("Movimento especificado inválido, cheater!")
                    
                    # Seleção de 1 pessoa da Direita
                    elif (pessoa1 in self.t1['Direita'] and pessoa2 is None):
                        self.t1['Direita'].remove(pessoa1)
                        self.t1['Esquerda'].insert(0, pessoa1)

                        # Confere se a jogada é valida
                        if self.ValidacaoDireitaEsquerda() is True:
                            self.cont += 1
                        else:
                            self.t1['Esquerda'].remove(pessoa1)
                            self.t1['Direita'].insert(0, pessoa1)
                            raise ValueError("Movimento especificado inválido, cheater!")
                    else:
                        raise ValueError("Movimento especificado inválido, cheater!")        
            else:
                raise ValueError("Movimento especificado inválido, cheater!")
        return estado_resultante.tabuleiro
    
        def ValidacaoDireitaEsquerda(self) -> bool:
        """Mais informações sobre as regras no arquivo README.md"""
        tabuleiro = self.t1
        for i in tabuleiro:
            # Lado Esquerdo
            if i == 'Esquerda':
                esquerda = tabuleiro['Esquerda']
                # Regras 5 e 6
                if 'Pai' in esquerda:
                    if ('Filha1' in esquerda) or ('Filha2' in esquerda):
                        if 'Mãe' not in esquerda: return False
                # Regras 3 e 4
                if 'Mãe' in esquerda:
                    if ('Filho1' in esquerda) or ('Filho2' in esquerda):
                        if 'Pai' not in esquerda: return False
                # Regra 7
                if 'Prisioneira' in esquerda:
                    if 'Policial' not in esquerda:
                        if len(esquerda) > 1: return False
            # Lado Direito
            if i == 'Direita':
                direita = tabuleiro['Direita']
                print(len(direita))
                # Regras 5 e 6
                if 'Pai' in direita:
                    if ('Filha1' in direita) or ('Filha2' in direita):
                        if 'Mãe' not in direita: return False
                # Regras 3 e 4
                if 'Mãe' in direita:
                    if 'Filho1' or 'Filho2' in direita:
                        if 'Pai' not in direita: return False
                # Regra 7
                if 'Prisioneira' in direita:
                    if 'Policial' not in direita:
                        if len(direita) > 1: return False
        return True

    @staticmethod
    def teste_objetivo(estado: EstadoRestaUm) -> bool:
        return len(estado.tabuleiro) == 1
    
    @staticmethod
    def custo(inicial: EstadoRestaUm, acao: Mover, 
              resultante: EstadoRestaUm) -> int:
        """Custo em quantidade de jogadas"""
        return 1