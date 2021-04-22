from agentes.abstrato import AgenteAbstrato

class AgentePrepostoESHumano(AgenteAbstrato):

    def adquirirPercepcao(self, percepcao_mundo):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        print("--- Tabuleiro após a ultima jogada: ---\n")
    
    def escolherProximaAcao(self):
        jogada = None
        count = 0
        while not jogada:
            jogada = input("Escreva sua jogada no formato [Pessoa1, Pessoa2]")
            #Printa as pessoas
            print("Margem Esquerda".center(25, "-"))
            if count % 2 == 0:
                print("Jangada \n")
            else:
                print("\n Jangada")
            print("Margem Direita".center(26, "-"))
            #Printa as pessoas
            count += 1
            if not AgentePrepostoESHumano.is_jogada_valida():
                pass

@staticmethod
def is_jogada_valida():
    pass