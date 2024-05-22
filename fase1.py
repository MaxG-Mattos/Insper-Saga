import random
import pygame
import time
from assets import musica, imagem
# from Classes import Nave, Bullet
from Classes import Nave, Bullet, Servidor
from configuracoes import FPS, BLACK, WHITE, TELA, FONT1, QUIT, INIT, RUNNING1, v_jogador, servidor,tam_servidor, ALTURA,scale

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
    bullet_enemy = pygame.sprite.Group()
    sprite_jog = pygame.sprite.Group()
    sprite_en = pygame.sprite.Group()
    jogador = Nave('jogador',all_sprites,all_bullets,imagem['sprites']['Jogador'],imagem['tiros']['tiro'])
    inimigo = Servidor(all_sprites,bullet_enemy,imagem['sprites']['servidor'],imagem['tiros']['tiro_servidor'])
    # for i in range(v_jogador):
    #     lifes = Vidas(v_jogador, all_sprites, 'jogador', imagem['vida'], imagem['metade vida'])
    #     all_sprites.add(lifes)
    # for k in range(servidor):
    #     ini_lifes = Vidas(servidor, all_sprites, 'inimigo', imagem['vida'], imagem['metade vida'])
    #     all_sprites.add(ini_lifes)
    all_sprites.add(jogador)
    all_sprites.add(inimigo)
    sprite_jog.add(jogador)
    sprite_en.add(inimigo)
    atira = False
    timer_shoot_servidor = 550//scale
    timer_special = 5000//scale
    duracao_f5 = 5000//scale
    timer_espera_f5 = True
    contagem_espera = 15000//scale
    f5 = False
    VIDA_JOGADOR = v_jogador*22
    VIDA_SERVIDOR = servidor
    back =  imagem['background']['1']
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
                    jogador.speed_x = 3
                #se a tecla for 'A'
                if event.key == pygame.K_a:
                    #jogador move para esquerda
                    jogador.speed_x = -3
                #se a tecla for 'W'
                if event.key == pygame.K_w:
                    #jogador move para cima
                    jogador.speed_y = -3
                #se a tecla for 'S'
                if event.key == pygame.K_s:
                    #jogador move para baixo
                    jogador.speed_y = 3
                #se a tecla for 'SPAÇO'
                if f5 == False:
                    if event.key == pygame.K_SPACE:
                    #jogador atira
                        jogador.shoot()
                        atira = True
                else:
                    if event.key == pygame.K_F5 and pygame.K_SPACE:
                        jogador.shoot()

            # se o evento for 'soltar a tecla'
            if event.type == pygame.KEYUP:
                #se a tecla for D
                if event.key == pygame.K_d:
                    jogador.speed_x -= 3
                if event.key == pygame.K_a:
                    jogador.speed_x += 3
                if event.key == pygame.K_s:
                    jogador.speed_y -= 3
                if event.key == pygame.K_w:
                    jogador.speed_y += 3
                if event.key == pygame.K_SPACE:
                    if f5 == False:
                        atira = False
                    else:
                        if event.key == pygame.K_F5:
                            atira = False
            
        if atira:
            jogador.shoot()
        if timer_shoot_servidor == 0:
            inimigo.shoot()
            timer_shoot_servidor = 550//scale
        else:
            timer_shoot_servidor -= 1
        if timer_special == 0:
            inimigo.special_shoot()
            timer_special = 5000//scale
        else:
            timer_special -= 1
            # if event.type == pygame.KEYDOWN:
            #     running = False
            #     state = RUNNING2
        if f5:
            duracao_f5 -= 1
            print(duracao_f5)
        if duracao_f5 == 0:
            f5 = False
            duracao_f5 = 5000//scale
            timer_espera_f5 = True

        if timer_espera_f5:
            contagem_espera -= 1
        if contagem_espera == 0:
            f5 = True
            contagem_espera = 15000//scale
        window.fill(BLACK)
        window.blit(back, (50, 50))
        all_sprites.update()
        all_sprites.draw(window)
        if pygame.sprite.groupcollide(bullet_enemy,sprite_jog,False,False):
            VIDA_JOGADOR -= 1
            print(VIDA_JOGADOR)
        if pygame.sprite.groupcollide(all_bullets,sprite_en,False,False):
            VIDA_SERVIDOR -= 1
        if pygame.sprite.collide_mask(jogador,inimigo):
            VIDA_JOGADOR -= 1
            print(VIDA_JOGADOR)
            VIDA_SERVIDOR -= 1
        if VIDA_SERVIDOR == 0:
            return RUNNING2
        if VIDA_JOGADOR == 0:
            state = INIT
        if VIDA_SERVIDOR == 120:
            window.blit(imagem['vida'],(0,0))
            window.blit(imagem['vida'],(70,0))
            window.blit(imagem['vida'],(140,0))
        if VIDA_SERVIDOR >= 100 and VIDA_SERVIDOR < 120:
            window.blit(imagem['vida'],(0,0))
            window.blit(imagem['vida'],(70,0))
            window.blit(imagem['metade vida'],(140,0))
        if VIDA_SERVIDOR >= 80 and VIDA_SERVIDOR < 100:
            window.blit(imagem['vida'],(0,0))
            window.blit(imagem['vida'],(70,0))
        if VIDA_SERVIDOR >= 60 and VIDA_SERVIDOR < 80:
            window.blit(imagem['vida'],(0,0))
            window.blit(imagem['metade vida'],(70,0))
        if VIDA_SERVIDOR >= 40 and VIDA_SERVIDOR < 60:
            window.blit(imagem['vida'],(0,0))
        if VIDA_SERVIDOR >= 20 and VIDA_SERVIDOR < 40:
            window.blit(imagem['metade vida'],(0,0))
        if VIDA_JOGADOR < 2*22 and VIDA_JOGADOR > 0:
            window.blit(imagem['vida'],(0,ALTURA-70))
        if VIDA_JOGADOR < v_jogador*22 and VIDA_JOGADOR >= 2*22:
            window.blit(imagem['vida'],(0,ALTURA-70))
            window.blit(imagem['vida'],(70,ALTURA-70))
        if VIDA_JOGADOR == v_jogador*22:
            window.blit(imagem['vida'],(0,ALTURA-70))
            window.blit(imagem['vida'],(70,ALTURA-70))
            window.blit(imagem['vida'],(140,ALTURA-70))
        pygame.display.flip()
    return state

print(fase1(screen))