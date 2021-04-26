from typing import Tuple
from .abstrato import AgenteAbstrato
from percepcoes import PercepcoesJogador
from acoes import AcaoJogador 
from .problemas import ProblemaTravessia


class AgenteAutomaticoBfs(AgenteAbstrato):
    def __init__(self):
        super.__init__()
        self.count = 0

        self.ProblemaTravessia
    
    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        AgenteAutomaticoBfs.desenhar_tabuleiro(percepcao_mundo)

        if not self.solucao:
            self.problema = ProblemaTravessia() #TODO: # percepcao_mundo)

    def desenhar_tabuleiro(percepcao_mundo: PercepcoesJogador):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        print('--- Tabuleiro após a ultima jogada: ---\n')
        print('# 1-Pai ; 2-Mãe ; 3-Filho1 ; 4-Filha1 ; 5-Filho2 ; 6-Filha2 ; 7-Policial ; 8-Prisioneira #\n')

        print(percepcao_mundo.personagens_esquerda)

        print('Margem Esquerda'.center(81, '-'))

        if self.count % 2 == 0:
            print('Jangada \n')
        else:
            print('\n Jangada')

        print('Margem Direita'.center(81, '-'))

        print(percepcao_mundo.personagens_direita)
        
        if percepcao_mundo.mensagem_jogo:
            print(f'Mensagem do jogo: {percepcao_mundo.mensagem_jogo}')
        else:
            self.count += 1

    def escolherProximaAcao(self):  
        if not self.seq:
            self.formularObjetivo()
            self.formularProblema()
            self.busca()
            if not self.seq:
                return None
        acao = self.seq.pop(0)
        return acao

    @staticmethod
    def parse_jogada(entrada: str) -> Tuple[int, int]:
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
        if len(entrada) == 3:
            p1, p2 = entrada.split(',')
            return p1, p2
        elif len(entrada) < 3:
            p1 = int(entrada)
            return p1
