import pygame
from assets import imagem
pygame.font.init()
LARGURA = 750
ALTURA = 750
TELA = pygame.display.set_mode((LARGURA, ALTURA))
FPS = 45
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,51,51)
FONT1 = pygame.font.SysFont('arial', 32)
QUIT = 0
INIT = -1
RUNNING1 = 1
RUNNING2 = 2 
RUNNING5 = 5
#vidas na prática
servidor = 120 #cada hit é -1
v_jogador = 3
leticia = 10
crianca = 80
bia = 60
resina = 10

#tamanhos sprites
tam_servidor = 64
scale = 5
