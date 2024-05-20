import pygame
from pygame.locals import *
from sys import exit
from assets import * 
from configuracoes import ALTURA,LARGURA
#inicia o jogo
# pygame.init()
# #  === Classes ===

# #classe nave como sprite
class Nave(pygame.sprite.Sprite):
    #inicia construção da classe
    def __init__(self,lado,todas_sprites,todos_tiros,image,imagem_tiro):
        #inicializa a sprite
        pygame.sprite.Sprite.__init__(self)
        #definie a imagem da sprite
        self.image = image
        #define a hitbox da nave
        self.hitbox = pygame.mask.from_surface(self.image)
        #define a nave como um retangulo para o computador, para possibilitar movimento
        self.rect = self.hitbox.get_rect()
        #qual lado do mapa ele se encontra (inimigo ou jogador)
        self.estado = lado
        #movimento no eixo x
        self.speed_x = 0
        #movimento no eixo y
        self.speed_y = 0
        #define a imagem do tiro
        self.imagem_tiro = imagem_tiro
        #recebe o grupo de todas as sprites
        self.all_sprites = todas_sprites
        #recebe o grupo de todos os tiros
        self.all_bullets = todos_tiros
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500 
        if self.estado == 'jogador':
            self.rect.x = 600
            self.rect.y = 300
        else:
            self.rect.x = 200
            self.rect.y = 100
            self.speed_x = 20
        #função de ações da Nave
    def update(self):
        #movimento no eixo x
        self.rect.x += self.speed_x
        #movimento no eixo y
        self.rect.y += self.speed_y
        if self.estado == 'inimigo':
            if self.rect.x > LARGURA-75:
                self.speed_x = 0 
                self.speed_y = 10
            if self.rect.y > ALTURA -475:
                self.speed_x = -10 
                self.speed_y = 0
            if self.rect.x < 25 and self.rect.y > ALTURA -475:
                self.speed_x = 0 
                self.speed_y = -10
            if self.rect.x < 25 and self.rect.y < 25:
                self.speed_x = 10
                self.speed_y = 0
    #função atirar
    def shoot(self):
        if self.estado == 'jogador':
            now = pygame.time.get_ticks()
            elapsed_ticks = now - self.last_shot
            if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
                self.last_shot = now
        #cria uma sprite (tiro) ['atirar']
                tiro = Bullet('jogador',self.imagem_tiro,self.rect.x+65,self.rect.y+75)
            #adiciona o tiro no grupo todas_as_sprites, necessario para a vizualização do tiro 
                self.all_sprites.add(tiro)
            #adiciona o tiro no grupo todos os tiros, necessario para a vizualização do tiro 
                self.all_bullets.add(tiro)
        else:
            # Verifica se pode atirar
            noww = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
            elapsed_ticks = noww - self.last_shot
            if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
                self.last_shot = noww
                tiro = Bullet('inimigo',self.imagem_tiro,self.rect.x+65,self.rect.y+75)
                #adiciona o tiro no grupo todas_as_sprites, necessario para a vizualização do tiro 
                self.all_sprites.add(tiro)
                #adiciona o tiro no grupo todos os tiros, necessario para a vizualização do tiro 
                self.all_bullets.add(tiro)
#classe Bullet como sprite
class Bullet(pygame.sprite.Sprite):
    #inicia a construção da nave
    def __init__(self,lado,image,x,y):
        #inicializa a sprite
        pygame.sprite.Sprite.__init__(self)
        #define a imagem do tiro
        self.image = image
        #define a hitbox do tiro
        self.hitbox = pygame.mask.from_surface(self.image)
        #define o tiro como um retangulo para o computador, para possibilitar movimento
        self.rect = self.hitbox.get_rect()
        #define o lado de partida do tiro (inimigo ou jogador)
        self.rect.center = (x,y)
        self.estado = lado
        if self.estado == 'jogador':
        #velocidade tiro
            self.speedy = -10
        else: 
            self.speedy = 10
    #funcao que define as ações do tiro
    def update(self):
        #movimenta o tiro no eixo y
        self.rect.y += self.speedy
        #se o tiro passar da tela
        if self.rect.y < 0:
            #auto destruição do tiro
            self.kill()

# #carregando a imagem do jogador sem dimensao
# imagem_jogador_adimensionada = pygame.image.load("C:/Users/rafae/Desktop/Dessoft/.pygame/pygame/assets/jogador.png")
# #carregando a imagem do tiro sem dimensao
# imagem_tiro_adimensionada = pygame.image.load("C:/Users/rafae/Desktop/Dessoft/.pygame/pygame/assets/New Piskel.png")
# #carregando a imagem do jogador ja dimensionada
# imagem_jogador = pygame.transform.scale(imagem_jogador_adimensionada,(32*2,32*1.5))
# #carregando a imagem do jogador ja dimensionada
# imagem_tiro = pygame.transform.scale(imagem_tiro_adimensionada,(32/1.5,32))

# Assets = [imagem_jogador,imagem_tiro]

# #  === Tela Principal ===

# LARGURA = 750
# ALTURA = 750


