#!/usr/bin/env python3

import time
from regras_jogo.regras_travessia import construir_jogo
from regras_jogo.personagens import Personagens
from agentes import construir_agente
from agentes.tipos import TiposAgentes

def ler_tempo(em_turnos=False):
    """ Se o jogo for em turnos, retorna a passada de 1 rodada.
    
    Se não for em turno, é continuo ou estratégico, retorna tempo
    preciso (ns) do relógio.
    """
    return 1 if em_turnos else time.time()


def iniciar_jogo():
    
    # Inicializar e configurar jogo
    jogo = construir_jogo()
    personagem_jogador = jogo.registrarAgentePersonagem(Personagens.O_JOGADOR)
    escolha = int(input("1- Humano joga || 2- Maquina joga "))
    if escolha == 1:
        agente_jogador = construir_agente(TiposAgentes.PREPOSTO_HUMANO, Personagens.O_JOGADOR)
    elif escolha == 2:
        escolha2 = int(input("1- AUTO_BFS || 2- AUTO_DFS "))
        if escolha2 == 1:
            pass
            #agente_jogador = construir_agente(TiposAgentes.AUTO_BFS, Personagens.O_JOGADOR)
        elif escolha2 == 2:
            pass
            # agente_jogador = construir_agente(TiposAgentes.AUTO_DFS, Personagens.O_JOGADOR)
    
    tempo_de_jogo = 0
    while not jogo.isFim():
        
        # Mostrar mundo ao jogador
        ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
        agente_jogador.adquirirPercepcao(ambiente_perceptivel)
        
        # Decidir jogada e apresentar ao jogo
        acao = agente_jogador.escolherProximaAcao()
        jogo.registrarProximaAcao(personagem_jogador, acao)

        # Atualizar jogo
        tempo_corrente = ler_tempo()
        jogo.atualizarEstado(tempo_corrente - tempo_de_jogo)
        tempo_de_jogo += tempo_corrente


if __name__ == '__main__':
    iniciar_jogo()
