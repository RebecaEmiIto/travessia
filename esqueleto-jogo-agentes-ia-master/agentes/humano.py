
from typing import Tuple
from .abstrato import AgenteAbstrato
from percepcoes import PercepcoesJogador
from acoes import AcaoJogador, DirecaoJangada

class AgentePrepostoESHumano(AgenteAbstrato):
    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        count = 0
        print("--- Tabuleiro após a ultima jogada: ---\n")
        for i in PercepcoesJogador.personagens:
            print(i["Esquerda"])
                
            print("Margem Esquerda".center(25, "-"))
            
            if count % 2 == 0:
                print("Jangada \n") 
            else:
                print("\n Jangada")

            print("Margem Direita".center(26, "-"))
    
            print(i["Direita"])
                
            count += 1
            if percepcao_mundo.mensagem_jogo:
                print(f'Mensagem do jogo: {percepcao_mundo.mensagem_jogo}')
    
    def escolherProximaAcao(self):  
        jogada = None
        while not jogada:
            jogada = input("Escreva sua jogada no formato [Pessoa1, Pessoa2]")
            if not AgentePrepostoESHumano.parse_jogada():
                pass

    @staticmethod
    def parse_jogada(entrada: str) -> {str: [str], str: [str]}:
        
        raw_p1, raw_p2 = entrada.split(',')
        p1, p2 = str(raw_p1), str(raw_p2)
        
        return p1, p2

    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        print("\nTabuleiro após a última jogada.")
