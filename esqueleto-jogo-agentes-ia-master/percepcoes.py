from typing import Set, Optional
from dataclasses import dataclass

@dataclass
class PercepcoesJogador():
    '''Coloque aqui atributos que descrevam as percepções possíveis de
    mundo por parte do agente jogador
    
    Vide documentação sobre dataclasses em python.
    '''
    personagens_esquerda: {str: [str]}
    personagens_direita: {str: [str]}
    mensagem_jogo: Optional[str] = None
