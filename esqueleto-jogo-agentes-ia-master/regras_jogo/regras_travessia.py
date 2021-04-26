import sys
from typing import Tuple
from .regras_abstratas import AbstractRegrasJogo
from .personagens import Personagens
# from .resta_um import TabuleiroRestaUm,
from percepcoes import PercepcoesJogador
from acoes import AcoesJogador, Individuo

sys.path.append("..")

class RegrasTravessia(AbstractRegrasJogo):
    def __init__(self) -> None:
        super().__init__()
        t0 = {'Esquerda': ['Pai', 'Mãe', 'Filho1', 'Filha1', 'Filho2', 'Filha2', 'Policial', 'Prisioneira'],
              'Direita': []}
        self.t1 = t0
        contador = 0
        self.cont = contador
        self.id_personagem = {Personagens.O_JOGADOR: 0}
        self.acao_personagem = {0: None}
        self.msg_jogador = None

    def registrarAgentePersonagem(self, personagem:list):
        """ Cria ou recupera id de um personagem agente.
        """
        return self.id_personagem[personagem]

    def isFim(self):
        return len(self.t1["Direita"]) == 8

    def gerarCampoVisao(self, id_agente):
        """ Retorna um EstadoJogoView para ser consumido por um agente
        específico. Objeto deve conter apenas descrição de elementos visíveis
        para este agente.

        EstadoJogoView é um objeto imutável ou uma cópia do jogo, de forma que
        sua manipulação direta não tem nenhum efeito no mundo de jogo real.
        """
        percepcoes_jogador = PercepcoesJogador(
            personagens_esquerda = set(self.t1['Esquerda']),
            personagens_direita = set(self.t1['Direita']),
            mensagem_jogo = self.msg_jogador)

        self.msg_jogador = None
        return percepcoes_jogador
        

    def registrarProximaAcao(self, id_agente, acao):
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        self.acao_personagem[id_agente] = acao

    def atualizarEstado(self, diferencial_tempo):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        acao_jogador = self.acao_personagem[
            self.id_personagem[Personagens.O_JOGADOR]]
        if acao_jogador.tipo == AcoesJogador.Selecionar_Indivíduo:
            p1, p2 = acao_jogador.parametros
            # Devolve o valor(personagem) de cada integer
            pessoa1 = self.decodificar_pessoa(p1)
            pessoa2 = self.decodificar_pessoa(p2)
            
            # Verifica se o Pai, a Mãe ou o Policial estão na Jangada(que são as pessoas que
            # conseguem usar a Jangada), caso contrário, dá "Erro"
            # Regra 2 (README.md)
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
                            self.msg_jogador = f'Movimento inválido.'
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
                            self.msg_jogador = f'Movimento inválido.'
                    else:
                        self.msg_jogador = f'{pessoa1} e/ou {pessoa2} não encontrados.'
                
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
                            self.msg_jogador = f'Movimento inválido.'
                    
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
                            self.msg_jogador = f'Movimento inválido.'
                    else:
                        self.msg_jogador = f'{pessoa1} e/ou {pessoa2} não encontrados.'
            else:
                self.msg_jogador = f'As pessoas selecionadas não podem usar a Jangada.'    
        return 

    def terminarJogo(self):
        """ Faz procedimentos de fim de jogo, como mostrar placar final,
        gravar resultados, etc...
        """
        return

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
    def decodificar_pessoa(p):
        pessoa = int(p)
        if pessoa == 1:
            return 'Pai'
        elif pessoa == 2:
            return 'Mãe'
        elif pessoa == 3:
            return 'Filho1'
        elif pessoa == 4:
            return 'Filha1'
        elif pessoa == 5:
            return 'Filho2'
        elif pessoa == 6:
            return 'Filha2'
        elif pessoa == 7:
            return 'Policial'
        elif pessoa == 8:
            return 'Prisioneira'
        elif pessoa == 0:
            return
            

def construir_jogo(*args, **kwargs):
    """ Método factory para uma instância RegrasJogo arbitrária, de acordo com os
    parâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    return RegrasTravessia()
