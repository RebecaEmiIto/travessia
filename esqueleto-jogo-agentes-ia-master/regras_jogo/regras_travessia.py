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
        t0 = {'Esquerda': ['Pai', 'Mae', 'Filho1', 'Fliha1', 'Filho2', 'Fliha2', 'Policial', 'Prisioneira'],
              'Direita': []}
        self.t1 = t0
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
        cont = 0
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        acao_jogador = self.acao_personagem[
            self.id_personagem[Personagens.O_JOGADOR]]
        if acao_jogador.tipo == AcoesJogador.Selecionar_Indivíduo:
            p1, p2 = acao_jogador.parametros

            pessoa1 = self.decodificar_pessoa(p1)
            pessoa2 = self.decodificar_pessoa(p2)
        
            if (p1 in self.t1 and p2 in self.t1):
                if self.ValidacaoDireitaEsquerda() is True:
                    if cont % 2 == 0: # esquerda
                        self.t1['Esquerda'].remove(pessoa1)
                        self.t1['Esquerda'].remove(pessoa2)
                        self.t1['Direita'].add(pessoa1)
                        self.t1['Direita'].add(pessoa2)
                        cont += 1
                    else: # direita
                        self.t1['Direita'].remove(pessoa1)
                        self.t1['Direita'].remove(pessoa2)
                        self.t1['Esquerda'].add(pessoa1)
                        self.t1['Esquerda'].add(pessoa2)
                        cont += 1
                else:
                    self.msg_jogador = f'Movimento inválido.'
            else:
                self.msg_jogador = f'{pessoa1} e/ou {pessoa2} não encontrados.'
        else:
            self.msg_jogador = f'Ação especificada inválida.'    
            
        return 

    def terminarJogo(self):
        """ Faz procedimentos de fim de jogo, como mostrar placar final,
        gravar resultados, etc...
        """
        return

    def ValidacaoDireitaEsquerda(self) -> bool:
        tabuleiro = self.t1
        for i in tabuleiro:
            
            if i == "Esquerda":
                esquerda = tabuleiro["Esquerda"]
            
                for j in range(len(esquerda)):
            
                    if esquerda[j] == "Pai":
                        if "Filha1" or "Filha2" in esquerda:
                            if "Mae" in esquerda: return True
                            else: return False

                    if esquerda[j] == "Mae":
                        if "Filho1" or "Filho2" in esquerda:
                            if "Pai" in esquerda: return True
                            else: return False
                    
                    if esquerda[j] == "Prisioneira":
                        if "Policial" in esquerda: return True
                        elif len(esquerda) == 1: return True
                        else: return False
            
            if i == "Direita":
                esquerda = tabuleiro["Esquerda"]
            
                for j in range(len(esquerda)):
                    if esquerda[j] == "Pai":
                        if "Filha1" or "Filha2" in esquerda:
                            if "Mae" in esquerda: return True
                            else: return False
                    
                    if esquerda[j] == "Mae":
                        if "Filho1" or "Filho2" in esquerda:
                            if "Pai" in esquerda: return True
                            else: return False
                    
                    if esquerda[j] == "Prisioneira":
                        if "Policial" in esquerda: return True
                        elif len(esquerda) == 1: return True
                        else: return False

    @staticmethod
    def decodificar_pessoa(pessoa):
        if pessoa == Individuo.Pai:
            return 'Pai'
        elif pessoa == Individuo.Mae:
            return 'Mãe'
        elif pessoa == Individuo.Filho1:
            return 'Filho1'
        elif pessoa == Individuo.Filha1:
            return 'Filha1'
        elif pessoa == Individuo.Filho2:
            return 'Filho2'
        elif pessoa == Individuo.Filha2:
            return 'Filha2'
        elif pessoa == Individuo.Policial:
            return 'Policial'
        elif pessoa == Individuo.Prisioneira:
            return 'Prisioneira'

def construir_jogo(*args, **kwargs):
    """ Método factory para uma instância RegrasJogo arbitrária, de acordo com os
    parâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    return RegrasTravessia()

