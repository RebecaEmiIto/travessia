import sys
from typing import Tuple
from .regras_abstratas import AbstractRegrasJogo
from .personagens import Personagens
# from .resta_um import TabuleiroRestaUm,
from percepcoes import PercepcoesJogador
from acoes import AcoesJogador, DirecaoJangada

sys.path.append("..")

class RegrasTravessia(AbstractRegrasJogo):
    def __init__(self) -> None:
        super().__init__()
        t0 = {"Esquerda": ["Pai", "Mae", "Filho1", "Fliha1", "Filho2", "Fliha2", "Policial", "Prisioneira"],
              "Direita": []}
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
            personagens = set(self.t1),
            mensagem_jogo = self.msg_jogador)

        self.msg_jogador = None
        return percepcoes_jogador
        

    def registrarProximaAcao(self, id_agente, acao):
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        self.acoes_personagens[id_agente] = acao

    def atualizarEstado(self, diferencial_tempo):
        cont = 0
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        acao_jogador = self.acao_personagem[
            self.id_personagem[Personagens.O_JOGADOR]]
        if acao_jogador.tipo == AcoesJogador.Selecionar_Indivíduo:

            p1, p2 = acao_jogador.parametros
            if (p1, p2) in self.t1:
                if self.ValidacaoDireitaEsquerda() is True:
                    if cont % 2 == 0: # esquerda
                        self.t1['Esquerda'].discard(p1, p2)
                        self.t1['Direita'].add(p1, p2)
                        cont += 1
                    else: # direita
                        self.t1['Direita'].discard(p1, p2)
                        self.t1['Esquerda'].add(p1, p2)
                        cont += 1
                else:
                    self.msg_jogador = f'Direção especificada para movimento não é possível.'
            else:
                self.msg_jogador = f'Não há bolinha na coordenada especificada.'
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

def construir_jogo(*args, **kwargs):
    """ Método factory para uma instância RegrasJogo arbitrária, de acordo com os
    parâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    return RegrasTravessia()

