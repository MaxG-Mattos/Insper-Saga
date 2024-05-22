import pygame
menu_inicial = 'Assets_em_questao\\Touhou15_5_LunaticEyesInvisibleFullMoon(ReisenUdongeinInaba).ogg'
primeira_fase = 'Assets_em_questao\\MoFStage2Theme_RoadoftheApotropaicGod_DarkRoad.ogg'
segunda_fase = 'Assets_em_questao\\ULiLMokousTheme_ReachfortheMoon_ImmortalSmoke.ogg'
terceira_fase = 'Assets_em_questao\\DivetoEmergency.ogg'
quarta_fase = 'Assets_em_questao\\LoLK_Junkos_Theme_Pure Furies_Whereabouts_of_theHeart'
fase_final = 'Assets_em_questao\\GoldenNocturne.ogg'
imagem_jogador_a = pygame.image.load('Assets_em_questao\\jogador.png')
imagem_inimigo_a = pygame.image.load('Assets_em_questao\\jogador.png')
imagem_tiro_base_a = pygame.image.load('Assets_em_questao\\New Piskel.png')
imagem_tiro_servidor_a = pygame.image.load('Assets_em_questao\\tiro_servidor.png')
vidas = pygame.image.load('Assets_em_questao\\vida.png')
perca_boss = pygame.image.load('Assets_em_questao\\VidaPerdida.png')


imagem_vida = pygame.transform.scale(vidas,(720/5,730/5))
imagem_metade = pygame.transform.scale(perca_boss,(359/5,730/5))
imagem_jogador = pygame.transform.scale(imagem_jogador_a,(32*2,32*1.5))
imagem_servidor = pygame.transform.scale(imagem_inimigo_a,(32*2,32*2))
imagem_tiro_base = pygame.transform.scale(imagem_tiro_base_a,(32/1.5,32))
imagem_tiro_servidor = pygame.transform.scale(imagem_tiro_servidor_a,(32*1.5,32*1.5))

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
imagem['tiros'] = {}
imagem['tiros']['tiro'] = imagem_tiro_base
imagem['tiros']['tiro_servidor'] = imagem_tiro_servidor
imagem['vida'] = imagem_vida
imagem['metada vida'] = imagem_metade
print(musica['boss final'])