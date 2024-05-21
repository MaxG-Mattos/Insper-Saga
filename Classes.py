import pygame
from pygame.locals import *
from sys import exit
from assets import * 
from configuracoes import ALTURA,LARGURA, v_jogador, crianca, servidor, bia, leticia
#inicia o jogo
# pygame.init()
# #  === Classes ===

# #classe nave como sprite
class Nave(pygame.sprite.Sprite):
    #inicia construção da classe
    def __init__(self,lado ,todas_sprites,todos_tiros,image,imagem_tiro):
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
            # self.lives = 3
        else:
            self.rect.x = 200
            self.rect.y = 100
            self.speed_x = 1

        #função de ações da Nave
    def update(self):
        #movimento no eixo x
        self.rect.x += self.speed_x
        #movimento no eixo y
        self.rect.y += self.speed_y
        if self.estado == 'jogador':
            if self.rect.right > LARGURA:
                self.rect.right = LARGURA
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.bottom > ALTURA:
                self.rect.bottom = ALTURA
            if self.rect.top < 0:
                self.rect.top = 0
        if self.estado == 'inimigo':
            if self.rect.x > LARGURA-75:
                self.speed_x = 0 
                self.speed_y = 1
            if self.rect.y > ALTURA -475:
                self.speed_x = -1
                self.speed_y = 0
            if self.rect.x < 25 and self.rect.y > ALTURA -475:
                self.speed_x = 0 
                self.speed_y = -1
            if self.rect.x < 25 and self.rect.y < 25:
                self.speed_x = 1
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
    # def lives_update(self):
    #     s

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
# class Vidas(pygame.sprite.Sprite):
#     def __init__(self, ind, group, lado):
#         pygame.sprite.Sprite.__init__(self)
#         self.groups = group
#         self.image = imagens['vida']
#         self.lives = ind
#         self.id = lado
#         self.rect = self.image.get_rect()
#         if self.id == 'jogador':
#             self.rect.x = 10
#             self.rect.y = ALTURA-20
#         else:
#             self.rect.x = LARGURA - 10
#             self.rect.y = 20
#     def update(self):
#         if self.id != 'jogador' and self.lives != bia:
#             if self.lives%2 != 0:
#                 self.image = imagens['vida boss']


class BulletLeticia1(pygame.sprite.Sprite):
    #inicia a construção da nave
    def __init__(self,image,x,y):
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
        self.tempo_h = 300
        self.tempo_v = 100
        self.speedy = 2
        self.speedx = 1
    #funcao que define as ações do tiro
    def update(self):
        if self.tempo_h > 0:
            #movimenta o tiro no eixo y
            # indo pro lado da tela
            self.rect.x += self.speedx
            #se o tiro passar da tela
            if self.rect.y < 0:
                #auto destruição do tiro
                self.kill()
            if self.rect.x > LARGURA or self.rect.x < 0:
                self.kill()
            self.tempo_h -= 1
        if self.tempo_h <= 0 and self.tempo_v > 0:
            self.rect.y += self.speedy
            self.rect.x += self.speedx
            if self.rect.y < 0:
                self.kill()
            if self.rect.x > LARGURA or self.rect.x < 0:
                self.kill()
            self.tempo_v -= 1
        if self.tempo_h <= 0 and self.tempo_v <= 0:
            self.rect.y += self.speedy
            self.rect.x += -self.speedx
            if self.rect.y < 0:
                self.kill()
            if self.rect.x > LARGURA or self.rect.x < 0:
                self.kill()

class BulletLeticiaL(pygame.sprite.Sprite):
    #inicia a construção da nave
    def __init__(self,image,x,y):
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
        self.tempo_h = 300
        self.tempo_v = 100
        self.speedy = 2
        self.speedx = -1
    #funcao que define as ações do tiro
    def update(self):
        if self.tempo_h > 0:
            #movimenta o tiro no eixo y
            # indo pro lado da tela
            self.rect.x += self.speedx
            #se o tiro passar da tela
            if self.rect.y < 0:
                #auto destruição do tiro
                self.kill()
            if self.rect.x > LARGURA or self.rect.x < 0:
                self.kill()
            self.tempo_h -= 1
        if self.tempo_h <= 0 and self.tempo_v > 0:
            self.rect.y += self.speedy
            self.rect.x += -self.speedx
            if self.rect.y < 0:
                self.kill()
            if self.rect.x > LARGURA or self.rect.x < 0:
                self.kill()
            self.tempo_v -= 1
        if self.tempo_h <= 0 and self.tempo_v <= 0:
            self.rect.y += self.speedy
            self.rect.x += self.speedx
            if self.rect.y < 0:
                self.kill()
            if self.rect.x > LARGURA or self.rect.x < 0:
                self.kill()

