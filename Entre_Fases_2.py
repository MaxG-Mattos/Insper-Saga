import pygame
import time
import random
from assets import musica
from configuracoes import QUIT, TELA, RUNNING2
pygame.init()
font = pygame.font.SysFont('arial', 30)
titulo = "O servidor já caiu, só falta dar problema com Ninja agora..."
txt = "Aperte espaço quando estiver pronto"
# ALTURA = 400
# LARGURA = 500
# tela = TELA
pygame.display.set_caption("Insper Saga: A Vida Não Tá Fácil")
pos = (165, 540)
dramatis = (55, 200) #posição do título
FPS = 60
BLACK = (0,0,0)
class Blink():
    def __init__(self, txt, titulo, font):
        self.statement = font.render(txt, True, (255,255,255))
        # self.occult = font.render(txt,True,(0,0,0))
        self.title = font.render(titulo, True, (255,255,255))
        self.called = pygame.time.get_ticks()
        self.lim = 1000
        # self.low = 123
    def update(self, window):
        tela = window
        now = pygame.time.get_ticks()
        passado = now - self.called
        tela.blit(self.title, dramatis)
        if passado >= self.lim:           
            tela.blit(self.statement, pos)
            self.called = now
        # else:
        #     tela.blit(self.occult, pos)
var = Blink(txt, titulo, font)
def ninja_time(window):
    window = window
    vel = pygame.time.Clock()
    running = True
    state = None
    pygame.mixer.music.load(musica['terceira fase'])
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    while running:
        vel.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                state = QUIT
                return state
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    state = RUNNING2
                    return state
        window.fill(BLACK)
        var.update(window)
        pygame.display.flip()
        pygame.time.wait(600)
    return state
# tela_inicio(tela)