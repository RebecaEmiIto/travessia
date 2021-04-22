from typing import Tuple
from .regras_abstratas import AbstractRegrasJogo
from .personagens import Personagens
#from .resta_um import TabuleiroRestaUm, 
from percepcoes import PercepcoesJogador
from acoes import AcoesJogador, SelecionarIndividuo

class RegrasTravessia(AbstractRegrasJogo):    

    def __init__(self) -> None:
        super().__init__()
        t0 = {"Esquerda": ["Pai", "Mae", "Filho1", "Fliha1", "Filho2", "Fliha2", "Policial", "Prisioneira"], "Direita": [] }
        self.t1 = t0
        self.id_personagem = {Personagens.O_JOGADOR}
        self.acao_personagem = {0 : None}
    
    def isFim(self) -> bool:
        # Se Lado direito = 0, encerra jogo
        return super().isFim()

    def ValidacaoDireitaEsquerda(self) -> bool:
        for i in t1:
            
            if i == "Esquerda":
                esquerda = t1["Esquerda"]
            
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
                esquerda = t1["Esquerda"]
            
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

    def construir_jogo(*args,**kwargs):
        """ Método factory para uma instância RegrasJogo arbitrária, de acordo com os
        parâmetros. Pode-se mudar à vontade a assinatura do método.
        """
        return RegrasTravessia()