class Nave_Leticia(pygame.sprite.Sprite):
    #inicia construção da classe
    def __init__(self,todas_sprites,todos_tiros,image,imagem_tiro):
        #inicializa a sprite
        pygame.sprite.Sprite.__init__(self)
        #definie a imagem da sprite
        self.image = image
        #define a hitbox da nave
        self.hitbox = pygame.mask.from_surface(self.image)
        #define a nave como um retangulo para o computador, para possibilitar movimento
        self.rect = self.hitbox.get_rect()
        #qual lado do mapa ele se encontra (inimigo ou jogador)
        #movimento no eixo x
        # self.speed_x = 0
        #movimento no eixo y
        # self.speed_y = 0
        #define a imagem do tiro
        self.imagem_tiro = imagem_tiro
        #recebe o grupo de todas as sprites
        self.all_sprites = todas_sprites
        #recebe o grupo de todos os tiros
        self.all_bullets = todos_tiros
        self.last_shot = pygame.time.get_ticks()
        self.last_left_shot = pygame.time.get_ticks()
        self.last_move = pygame.time.get_ticks() #tempo desde o ultimo movimento
        self.pare = 3000
        self.tempo_parada = 5000
        self.shoot_ticks = 700 #tempo pro tiro
#posição
        self.rect.x = 200
        self.rect.y = 100
        self.speed_x = 1
        self.speed_y = 1
        #função de ações da Nave
    def update(self):
        if self.pare > 0:
            self.pare -= 1
            self.rect.x += self.speed_x
            #movimento no eixo y
            self.rect.y += self.speed_y
            if self.rect.x > LARGURA-75:
                self.speed_x = 0 
                self.speed_y = 1
            if self.rect.y > ALTURA -475:
                self.speed_x = -1
                self.speed_y = 0
            if self.rect.x < 25 and self.rect.y > ALTURA -475:
                self.speed_x = 0 
                self.speed_y = -1
            if self.rect.x < 25 and self.rect.y < 25:
                self.speed_x = 1
                self.speed_y = 0
        if self.pare <= 0 and self.tempo_parada > 0:
            self.rect.x += 0
            self.rect.y += 0
            self.tempo_parada -= 1
        if self.pare <= 0 and self.tempo_parada <= 0:
            self.pare = 3000
            self.tempo_parada = 5000
            self.rect.x += self.speed_x
            #movimento no eixo y
            self.rect.y += self.speed_y
            if self.rect.x > LARGURA-75:
                self.speed_x = 0 
                self.speed_y = 1
            if self.rect.y > ALTURA -475:
                self.speed_x = -1
                self.speed_y = 0
            if self.rect.x < 25 and self.rect.y > ALTURA -475:
                self.speed_x = 0 
                self.speed_y = -1
            if self.rect.x < 25 and self.rect.y < 25:
                self.speed_x = 1
                self.speed_y = 0            
    def shoot(self):
         # Verifica se pode atirar
        noww = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = noww - self.last_shot
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = noww
            tiro = BulletLeticia1(self.imagem_tiro,self.rect.x+65,self.rect.y+75)
                #adiciona o tiro no grupo todas_as_sprites, necessario para a vizualização do tiro 
            self.all_sprites.add(tiro)
                #adiciona o tiro no grupo todos os tiros, necessario para a vizualização do tiro 
            self.all_bullets.add(tiro)
    def shoot_left(self):
         # Verifica se pode atirar
        agora = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = agora - self.last_left_shot
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_left_shot = agora
            tiroL = BulletLeticiaL(self.imagem_tiro,self.rect.x+65,self.rect.y+75)
                #adiciona o tiro no grupo todas_as_sprites, necessario para a vizualização do tiro 
            self.all_sprites.add(tiroL)
                #adiciona o tiro no grupo todos os tiros, necessario para a vizualização do tiro 
            self.all_bullets.add(tiroL)        