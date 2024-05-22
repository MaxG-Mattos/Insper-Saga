import random
import pygame
import time
from assets import musica, imagem
from game_start_screen_definitivo import tela_inicio
from configuracoes import FPS, BLACK, WHITE, TELA, FONT1, QUIT, INIT, RUNNING1, RUNNING2, RUNNING3, RUNNING4, RUNNING5
from fase1 import fase1
from fase2 import fase2
from FaseFinal import faseFinal
pygame.init()
pygame.mixer.init()
def jogo():
    clock = pygame.time.Clock()
    clock.tick(FPS)
    state = INIT
    while state != QUIT:
        if state == INIT:
            tela_inicio(TELA)
        elif state == RUNNING1:
            fase1(TELA)
        elif state == RUNNING2:
            fase2(TELA)
        elif state == RUNNING5:
            faseFinal(TELA)
        else:
            state = QUIT
        pygame.display.flip()
pygame.quit()