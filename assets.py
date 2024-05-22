import pygame
menu_inicial = 'Assets_em_questao\\Touhou15_5_LunaticEyesInvisibleFullMoon(ReisenUdongeinInaba).ogg'
primeira_fase = 'Assets_em_questao\\MoFStage2Theme_RoadoftheApotropaicGod_DarkRoad.ogg'
segunda_fase = 'Assets_em_questao\\ULiLMokousTheme_ReachfortheMoon_ImmortalSmoke.ogg'
terceira_fase = 'Assets_em_questao\\DivetoEmergency.ogg'
quarta_fase = 'Assets_em_questao\\LoLK_Junkos_Theme_Pure Furies_Whereabouts_of_theHeart'
fase_final = 'Assets_em_questao\\GoldenNocturne.ogg'
imagem_jogador_a = pygame.image.load('Assets_em_questao\\jogador.png')
imagem_inimigo_a = pygame.image.load('Assets_em_questao\\servidor_assets.jpg')
imagem_tiro_base_a = pygame.image.load('Assets_em_questao\\New Piskel.png')
imagem_tiro_servidor_a = pygame.image.load('Assets_em_questao\\tiro_servidor.png')
vidas = pygame.image.load('Assets_em_questao\\vida.jpg')
perca_boss = pygame.image.load('Assets_em_questao\\VidaPerdida.jpg')
img_jogador_oficial = pygame.image.load('Assets_em_questao\\Humberto.png')
img_inimigo_2 = pygame.image.load('Assets_em_questao\\Leticia.png')
inimig_final = pygame.image.load('Assets_em_questao\\Resina.png')
background1 = pygame.image.load('Assets_em_questao\\sala dos professores.png')
background2 = pygame.image.load('Assets_em_questao\\Sala de Aula.png')


imagem_vida = pygame.transform.scale(vidas,(720/10,730/10))
imagem_metade = pygame.transform.scale(perca_boss,(359/10,730/10))
imagem_jogador = pygame.transform.scale(imagem_jogador_a,(32*2,32*1.5))
imagem_servidor = pygame.transform.scale(imagem_inimigo_a,(32*2,32*2))
imagem_tiro_base = pygame.transform.scale(imagem_tiro_base_a,(32/1.5,32))
imagem_tiro_servidor = pygame.transform.scale(imagem_tiro_servidor_a,(32*1.5,32*1.5))
imagem_jogador_oficial = pygame.transform.scale(img_jogador_oficial,(25*2.3,35*1.8))
imagem_let = pygame.transform.scale(img_inimigo_2,(30*2.2,35*1.8))
imagem_resi = pygame.transform.scale(inimig_final,(25*2.3,35*1.8))
imagem_back1 = pygame.transform.scale(background1,(801*1.1, 786*1.1))
imagem_back2 = pygame.transform.scale(background2,(762*1.1, 822*1.1))

musica = {}
musica['start'] = menu_inicial
musica['primeira fase'] = primeira_fase
musica['segunda fase'] = segunda_fase
musica['terceira fase'] = terceira_fase
musica['quarta fase'] = quarta_fase
musica['boss final'] = fase_final

imagem = {}
imagem['sprites'] = {}
imagem['sprites']['jogador'] = imagem_jogador
imagem['sprites']['servidor'] = imagem_servidor
imagem['sprites']['Jogador'] = imagem_jogador_oficial
imagem['sprites']['leticia'] = imagem_let
imagem['sprites']['resina'] = imagem_resi

imagem['tiros'] = {}
imagem['tiros']['tiro'] = imagem_tiro_base
imagem['tiros']['tiro_servidor'] = imagem_tiro_servidor
imagem['vida'] = imagem_vida
imagem['metade vida'] = imagem_metade
imagem['background'] = {}
imagem['background']['1'] = imagem_back1
imagem['background']['2'] = imagem_back2
print(musica['boss final'])