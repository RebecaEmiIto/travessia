from .humano import AgentePrepostoESHumano
from .auto_bfs import AgenteAutomaticoBfs
from .auto_dfs import AgenteAutomaticoDfs
from .tipos import TiposAgentes

def construir_agente(*args, **kwargs):
    """ Método factory para uma instância Agente arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    tipo_agente = args[0]
    if tipo_agente == TiposAgentes.PREPOSTO_HUMANO:
        return AgentePrepostoESHumano()
    elif tipo_agente == TiposAgentes.AUTO_BFS:
        return AgenteAutomaticoBfs()
    elif tipo_agente == TiposAgentes.AUTO_DFS:
        return AgenteAutomaticoDfs()
    
    raise ValueError("Agente selecionado não encontrado.")