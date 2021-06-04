from typing import Any, Optional
from dataclasses import dataclass

class ProblemaSemSolucaoException(Exception):
    pass

@dataclass
class No():
    estado: Any
    acao: Optional[Any] = None
    custo_solucao: int = 0
    pai: Optional['No'] = None

    def calcular_profundidade(self):
        raiz = not self.pai
        return 0 if raiz else self.pai.calcular_profundidade() + 1

    def caminho_acoes(self) -> list:
        """Retorna uma lista com as ações em ordem para atingir o estado
        que este nó armazena.
        """
        raiz = not self.pai
        return [] if raiz else self.pai.caminho_acoes() + [self.acao]

    @classmethod
    def criar_no_filho(cls, problema, pai, acao):
        novo_estado = problema.resultado(pai.estado, acao)
        #print(f'novo estado = {novo_estado}')
        custo_solucao = pai.custo_solucao + problema.custo(pai.estado, acao, novo_estado)
        return cls(novo_estado, acao, custo_solucao, pai)

    def __repr__(self) -> str:
        return f'No({self.estado!r},{self.acao!r})'


def busca_em_arvore(problema, count) -> No:
    """ Retorna uma solucao ou falha"""
    #print(f'problema:::: {problema.estado_inicial()}')
    borda = [No(problema.estado_inicial())]
    #print(f'borda: {borda}')
    while borda:
        #print(f'borda {borda}')
        folha = borda.pop(0)
        #print(f'folha = {folha}')
        #print(f"Altura {folha.estado}, com {len(borda)} nós na borda.")
        if problema.teste_objetivo(folha.estado):
            #print(f'folha sdfs')

            return folha

        #print(f'estado = {estado} e acao = {acao}')
        # print(f'Não era objetivo. Ações adjacentes são {problema.acoes(folha.estado)}.')
        #print(f'pajncsdv {folha}')
        lista = []
        lista.append(folha)
        if count%2 == 0:
            for acao in problema.acoesE(folha.estado):
                print(f'kkkkESQ {acao}')
                expandido = No.criar_no_filho(problema, folha, acao)
                borda.append(expandido)
        else:
            for acao in problema.acoesD(folha.estado):
                    print(f'kkkkDIR {acao}')
                    expandido = No.criar_no_filho(problema, folha, acao)
                    borda.append(expandido)

            # print(f'Enfileirado {expandido}')

    raise ProblemaSemSolucaoException()
    print(f'alo')
    
busca_arvore_bfs = busca_em_arvore

def busca_em_dfs(problema) -> No:
    """ Retorna uma solucao ou falha"""
    borda = [No(problema.estado_inicial())]
    while borda:
        folha = borda.pop()
        # print(f"Altura {folha.calcular_profundidade()}, com {len(borda)} nós na borda.")
        if problema.teste_objetivo(folha.estado):
            print(f'folha sdfs')
            return folha

        #print(f'Não era objetivo. Ações adjacentes são {problema.acoes(folha.estado)}.')
        for acao in problema.acoes(folha.estado):
            #print(f'Não era objetivo. Ações adjacentes são {problema.acoes(folha.estado)}.')
            expandido = No.criar_no_filho(problema, folha, acao)
            borda.append(expandido)
            #print(f'kkkk {borda}')

            # print(f'Enfileirado {expandido}')

    raise ProblemaSemSolucaoException()
    print(f'alo pao')


busca_arvore_dfs = busca_em_dfs