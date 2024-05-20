#carregando a imagem do jogador sem dimensao
imagem_jogador_adimensionada = pygame.image.load("C:/Users/rafae/Desktop/Dessoft/.pygame/pygame/assets/jogador.png")
#carregando a imagem do tiro sem dimensao
imagem_tiro_adimensionada = pygame.image.load("C:/Users/rafae/Desktop/Dessoft/.pygame/pygame/assets/New Piskel.png")
#carregando a imagem do jogador ja dimensionada
imagem_jogador = pygame.transform.scale(imagem_jogador_adimensionada,(32*2,32*1.5))
#carregando a imagem do jogador ja dimensionada
imagem_tiro = pygame.transform.scale(imagem_tiro_adimensionada,(32/1.5,32))

Assets = [imagem_jogador,imagem_tiro]

#  === Tela Principal ===

largura = 750
altura = 750


#cria o grupo para todas as sprites
todas_sprites = pygame.sprite.Group()
#cria o grupo dos tiros
todos_tiros = pygame.sprite.Group()

inimigos = pygame.sprite.Group()

jogador_grupo = pygame.sprite.Group()
#cria a nave do jogador
jogador = Nave('jogador',todas_sprites,todos_tiros,Assets[0],Assets[1])
#cria a nave do inimigo
inimigo = Nave('inimigo',todas_sprites,todos_tiros,Assets[0],Assets[1])
bala = Bullet('jogador',imagem_tiro,50,50)
#adiciona a sprite do jogador ao grupo de todas as sprites
todas_sprites.add(jogador)
todas_sprites.add(bala)
todas_sprites.add(inimigo)
jogador_grupo.add(jogador)
inimigos.add(inimigo)
#cria fonte para texto (tamanho  negrito italico)
fonte = pygame.font.SysFont('arial',40,True,False)

#cria a tela
tela = pygame.display.set_mode((largura,altura))

#escrita em cima da janela
pygame.display.set_caption('Space invaders')

#controla a taxa de frames do jogo
clock = pygame.time.Clock()

#bloco do codigo antigo:
#{
#impede inimigo de sair da tela
# fora_x = False
# fora_y = False
#}

atira = False
# looping infinito em que o jogo passa