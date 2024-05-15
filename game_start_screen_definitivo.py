import pygame
import time
import random
from assets import musica
from configuracoes import QUIT, TELA
pygame.init()
pygame.mixer.music.load(musica['start'])
pygame.mixer.music.set_volume(0.4)
font = pygame.font.SysFont('arial', 32)
titulo = "Insper Saga: A Vida Não Tá Fácil"
txt = "Aperte qualquer botão para começar!"
# ALTURA = 400
# LARGURA = 500
tela = TELA
pygame.display.set_caption("Insper Saga: A Vida Não Tá Fácil")
pos = (170, 540)
dramatis = (200, 200) #posição do título
FPS = 60
BLACK = (0,0,0)
CONTROLES = False #se for True vai pra tela que mostra os controles do jogo
RUNNING1 = 1 #primeira fase
class Blink():
    def __init__(self, txt, titulo, font):
        self.statement = font.render(txt, True, (255,255,255))
        # self.occult = font.render(txt,True,(0,0,0))
        self.title = font.render(titulo, True, (255,255,255))
        self.called = pygame.time.get_ticks()
        self.lim = 1000
        # self.low = 123
    def update(self):
        now = pygame.time.get_ticks()
        passado = now - self.called
        tela.blit(self.title, dramatis)
        if passado >= self.lim:           
            tela.blit(self.statement, pos)
            self.called = now
        # else:
        #     tela.blit(self.occult, pos)
var = Blink(txt, titulo, font)
pygame.mixer.music.play(loops=-1)
def tela_inicio(window):
    window = TELA
    vel = pygame.time.Clock()
    running = True
    state = None
    while running:
        vel.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                state = QUIT
            if event.type == pygame.KEYDOWN:
                CONTROLES = True
                running = False
                state = RUNNING1
        window.fill(BLACK)
        var.update()
        pygame.display.flip()
        pygame.time.wait(600)
    return state
tela_inicio(tela)