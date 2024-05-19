import random
import pygame
import time
from assets import musica, imagens
from classes import *
from configuracoes import FPS, BLACK, WHITE, TELA, FONT1, QUIT, INIT, RUNNING1, RED

pygame.init()
pygame.mixer_music.load(musica['segunda fase'])
pygame.mixer_music.set_volume(0.5)
screen = TELA
pygame.display.set_caption("Insper Saga: A Vida Não Tá Fácil")
RUNNING3 = 3 
pygame.mixer.music.play(loops=-1)

def fase2(window):
    clock = pygame.time.Clock()
    clock.tick(FPS)
    state = None
    running = True
    window = screen
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                state = QUIT
            if event.type == pygame.KEYDOWN:
                running = False
                state = RUNNING3
        window.fill(RED)
        pygame.display.flip()
    return state

fase2(screen)