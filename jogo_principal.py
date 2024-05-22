import random
import pygame
import time
from assets import musica, imagem
from game_start_screen_definitivo import tela_inicio
from configuracoes import FPS, BLACK, WHITE, TELA, FONT1, QUIT, INIT, RUNNING1, RUNNING2, RUNNING5
from fase1 import fase1
from fase2 import fase2
from FaseFinal import faseFinal

tela = TELA
pygame.display.set_caption('Insper Saga: A Vida Não Tá Fácil')
pygame.init()
pygame.mixer.init()

state = INIT
running = True
while running:
    if state == INIT:
        state = tela_inicio(tela)
    elif state == RUNNING1 and state != 0:
        state = fase1(tela)
    elif state == RUNNING2 and state != 0:
        state = fase2(tela)
    elif state == RUNNING5 and state != 0:
        state = faseFinal(tela)
    else:
        state = QUIT





pygame.quit()