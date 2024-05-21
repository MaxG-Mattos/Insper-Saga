import random
import pygame
import time
from assets import musica, imagens
from Classes import *
from configuracoes import FPS, BLACK, WHITE, TELA, FONT1, QUIT, INIT, RUNNING1, RED

pygame.init()
pygame.mixer_music.load(musica['boss final'])
pygame.mixer_music.set_volume(0.5)
screen = TELA
pygame.display.set_caption("Insper Saga: A Vida Não Tá Fácil")
RUNNING5 = 5 
pygame.mixer.music.play(loops=-1)

def faseFinal(window):
    clock = pygame.time.Clock()
    clock.tick(FPS)
    state = None
    running = True
    window = window
    atira = False
    all_sprites = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    jogador = Nave('jogador', all_sprites, all_bullets, imagens['jogador'], imagens['new piskel'])
    pelicano = Pelicano(all_sprites, all_bullets, imagens['jogador'], imagens['new piskel'])
    all_sprites.add(jogador)
    all_sprites.add(pelicano)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    jogador.speed_x += 1
                if event.key == pygame.K_a:
                    jogador.speed_x -= 1
                if event.key == pygame.K_s:
                    jogador.speed_y += 1
                if event.key == pygame.K_w:
                    jogador.speed_y -= 1
                if event.key == pygame.K_SPACE:
                    jogador.shoot()
                    atira = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    jogador.speed_x -= 1
                if event.key == pygame.K_a:
                    jogador.speed_x += 1
                if event.key == pygame.K_s:
                    jogador.speed_y -= 1
                if event.key == pygame.K_w:
                    jogador.speed_y += 1
                if event.key == pygame.K_SPACE:
                    atira = False
        window.fill(RED)
        all_sprites.update()
        all_sprites.draw(window)           
        pygame.display.flip()
    return state

faseFinal(screen)