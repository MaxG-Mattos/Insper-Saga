import random
import pygame
import time
from assets import musica, imagem
# from Classes import Nave, Bullet
from Classes import Nave, Bullet, Vidas, Servidor
from configuracoes import FPS, BLACK, WHITE, TELA, FONT1, QUIT, INIT, RUNNING1, v_jogador, servidor

pygame.init()
pygame.mixer_music.load(musica['primeira fase'])
pygame.mixer_music.set_volume(0.5)
screen = TELA
pygame.display.set_caption("Insper Saga: A Vida Não Tá Fácil")
RUNNING2 = 2 #se for verdade vai pra fase 2
pygame.mixer.music.play(loops=-1)


def fase1(window):
    clock = pygame.time.Clock()
    clock.tick(FPS)
    state = None
    running = True
    window = screen
    all_sprites = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    jogador = Nave('jogador',all_sprites,all_bullets,imagem['sprites']['jogador'],imagem['tiros']['tiro'])
    inimigo = Servidor(all_sprites,all_bullets,imagem['sprites']['servidor'],imagem['tiros']['tiro_servidor'])
    # for i in range(v_jogador):
    #     lifes = Vidas(v_jogador, all_sprites, 'jogador', imagem['vida'], imagem['metade vida'])
    #     all_sprites.add(lifes)
    # for k in range(servidor):
    #     ini_lifes = Vidas(servidor, all_sprites, 'inimigo', imagem['vida'], imagem['metade vida'])
    #     all_sprites.add(ini_lifes)
    all_sprites.add(jogador)
    all_sprites.add(inimigo)
    atira = False
    timer_shoot_servidor = 550
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                state = QUIT
            #se o evento for precionar a tecla
            if event.type == pygame.KEYDOWN:
                #se a tecla for 'D'
                if event.key == pygame.K_d:
                    #jogador move para direita
                    jogador.speed_x = 2
                #se a tecla for 'A'
                if event.key == pygame.K_a:
                    #jogador move para esquerda
                    jogador.speed_x = -2
                #se a tecla for 'W'
                if event.key == pygame.K_w:
                    #jogador move para cima
                    jogador.speed_y = -2
                #se a tecla for 'S'
                if event.key == pygame.K_s:
                    #jogador move para baixo
                    jogador.speed_y = 2
                #se a tecla for 'SPAÇO'
                if event.key == pygame.K_SPACE:
                    #jogador atira
                    jogador.shoot()
                    atira = True

            # se o evento for 'soltar a tecla'
            if event.type == pygame.KEYUP:
                #se a tecla for D
                if event.key == pygame.K_d:
                    #para o movimento da direita
                    jogador.speed_x = 0
                #se a tecla for A
                if event.key == pygame.K_a:
                    #para o movimento da esquerda
                    jogador.speed_x = 0
                #se a tecla for W
                if event.key == pygame.K_w:
                    #para o movimento para cima
                    jogador.speed_y = 0
                #se a tecla for S
                if event.key == pygame.K_s:
                    #para o movimento para baixo
                    jogador.speed_y = 0
                if event.key == pygame.K_SPACE:
                    atira = False
            
        if atira:
            jogador.shoot()
        if timer_shoot_servidor == 0:
            inimigo.shoot()
            timer_shoot_servidor = 550
        else:
            timer_shoot_servidor -= 1
            # if event.type == pygame.KEYDOWN:
            #     running = False
            #     state = RUNNING2

        window.fill(WHITE)
        all_sprites.update()
        all_sprites.draw(window)
        pygame.display.flip()
    return state

fase1(screen)
