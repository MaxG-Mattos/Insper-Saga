import pygame
class Nave(pygame.sprite.Sprite):
    #inicia construção da classe
    def _init_(self,lado,todas_sprites,todos_tiros,image,imagem_tiro):
        #inicializa a sprite
        pygame.sprite.Sprite._init_(self)
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
            if self.rect.x > largura-75:
                self.speed_x = 0 
                self.speed_y = 10
            if self.rect.y > altura -475:
                self.speed_x = -10 
                self.speed_y = 0
            if self.rect.x < 25 and self.rect.y > altura -475:
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
    def _init_(self,lado,image,x,y):
        #inicializa a sprite
        pygame.sprite.Sprite._init_(self)
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