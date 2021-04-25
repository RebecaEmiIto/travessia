from typing import Tuple
from .abstrato import AgenteAbstrato
from percepcoes import PercepcoesJogador
from acoes import AcaoJogador, Individuo

class AgentePrepostoESHumano(AgenteAbstrato):
    
    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        count = 0
        print("--- Tabuleiro após a ultima jogada: ---\n")
        print("# 1-Pai ; 2-Mãe ; 3-Filho1 ; 4-Filha1 ; 5-Filho2 ; 6-Filha2 ; 7-Policial ; 8-Prisioneira #\n")

        print(percepcao_mundo.personagens_esquerda)

        print("Margem Esquerda".center(81, "-"))

        if count % 2 == 0:
            print("Jangada \n")
        else:
            print("\n Jangada")

        print("Margem Direita".center(81, "-"))

        print(percepcao_mundo.personagens_direita)

        count += 1
        if percepcao_mundo.mensagem_jogo:
            print(f'Mensagem do jogo: {percepcao_mundo.mensagem_jogo}')
    
    def escolherProximaAcao(self):  
        jogada = 0
        while not jogada:
            jogada = input("Escreva sua jogada no formato [Pessoa1,Pessoa2]\n").strip()
            try:
                p1, p2 = AgentePrepostoESHumano.parse_jogada(jogada)
                #print(f'{p1} e {p2}')
            except ValueError:
                jogada = 9
                print("Jogada entrada é inválida. Tente novamente.")

        return AcaoJogador.SelecionarIndividuo(p1, p2)

    @staticmethod
    def parse_jogada(entrada: str) -> Tuple[int, int]:
        #print(entrada)
        pessoa = {
            1: Individuo.Pai,
            2: Individuo.Mae,
            3: Individuo.Filho1,
            4: Individuo.Filha1,
            5: Individuo.Filho2,
            6: Individuo.Filha2,
            7: Individuo.Policial,
            8: Individuo.Prisioneira
        }
        p1, p2 = entrada.split(',')
        #if not d:
        #   raise ValueError()

        return p1, p2
