from agentes.abstrato import AgenteAbstrato
from typing import Tuple
from agentes.abstrato import AgenteAbstrato
from percepcoes import PercepcoesJogador
from acoes import AcaoJogador, DirecaoMoverBolinha

class AgentePrepostoESHumano(AgenteAbstrato):

    count = 0
    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
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

        linhas, colunas = percepcao_mundo.dimensoes
        start_linha, stop_linha = linhas//2, -1 * linhas//2
        start_coluna, stop_coluna = -1 * (colunas//2), colunas//2 + 1

        print("+-3210123+")
        for linha in range(start_linha, stop_linha, -1):
            print_linha = f'{abs(linha)} '
            for coluna in range(start_coluna, stop_coluna, 1):
                if (coluna, linha) in percepcao_mundo.pos_bolinhas:
                    print_linha += 'o'
                else:
                    print_linha += '.'
        
            print(print_linha)
        print('-')

        if percepcao_mundo.mensagem_jogo:
            print(f'Mensagem do jogo: {percepcao_mundo.mensagem_jogo}')
    
    def escolherProximaAcao(self):
        jogada = None
        while not jogada:
            jogada = input("Escreva sua jogada no formato [x,y,d]: ").strip()
            try:                
                x, y, d = AgentePrepostoESHumano.parse_jogada(jogada)            
            except ValueError:
                jogada = None
                print("Jogada entrada é inválida. Tente novamente.")

        return AcaoJogador.mover_bolinha(x, y, d)

    @staticmethod
    def parse_jogada(entrada: str) -> Tuple[int, int, str]:
        direcoes = {
            'd': DirecaoMoverBolinha.DIREITA,
            'e': DirecaoMoverBolinha.ESQUERDA,
            'c': DirecaoMoverBolinha.CIMA,
            'b': DirecaoMoverBolinha.BAIXO
        }

        raw_x, raw_y, raw_d = entrada.split(',')
        x, y, d = int(raw_x), int(raw_y), direcoes.get(raw_d.lower())
        if not d:
            raise ValueError()
        
        return x, y, d