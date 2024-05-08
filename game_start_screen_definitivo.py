import pygame
import time
import random
from assets import musica
pygame.init()
pygame.mixer.music.load(musica['start'])
pygame.mixer.music.set_volume(0.4)
font = pygame.font.SysFont('arial', 32)
txt = "Aperte qualquer botão para começar!"
ALTURA = 400
LARGURA = 500
tela = pygame.display.set_mode((LARGURA, ALTURA))
pos = (LARGURA-460, ALTURA-200)
FPS = 60
BLACK = (0,0,0)
class Blink():
    def __init__(self, txt, font):
        self.statement = font.render(txt, True, (255,255,255))
        self.occult = font.render(txt,True,(0,0,0))
        self.called = pygame.time.get_ticks()
        self.lim = 1000
        # self.low = 123
    def update(self):
        now = pygame.time.get_ticks()
        passado = now - self.called
        if passado >= self.lim:           
            tela.blit(self.statement, pos)
            self.called = now
        # else:
        #     tela.blit(self.occult, pos)
var = Blink(txt, font)
pygame.mixer.music.play(loops=-1)
def tela_inicio():
    vel = pygame.time.Clock()
    running = True
    while running:
        vel.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                running = False
        tela.fill(BLACK)
        var.update()
        pygame.display.flip()
        pygame.time.wait(600)
tela_inicio()