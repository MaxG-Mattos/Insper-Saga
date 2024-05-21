import pygame
menu_inicial = 'Assets_em_questao\\Touhou15_5_LunaticEyesInvisibleFullMoon(ReisenUdongeinInaba).ogg'
primeira_fase = 'Assets_em_questao\\MoFStage2Theme_RoadoftheApotropaicGod_DarkRoad.ogg'
segunda_fase = 'Assets_em_questao\\ULiLMokousTheme_ReachfortheMoon_ImmortalSmoke.ogg'
terceira_fase = 'Assets_em_questao\\DivetoEmergency.ogg'
quarta_fase = 'Assets_em_questao\\LoLK_Junkos_Theme_Pure Furies_Whereabouts_of_theHeart'
fase_final = 'Assets_em_questao\\GoldenNocturne.ogg'

musica = {}
imagens = {}
musica['start'] = menu_inicial
musica['primeira fase'] = primeira_fase
musica['segunda fase'] = segunda_fase
musica['terceira fase'] = terceira_fase
musica['quarta fase'] = quarta_fase
musica['boss final'] = fase_final

jogador = pygame.image.load('Assets_em_questao\\jogador.png')
new_piskel = pygame.image.load('Assets_em_questao\\NewPiskel.png')
imagens['jogador'] = pygame.transform.scale(jogador, (32*2,32*1.5))
imagens['new piskel'] = pygame.transform.scale(new_piskel, (32*2,32*1.5))