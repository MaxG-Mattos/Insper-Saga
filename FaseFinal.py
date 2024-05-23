import random
import pygame
import time
from assets import musica, imagem
from Classes import *
from configuracoes import FPS, BLACK, WHITE, TELA, FONT1, QUIT, INIT, RUNNING1, RED, resina

pygame.init()
pygame.mixer_music.load(musica['boss final'])
pygame.mixer_music.set_volume(0.5)
# screen = TELA
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
    bullet_enemy = pygame.sprite.Group()
    sprite_jog = pygame.sprite.Group()
    sprite_en = pygame.sprite.Group()
    jogador = Nave('jogador', all_sprites, all_bullets, imagem['sprites']['Jogador'], imagem['tiros']['tiro'])
    pelicano = Pelicano(all_sprites, bullet_enemy, imagem['sprites']['resina'], imagem['tiros']['tiro'])
    all_sprites.add(jogador)
    all_sprites.add(pelicano)
    sprite_jog.add(jogador)
    sprite_en.add(pelicano)
    VIDA_JOGADOR = v_jogador
    VIDAS_RESINA = resina
    back =  imagem['background']['3']
    pygame.mixer_music.load(musica['boss final'])
    pygame.mixer_music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)
    while running:
        if pelicano.pare <= 0 and pelicano.tempo_parada > 0:
            if pelicano.rect.y >= ALTURA - 300:
                pelicano.shoot_diaE_up()
                pelicano.shoot_dia_up()
                pelicano.shoot_normal()
                pelicano.shoot_normal_baixo()
                pelicano.shoot_diagonal_esquerda()
                pelicano.shoot_diagonal_direita()
            if pelicano.rect.x <= 200:             
                pelicano.shoot_left_down()
                pelicano.shoot_left_up()
                pelicano.shoot_dia_up()
                pelicano.shoot_diaE_up()
                pelicano.shoot_diagonal_direita()
                pelicano.shoot_diagonal_esquerda()
            if pelicano.rect.x >= LARGURA - 375:
                pelicano.shoot_right_down()
                pelicano.shoot_right_up()
                pelicano.shoot_diagonal_direita()
                pelicano.shoot_diagonal_esquerda()
                pelicano.shoot_normal_baixo()
                pelicano.shoot_dia_up()
                pelicano.shoot_diaE_up()
            if pelicano.rect.y <= 200:
                pelicano.shoot_normal()
                pelicano.shoot_normal_baixo()
                pelicano.shoot_diagonal_direita()
                pelicano.shoot_diagonal_esquerda()
                pelicano.shoot_diaE_up()
                pelicano.shoot_dia_up()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    jogador.speed_x += 4
                if event.key == pygame.K_a:
                    jogador.speed_x -= 4
                if event.key == pygame.K_s:
                    jogador.speed_y += 4
                if event.key == pygame.K_w:
                    jogador.speed_y -= 4
                if event.key == pygame.K_SPACE:
                    jogador.shoot()
                    atira = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    jogador.speed_x -= 4
                if event.key == pygame.K_a:
                    jogador.speed_x += 4
                if event.key == pygame.K_s:
                    jogador.speed_y -= 4
                if event.key == pygame.K_w:
                    jogador.speed_y += 4
                if event.key == pygame.K_SPACE:
                    atira = False
        window.fill(BLACK)
        all_sprites.update()
        window.blit(back, (0, 0))
        all_sprites.draw(window)  
        if pygame.sprite.groupcollide(bullet_enemy,sprite_jog,True,False):
            VIDA_JOGADOR -= 1
        if pygame.sprite.groupcollide(all_bullets,sprite_en,True,False):
            VIDAS_RESINA -= 1

        if VIDAS_RESINA == 10:
            window.blit(imagem['vida'],(0,0))
            window.blit(imagem['vida'],(70,0))
            window.blit(imagem['vida'],(140,0))
            window.blit(imagem['vida'],(210,0))
            window.blit(imagem['vida'],(280,0))
        if VIDAS_RESINA == 9:
            window.blit(imagem['vida'],(0,0))
            window.blit(imagem['vida'],(70,0))
            window.blit(imagem['vida'],(140,0))
            window.blit(imagem['vida'],(210,0))
            window.blit(imagem['metade vida'],(280,0))
        if VIDAS_RESINA == 8:
            window.blit(imagem['vida'],(0,0))
            window.blit(imagem['vida'],(70,0))
            window.blit(imagem['vida'],(140,0))
            window.blit(imagem['vida'],(210,0))
        if VIDAS_RESINA == 7:
            window.blit(imagem['vida'],(0,0))
            window.blit(imagem['vida'],(70,0))
            window.blit(imagem['vida'],(140,0))
            window.blit(imagem['metade vida'],(210,0))
        if VIDAS_RESINA == 6:
            window.blit(imagem['vida'],(0,0))
            window.blit(imagem['vida'],(70,0))
            window.blit(imagem['vida'],(140,0))
        if VIDAS_RESINA == 5:
            window.blit(imagem['vida'],(0,0))
            window.blit(imagem['vida'],(70,0))
            window.blit(imagem['metade vida'],(140,0))
        if VIDAS_RESINA == 4:
            window.blit(imagem['vida'],(0,0))
            window.blit(imagem['vida'],(70,0))
        if VIDAS_RESINA == 3:
            window.blit(imagem['vida'],(0,0))
            window.blit(imagem['metade vida'],(70,0))
        if VIDAS_RESINA == 2:
            window.blit(imagem['vida'],(0,0))
        if VIDAS_RESINA == 1:
            window.blit(imagem['metade vida'],(0,0))
        if VIDA_JOGADOR == 1:
            window.blit(imagem['vida'],(0,ALTURA-70))
        if VIDA_JOGADOR == 2:
            window.blit(imagem['vida'],(0,ALTURA-70))
            window.blit(imagem['vida'],(70,ALTURA-70))
        if VIDA_JOGADOR == 3:
            window.blit(imagem['vida'],(0,ALTURA-70))
            window.blit(imagem['vida'],(70,ALTURA-70))
            window.blit(imagem['vida'],(140,ALTURA-70))

        if VIDAS_RESINA == 0 or VIDA_JOGADOR == 0:
            running = False
            state = INIT       
        pygame.display.flip()
    # jogador.speed_x = 0
    # jogador.speed_y = 0 
    return state

 