# #cria o grupo para todas as sprites
# todas_sprites = pygame.sprite.Group()
# #cria o grupo dos tiros
# todos_tiros = pygame.sprite.Group()

# inimigos = pygame.sprite.Group()

# jogador_grupo = pygame.sprite.Group()
# #cria a nave do jogador
# jogador = Nave('jogador',todas_sprites,todos_tiros,Assets[0],Assets[1])
# #cria a nave do inimigo
# inimigo = Nave('inimigo',todas_sprites,todos_tiros,Assets[0],Assets[1])
# bala = Bullet('jogador',imagem_tiro,50,50)
# #adiciona a sprite do jogador ao grupo de todas as sprites
# todas_sprites.add(jogador)
# todas_sprites.add(bala)
# todas_sprites.add(inimigo)
# jogador_grupo.add(jogador)
# inimigos.add(inimigo)
# #cria fonte para texto (tamanho  negrito italico)
# fonte = pygame.font.SysFont('arial',40,True,False)

# #cria a tela
# tela = pygame.display.set_mode((LARGURA,ALTURA))

# #escrita em cima da janela
# pygame.display.set_caption('Space invaders')

# #controla a taxa de frames do jogo
# clock = pygame.time.Clock()

# #bloco do codigo antigo:
# #{
# #impede inimigo de sair da tela
# # fora_x = False
# # fora_y = False
# #}

# atira = False
# # looping infinito em que o jogo passa
# while True:
  
#     #controla os frames por segundo
#     clock.tick(30)

#     #preenchimento da tela
#     tela.fill((0,100,100))
#     if atira:
#         jogador.shoot()
#     #verifica acontecimento de eventos
#     for event in pygame.event.get():
#         #se o evento for clickar para sair
#         if event.type == QUIT:
#             #saí do pygame
#             pygame.quit()
#             #fecha o terminal
#             exit()
  
#         #se o evento for precionar a tecla
#         if event.type == pygame.KEYDOWN:
#             #se a tecla for 'D'
#             if event.key == K_d:
#                 #jogador move para direita
#                 jogador.speed_x += 20
#             #se a tecla for 'A'
#             if event.key == K_a:
#                 #jogador move para esquerda
#                 jogador.speed_x -= 20
#             #se a tecla for 'W'
#             if event.key == K_w:
#                 #jogador move para cima
#                 jogador.speed_y -= 20
#             #se a tecla for 'S'
#             if event.key == K_s:
#                 #jogador move para baixo
#                 jogador.speed_y += 20
#             #se a tecla for 'SPAÇO'
#             if event.key == K_SPACE:
#                 #jogador atira
#                 jogador.shoot()
#                 atira = True

#         # se o evento for 'soltar a tecla'
#         if event.type == pygame.KEYUP:
#             #se a tecla for D
#             if event.key == K_d:
#                 #para o movimento da direita
#                 jogador.speed_x = 0
#             #se a tecla for A
#             if event.key == K_a:
#                 #para o movimento da esquerda
#                 jogador.speed_x = 0
#             #se a tecla for W
#             if event.key == K_w:
#                 #para o movimento para cima
#                 jogador.speed_y = 0
#             #se a tecla for S
#             if event.key == K_s:
#                 #para o movimento para baixo
#                 jogador.speed_y = 0
#             if event.key == K_SPACE:
#                 atira = False
        
#         if atira:
#             jogador.shoot()


#     inimigo.shoot()               
#     #atualiza o estado do grupo 'todas as sprites'
#     todas_sprites.update()
#     # "imprime" na tela o jogador (imagem dele e seu retangulo, para possibilitar movimento)
#     #tela.blit(jogador.image,jogador.rect)
#     #tela.blit(bala.image,bala.rect)
#     todas_sprites.draw(tela)
#     #pedaço do codigo antigo:
# #{

#     #desenho objeto.formato(lugar do desenho,cor,(posição,LARGURA,ALTURA))
    
#     #movimenta para baix_jogadoro, qnd chegar ao final da tela, reinicia a posição y
    
#     # if not fora_x and fora_y:
#     #     x_inimigo += 10
#     #     y_inimigo += 0
#     #     if x_inimigo > LARGURA-35:
#     #         fora_x = True
#     #         fora_y = False
#     # if fora_x and not fora_y:
#     #     x_inimigo += 0
#     #     y_inimigo += 10
#     #     if y_inimigo > ALTURA-400:
#     #         fora_x = True
#     #         fora_y = True
#     # if fora_x and fora_y:
#     #     x_inimigo -= 10
#     #     y_inimigo -= 0
#     #     if x_inimigo < 35:
#     #         fora_x = False
#     #         fora_y = False
#     # if not fora_x and not fora_y:
#     #     x_inimigo -= 0
#     #     y_inimigo -= 10
#     #     if y_inimigo < 35:
#     #         fora_x = False
#     #         fora_y = True
   
   
#     if pygame.sprite.spritecollide(inimigo,todos_tiros,False):
#                             #texto  antiserrilhado cor
#         texto = fonte.render('BOOM',False,(255,0,0))
#         tela.blit(texto,(10,10))
    
# #}


#     #atualização das infos dentro do jogo
#     pygame.display.flip()