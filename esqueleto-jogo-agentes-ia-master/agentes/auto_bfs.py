import Time
from typing import Tuple
from percepcoes import PercepcoesJogador
from acoes import AcaoJogador 
from .abstrato import AgenteAbstrato
from .problemas import ProblemaTravessia
from .buscadores.busca import busca_arvore_bfs

class AgenteAutomaticoBfs(AgenteAbstrato):
    def __init__(self):
        super.__init__()
        self.count = 0

        self.problema: ProblemaTravessia = None
        self.solucao: list = None
    
    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        AgenteAutomaticoBfs.desenhar_tabuleiro(percepcao_mundo)

        if not self.solucao:
            self.problema = ProblemaTravessia() #TODO: # percepcao_mundo)

    @staticmethod
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
        if not self.solucao:
            no_solucao = busca_arvore_bfs(self.problema)
            self.solucao = no_solucao.caminho_acoes()
            print(len(self.solucao), self.solucao)
            if not self.solucao:
                raise Exception("Agente BFS não encontrou solução.")
        
        acao = self.solucao.pop(0)
        print(f"Próxima ação é {acao}.")
        time.sleep(2)

        p1, p2 = AgenteAutomaticoBfs.traduzir_acao_jogo(acao)
        return AcaoJogador.SelecionarIndividuo(p1, p2)

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
