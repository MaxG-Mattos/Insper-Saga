import random
import pygame
import time
from assets import musica, imagem
from game_start_screen_definitivo import tela_inicio
from configuracoes import FPS, BLACK, WHITE, TELA, FONT1, QUIT, INIT, RUNNING1, RUNNING2, RUNNING5, ENTRE, ENTRE2
from fase1 import fase1
from fase2 import fase2
from FaseFinal import faseFinal
from Espere import intervalo
from Entre_Fases_2 import ninja_time

tela = TELA
pygame.display.set_caption('Insper Saga: A Vida Não Tá Fácil')
pygame.init()
pygame.mixer.init()

state = INIT
running = True
while running:
    if state == INIT:
        state = tela_inicio(tela)
        pygame.time.wait(80)
    elif state == RUNNING1:
        state = fase1(tela)
    elif state == ENTRE2:
        state = ninja_time(tela)
        pygame.time.wait(80)
    elif state == RUNNING2:
        state = fase2(tela)
    elif state == ENTRE:
        state = intervalo(tela)
        pygame.time.wait(80)
    elif state == RUNNING5:
        state = faseFinal(tela)
    else:
        state = QUIT
        running = False





pygame.quit()