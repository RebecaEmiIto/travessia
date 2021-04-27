#from node import Node

"""
public String bfs() {

        if (self.root == null) {
            return "";
        }
        Queue<Node> fila = new LinkedList<>();
        fila.add(self.root);

        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("[");
        while (!fila.isEmpty()) {
            Node aux = fila.remove();

            stringBuilder.append(" " + aux + " ");

            if (aux.getLeft() != null) {
                fila.add(aux.getLeft());
            }

            if (aux.getRight() != null) {
                fila.add(aux.getRight());
            }
        }

        stringBuilder.append("]");
        return stringBuilder.toString();

    }


    public String dfs() {

        if (self.root == null) {
            return "";
        }
        Stack<Node> pilha = new Stack();
        pilha.add(self.root);

        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("[");
        while (!pilha.isEmpty()) {
            Node aux = pilha.pop();

            stringBuilder.append(" " + aux + " ");

            if (aux.getLeft() != null) {
                pilha.push(aux.getLeft());
            }

            if (aux.getRight() != null) {
                pilha.push(aux.getRight());
            }
        }

        stringBuilder.append("]");
        return stringBuilder.toString();
"""
#class Arvore_bfs():
#    def bfs():
#        root = Node.__init__()

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
        custo_solucao = pai.custo_solucao + problema.custo(pai.estado, acao, novo_estado)
        return cls(novo_estado, acao, custo_solucao, pai)
    
    def __repr__(self) -> str:
        return f'No({self.estado!r},{self.acao!r})'


def busca_em_arvore(problema) -> No:
    """ Retorna uma solucao ou falha"""
    borda = [No(problema.estado_inicial())]
    while borda:

        folha = borda.pop(0)
        # print(f"Altura {folha.calcular_profundidade()}, com {len(borda)} nós na borda.")
        if problema.teste_objetivo(folha.estado):
            return folha

        # print(f'Não era objetivo. Ações adjacentes são {problema.acoes(folha.estado)}.')
        for acao in problema.acoes(folha.estado):
            expandido = No.criar_no_filho(problema, folha, acao)
            borda.append(expandido)

            # print(f'Enfileirado {expandido}')

    raise ProblemaSemSolucaoException()

busca_arvore_bfs = busca_em_arvore