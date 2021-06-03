from typing import Sequence, Set
from dataclasses import dataclass

from typing import Sequence, Set
from dataclasses import dataclass


@dataclass
class Personagens:
    x: int

    def __hash__(self) -> int:
        return hash(self.x)
    
    def __str__(self) -> str:
        return f'{self.x}'

@dataclass
class EstadoTravessia:
    tabuleiro: Set[Personagens]


@dataclass
class Mover:
    personagens: Personagens
    personagens2: Personagens

    def __str__(self) -> str:
        return f'Mover {self.personagens} e {self.personagens2} para o outro lado'

class ProblemaTravessia:
    
    @staticmethod
    def estado_inicial(*argd, **kwargs) -> EstadoTravessia:
        nivel = {
            #'t0': EstadoTravessia({
            #    'Esquerda': [ 1, 2, 3, 4, 5, 6, 7, 8 ],
            #    'Direita': []
            #})
            't0': EstadoTravessia({
                'Esquerda': [Personagens(1),Personagens(2),Personagens(3),Personagens(4),Personagens(5),Personagens(6),Personagens(7),Personagens(8)],
                'Direita': []
            })
        }
        return nivel[kwargs.get('nivel', 't0')]
    
    @staticmethod
    def acoes(estado: EstadoTravessia) -> Sequence[Mover]:
        acoes_possiveis = list()

        direita = estado.tabuleiro['Direita']
        esquerda = estado.tabuleiro['Esquerda']
        if count % 2 == 0:
            for individuo1 in estado.tabuleiro['Esquerda']:
                for individuo2 in estado.tabuleiro['Esquerda']:
            
                    x, y = str(individuo1), str(individuo2)
                    pessoa1, pessoa2 = esquerda[int(x)-1], esquerda[int(y)-1]
                    if pessoa1 in esquerda:
                        #print(f'1: {Personagens(pessoa1)}, 2: {Personagens(pessoa2)}')
                        #print('estoy aui')
                        acoes_possiveis.append(Mover(individuo1, None))
                        #Personagens(pessoa1, pessoa2)
                    
                    if (pessoa1 in esquerda and pessoa2 in esquerda ) or pessoa1 in esquerda:
                        acoes_possiveis.append(Mover(individuo1, individuo2))

            for individuo1 in estado.tabuleiro['Direita']:            
                for individuo2 in estado.tabuleiro['Direita']:

                    x, y = str(individuo1), str(individuo2)
                    pessoa1, pessoa2 = direita[int(x)-1], direita[int(y)-1]

                    if pessoa1 in direita:
                        acoes_possiveis.append(Mover(individuo1, None))
                        #(Personagens(pessoa1) in direita and Personagens(pessoa2) in direita )
                    
                    if (pessoa1 in direita and pessoa2 in direita ) or pessoa1 in direita:
                        acoes_possiveis.append(Mover(individuo1, individuo2))

        #print(f'adsadasd {acoes_possiveis}')
        return acoes_possiveis
    
    @staticmethod
    def resultado(estado: EstadoTravessia, acao: Mover) -> EstadoTravessia:
        estado_resultante = EstadoTravessia(set(estado.tabuleiro))
        p1 = acao.personagens.x
        estado_resultante.tabuleiro.add(Personagens(p1))
        if acao.personagens2 is None:
            p2 = None
        else:
            p2 = acao.personagens2.x
            estado_resultante.tabuleiro.add(Personagens(p2))
        contador = 0
        if p1 == 'Pai' or p1 == 'Mãe' or p1 == 'Policial' \
            or p2 == 'Pai' or p2 == 'Mãe' or p2 == 'Policial':

                if contador % 2 == 0: # Jangada na esquerda
                    # Seleção de 2 pessoas da Esquerda
                    if (p1 in estado_resultante['Esquerda'] and p2 in estado_resultante['Esquerda']):
                        estado_resultante['Esquerda'].remove(p1)
                        estado_resultante['Esquerda'].remove(p2)
                        estado_resultante['Direita'].insert(0, p1)
                        estado_resultante['Direita'].insert(0, p2)

                        # Confere se a jogada é valida,
                        # se sim a Jangada vai para o outro lado, 
                        # senão, retorna erro
                        if EstadoTravessia.ValidacaoDireitaEsquerda() is True:
                            contador += 1
                        else:
                            estado_resultante['Direita'].remove(p1)
                            estado_resultante['Direita'].remove(p2)
                            estado_resultante['Esquerda'].insert(0, p1)
                            estado_resultante['Esquerda'].insert(0, p2)
                            #raise ValueError(f'Movimento especificado inválido, cheater! 1: {p1}, 2: {p2}')
                    # Seleção de 1 pessoa da Esquerda
                    elif (p1 in estado_resultante['Esquerda'] and p2 is None):
                        estado_resultante['Esquerda'].remove(p1)
                        estado_resultante['Direita'].insert(0, p1)
                        
                        # Confere se a jogada é valida
                        if EstadoTravessia.ValidacaoDireitaEsquerda() is True:
                            contador += 1
                        else:
                            estado_resultante['Direita'].remove(p1)
                            estado_resultante['Esquerda'].insert(0, p1)
                            raise ValueError(f'Movimento especificado inválido, cheater! 1: {p1}, 2: {p2}')
                    #else:
                    #    raise ValueError(f'Movimento especificado inválido, cheater! 1: {p1}, 2: {p2}')
                
                else: # Jangada na direita
                    # Seleção de 2 pessoas da Direita
                    if (p1 in estado_resultante['Direita'] and p2 in estado_resultante['Direita']):
                        estado_resultante['Direita'].remove(p1)
                        estado_resultante['Direita'].remove(p2)
                        estado_resultante['Esquerda'].insert(0, p1)
                        estado_resultante['Esquerda'].insert(0, p2)
                        
                        # Confere se a jogada é valida
                        if EstadoTravessia.ValidacaoDireitaEsquerda() is True:
                            contador += 1
                        else:
                            estado_resultante['Esquerda'].remove(p1)
                            estado_resultante['Esquerda'].remove(p2)
                            estado_resultante['Direita'].insert(0, p1)
                            estado_resultante['Direita'].insert(0, p2)
                            #raise ValueError(f'Movimento especificado inválido, cheater! 1: {p1}, 2: {p2}')
                    
                    # Seleção de 1 pessoa da Direita
                    elif (p1 in estado_resultante['Direita'] and p2 is None):
                        estado_resultante['Direita'].remove(p1)
                        estado_resultante['Esquerda'].insert(0, p1)

                        # Confere se a jogada é valida
                        if EstadoTravessia.ValidacaoDireitaEsquerda() is True:
                            contador += 1
                        else:
                            estado_resultante['Esquerda'].remove(p1)
                            estado_resultante['Direita'].insert(0, p1)
                            #raise ValueError(f'Movimento especificado inválido, cheater! 1: {p1}, 2: {p2}')
                    #else:
                        #raise ValueError(f'Movimento especificado inválido, cheater! 1: {p1}, 2: {p2}')        
        #else:
        #    raise ValueError(f'Movimento especificado inválido, cheater! 1: {p1}, 2: {p2}')
        print(f'estado resultante tabu = {estado_resultante}')
        return estado_resultante
    
    def ValidacaoDireitaEsquerda(self) -> bool:
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
    def teste_objetivo(estado: EstadoTravessia) -> bool:
        print(f'tamanho = {len(estado.tabuleiro)}')
        return len(estado.tabuleiro) == 1
    
    @staticmethod
    def custo(inicial: EstadoTravessia, acao: Mover,
              resultante: EstadoTravessia) -> int:
        """Custo em quantidade de jogadas"""
        return 1
