import pygame
from pygame.locals import *
from sys import exit
#import classes as c
pygame.init()

#  === Tela Principal ===
largura = 750
altura = 750
x_jogador = 350
y_jogador = 700
x_inimigo = 350
y_inimigo = 35


tela = pygame.display.set_mode((largura,altura))

#escrita em cima da janela
pygame.display.set_caption('Space invaders')

#outra forma de controlar a velocidade do objeto(controlando a taxa de frames do jogo)
clock = pygame.time.Clock()

#      === Assets ===
# humberto = imagem do humberto, depois dar blit no while principal

#impede inimigo de sair da tela

fora_x = False
fora_y = False
# looping infinito em que o jogo passa
while True:
    #controla posicao fora da tela

    if x_jogador > largura:
        x_jogador = 10
    if x_jogador < 0:
        x_jogador = largura
    if y_jogador < 0:
        y_jogador = altura - 15
    if y_jogador > altura:
        y_jogador = 10
        
        
    #controla os frames por segundo
    clock.tick(30)
    #preenchimento da tela
    tela.fill((0,0,0))
    #cilck do jogador, nesse caso o de sair
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
  

        if event.type == pygame.KEYDOWN:
            if event.key == K_d:
                x_jogador += 50
            if event.key == K_a:
                x_jogador -= 50
            if event.key == K_w:
                y_jogador -= 50
            if event.key == K_s:
                y_jogador += 50
        

    #desenho objeto.formato(lugar do desenho,cor,(posição,largura,altura))
    
    #movimenta para baix_jogadoro, qnd chegar ao final da tela, reinicia a posição y

    humberto = pygame.draw.circle(tela,(0,0,120),(x_jogador,y_jogador),25) #(centro,raio)
    inimigo = pygame.draw.circle(tela,(255,0,0),(x_inimigo,y_inimigo),25)
    #pygame.draw.line(tela,(255,255,0),(150,55),(200,55),5) #(inicio_ponto,fim_ponto,espessura)
    #movimento inimigo
    # if not fora_x:
    #     x_inimigo += 10
    #     if x_inimigo > largura:
    #         fora_x = True
    # if fora_x:
    #     x_inimigo -= 10
    #     if x_inimigo < 0:
    #         fora_x = False

    if not fora_x and fora_y:
        x_inimigo += 10
        y_inimigo += 0
        if x_inimigo > largura-35:
            fora_x = True
            fora_y = False
    if fora_x and not fora_y:
        x_inimigo += 0
        y_inimigo += 10
        if y_inimigo > altura-400:
            fora_x = True
            fora_y = True
    if fora_x and fora_y:
        x_inimigo -= 10
        y_inimigo -= 0
        if x_inimigo < 35:
            fora_x = False
            fora_y = False
    if not fora_x and not fora_y:
        x_inimigo -= 0
        y_inimigo -= 10
        if y_inimigo < 35:
            fora_x = False
            fora_y = True

    #atualização das infos dentro do jogo
    pygame.display.update()