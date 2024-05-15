import random
import pygame
import time
from assets import musica, imagens
from classes import *
from game_start_screen_definitivo import tela_inicio, tela
from configuracoes import FPS, BLACK, WHITE, TELA, FONT1, QUIT, INIT, RUNNING1
from fase1 import fase1

def jogo():
    clock = pygame.time.Clock()
    clock.tick(FPS)
    state = INIT
    while state != QUIT:
        if state == INIT:
            tela_inicio(TELA)
        elif state == RUNNING1:
            fase1(TELA)
        else:
            state = QUIT
        pygame.display.flip()
pygame.quit()