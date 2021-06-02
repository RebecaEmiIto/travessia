from typing import Sequence, Set
from dataclasses import dataclass

@dataclass
class Personagens:
    p1: int
    p2: int

    def __hash__(self) -> int:
        return hash(self.p1) + hash(self.p2)
    
    def __str__(self) -> str:
        return f'Pessoa 1: ({self.p1} || Pessoa 2: {self.p2})'

@dataclass
class EstadoTravessia:
    tabuleiro: Set[Personagens]

@dataclass
class Mover:
    personagens: Personagens

    def __str__(self) -> str:
        return f'Mover {self.personagens} para o outro lado do Rio'

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
        for individuo1 in estado.tabuleiro:
            for individuo2 in estado.tabuleiro+1:
                direita = estado.tabuleiro['Direita']
                esquerda = estado.tabuleiro['Esquerda']
                if individuo1 in esquerda:
                    pessoa1, pessoa2 = esquerda.p1, esquerda.p2
                    if Personagens(pessoa1, pessoa2) in esquerda or Personagens(pessoa1) in esquerda:
                        acoes_possiveis.append(Mover(individuo1, individuo2))
                        
                if individuo1 in direita:
                    if Personagens(pessoa1, pessoa2) in direita or Personagens(pessoa1) in direita:
                        acoes_possiveis.append(Mover(individuo1, individuo2))

        return acoes_possiveis
    
    @staticmethod
    def resultado(estado: EstadoTravessia, acao: Mover) -> EstadoTravessia:
        estado_resultante = EstadoTravessia(set(estado.tabuleiro))
        p1 = acao.personagens.p1
        p2 = acao.personagens.p2
        estado_resultante.tabuleiro.add(Personagens(p1, p2))
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
                            raise ValueError("Movimento especificado inválido, cheater!")
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
                            raise ValueError("Movimento especificado inválido, cheater!")
                    else:
                        raise ValueError("Movimento especificado inválido, cheater!")
                
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
                            raise ValueError("Movimento especificado inválido, cheater!")
                    
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
                            raise ValueError("Movimento especificado inválido, cheater!")
                    else:
                        raise ValueError("Movimento especificado inválido, cheater!")        
        else:
            raise ValueError("Movimento especificado inválido, cheater!")
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
