from typing import Tuple, Set, Optional
from dataclasses import dataclass

@dataclass
class PercepcoesJogador():
    '''Coloque aqui atributos que descrevam as percepções possíveis de
    mundo por parte do agente jogador
    
    Vide documentação sobre dataclasses em python.
    '''
    personagens: dict = {str: [str], str: [str]}
    mensagem_jogo: Optional[str] = None