import pygame 
trocar = 0
largura = 0
altura = 0
# clase jogador
class Humberto(pygame.sprite.Sprite): #torna a classe visivel
    def __init__(self, group, assets): 
        pygame.sprite.Sprite.__init__(self)
        self.image = trocar # def imagem Humberto / trocar = asset['imagem da nave']
        self.mask = pygame.mask.from_surface(self.image) #define a hitbox como a superficie da nave
        self.rect = self.image.get_rect()
        self.rect.centerx = trocar #trocar = posição da nave em x
        self.rect.bottom  = trocar #trocar = posição da quina superior esquerda da nave
        self.speedx = 0 #velocidade inicial da nave
        self.groups = group #seta o grupo da nave
        self.assest = assets #assets da nave

        self.last_shot = pygame.time.get_ticks() #seta q vai ter um delay para o prox tiro
        self.shoot_ticks = 500 #delay de 500 ms

    def update(self):
        # Atualização da posição do Humberto
        self.rect.x += self.speedx

        #mantem na tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0
    
    def shoot(self):
        
        # seta os ticks no momento
        now = pygame.time.get_ticks()
        
        #verifica qnts ticks se passaram desde o ultimo tiro
        elapsed_tick = now - self.last_shot

        #se da pra atirar: 
        if elapsed_tick > self.shoot_ticks:
            #salva o tick no momento
            self.last_shot = now
            #Criação da nova bala()
            new_bullet = Bullet(self.assets, self.rect.top,self.rect.centerx)
            #salvando a bala como entidade
            self.groups['all_sprites'].add(new_bullet)
            #salvando a bala com um tipo de bala
            self.groups['all_bullets'].add(new_bullet)
            #som do disparo
            self.assets['som_tiro'].play()
#define a classe do inimigo
class Inimigo(pygame.sprite.sprite):
    #constroi a classe
    def __init__(self,group,assets):
        #inimigo visivel no jogo
        pygame.sprite.Sprite.__init__(self)
        #seta a iamgem do inimigo
        self.image = trocar
        #seta a hitbox
        self.mask = pygame.mask.from_surface(self.image)
        #seta o inimigo como um retangulo, mantendo a hitbox
        self.rect = self.image.get_rect()
        #posicao inimigo em x
        self.rect.x = largura/2
        #posicao inimigo em y
        self.rect.y = altura 
        #velocidade em x
        self.speedx = 0
        #velocidade em y
        self.speedy = 0
        #define os assets como do inigmo
        self.assets = assets
    #update de informacoes dentro da classe
    def update(self):
        #se o inimigo estiver dentro do mapa
        dentro = True #possivel erro: o update pode reiniciar o dentro como True toda vez q for acionado. possivel solução: colocar na inicialização o dentro = True
        #se o inimigo estiver dentro do mapa
        if self.rect.x < largura:
            dentro = True
        else:
            dentro = False
        if dentro:
            #movimenta para direita
            self.rect.x += self.speedx
            #nao movimenta em y
            self.rect.y += 0
        #
        if not dentro:
            #movimenta para esquerda
            self.rect.x -= self.speedx
            #nao movimenta em y
            self.rect.y + 0
#define a classe Bala
class Bullet(pygame.sprite.Sprite):
    #inicia a construcao da classe
    def __init__(self,assets,bottom,centerx):
        #seta a imagem da bala
        self.image = trocar
        #seta a hitbox da bala
        self.maks = pygame.mask.from_surface(self.image)
        #seta a bala como um retangulo, mantendo a hitbox
        self.rect = self.image.get_rect()

        #define a posicao centrao da bala em x
        self.rect.centerx = centerx
        #define a posicao do canto inferior esquerdo da bala
        self.rect.bottom = bottom
        #velocidade da bala
        self.speedy = -10

    #atualização de informacoes dentro da classe
    def update(self):
        #movimento no eixo y
        self.rect.y += self.speedy

        #se a bala atingir um canto do mapa
        if self.rect.bottom <0:
            #deleta a bala
            self.kill()