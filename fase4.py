import random
import pygame
import time
from assets import musica, imagens
from classes import *
from configuracoes import FPS, BLACK, WHITE, TELA, FONT1, QUIT, INIT, RUNNING1, RED, RUNNING4

pygame.init()
pygame.mixer_music.load(musica['quarta fase'])
pygame.mixer_music.set_volume(0.5)
screen = TELA
pygame.display.set_caption("Insper Saga: A Vida Não Tá Fácil")
RUNNING5 = 5 
pygame.mixer.music.play(loops=-1)

def fase4(window):
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
                state = RUNNING5
        window.fill(WHITE)
        pygame.display.flip()
    return state

fase4(screen)