import random
import pygame
import time
from assets import musica, imagem
from Classes import *
from configuracoes import FPS, BLACK, WHITE, TELA, FONT1, QUIT, INIT, RUNNING1, RED, leticia, v_jogador

pygame.init()
pygame.mixer_music.load(musica['segunda fase'])
pygame.mixer_music.set_volume(0.5)
screen = TELA
pygame.display.set_caption("Insper Saga: A Vida Não Tá Fácil")
RUNNING3 = 3 
pygame.mixer.music.play(loops=-1)

def fase2(window):
    clock = pygame.time.Clock()
    clock.tick(0)
    all_sprites = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    jogador = Nave('jogador', all_sprites, all_bullets, imagem['sprites']['Jogador'], imagem['tiros']['tiro'])
    inimigo = Nave_Leticia(all_sprites, all_bullets, imagem['sprites']['leticia'], imagem['tiros']['tiro'])
    all_sprites.add(jogador)
    all_sprites.add(inimigo)
    state = None
    running = True
    atira = False
    VIDAS_JOGADOR = v_jogador
    VIDAS_LETICIA = leticia
    window = screen
    back = imagem['background']['2']
    while running:
        if atira:
            jogador.shoot()
        if inimigo.pare <= 0 and inimigo.tempo_parada > 0:
            # inimigo.shoot()
            # inimigo.shoot_left()
            if inimigo.rect.left <= 200:
                inimigo.shoot_left_down()
                inimigo.shoot_right_up()
                inimigo.shoot_left()
                inimigo.shoot_dia_up()
                inimigo.shoot_diaE_up()
                inimigo.Nshot()
            if inimigo.rect.right >= 500:
                inimigo.shoot_right_down()
                inimigo.shoot_left_up()
                inimigo.shoot_left()
                inimigo.shoot_dia_up()
                inimigo.shoot_diaE_up()
                inimigo.Nshot()
            else:
                inimigo.shoot()
                inimigo.Nshot()
                inimigo.shoot_left()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    jogador.speed_x += 5
                if event.key == pygame.K_a:
                    jogador.speed_x -= 5
                if event.key == pygame.K_s:
                    jogador.speed_y += 5
                if event.key == pygame.K_w:
                    jogador.speed_y -= 5
                if event.key == pygame.K_SPACE:
                    jogador.shoot()
                    atira = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    jogador.speed_x -= 5
                if event.key == pygame.K_a:
                    jogador.speed_x += 5
                if event.key == pygame.K_s:
                    jogador.speed_y -= 5
                if event.key == pygame.K_w:
                    jogador.speed_y += 5
                if event.key == pygame.K_SPACE:
                    atira = False
                # running = False -->condição passagem de fase
                # state = RUNNING3
        if atira:
            jogador.shoot()
        # if inimigo.pare <= 0 and inimigo.tempo_parada > 0:
        #     # inimigo.shoot()
        #     # inimigo.shoot_left()
        #     if inimigo.rect.left <= 200:
        #         inimigo.shoot_left_up()
        #         inimigo.shoot_left_down()
        #         inimigo.shoot_left()
        #         inimigo.Nshot()
        #     if inimigo.rect.right >= 500:
        #         inimigo.shoot_right_up()
        #         inimigo.shoot_right_down()
        #         inimigo.shoot_left()
        #         inimigo.Nshot()
        #     else:
        #         inimigo.shoot()
        #         inimigo.shoot_left()
        window.fill(BLACK)
        all_sprites.update()
        window.blit(back, (70, 120))
        # all_sprites.update()
        all_sprites.draw(window)      
        pygame.display.flip()
    return state

fase2(screen)

