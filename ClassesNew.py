import pygame

class BulletBase(pygame.sprite.Sprite):
    def _init_(self, image, x, y, speedx=0, speedy=-5, lifetime=750):
        super()._init_()
        self.image = image
        self.hitbox = pygame.mask.from_surface(self.image)
        self.rect = self.hitbox.get_rect(center=(x, y))
        self.speedx = speedx
        self.speedy = speedy
        self.lifetime = lifetime
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.y < 0 or self.rect.y > self.lifetime or self.rect.x < 0 or self.rect.x > self.lifetime:
            self.kill()

class Bullet(BulletBase):
    def _init_(self, lado, image, x, y):
        speed = -5 if lado == 'jogador' else 5
        super()._init_(image, x, y, speedy=speed)

class BulletDiagonal(BulletBase):
    def _init_(self, image, x, y, speedx, speedy):
        super()._init_(image, x, y, speedx, speedy)

class BulletPelDia(BulletDiagonal):
    def _init_(self, image, x, y):
        super()._init_(image, x, y, speedx=1, speedy=-1)

class BulletPelDiaE(BulletDiagonal):
    def _init_(self, image, x, y):
        super()._init_(image, x, y, speedx=-2, speedy=1)

class BulletPelDiaUP(BulletDiagonal):
    def _init_(self, image, x, y):
        super()._init_(image, x, y, speedx=1, speedy=-1)

class BulletPelDiaUPE(BulletDiagonal):
    def _init_(self, image, x, y):
        super()._init_(image, x, y, speedx=-1, speedy=-1)