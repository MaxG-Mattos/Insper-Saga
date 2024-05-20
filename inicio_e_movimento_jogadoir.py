import pygame
while True:
  
    #controla os frames por segundo
    clock.tick(30)

    #preenchimento da tela
    tela.fill((0,100,100))
    if atira:
        jogador.shoot()
    #verifica acontecimento de eventos
    for event in pygame.event.get():
        #se o evento for clickar para sair
        if event.type == QUIT:
            #saí do pygame
            pygame.quit()
            #fecha o terminal
            exit()
  
        #se o evento for precionar a tecla
        if event.type == pygame.KEYDOWN:
            #se a tecla for 'D'
            if event.key == K_d:
                #jogador move para direita
                jogador.speed_x += 20
            #se a tecla for 'A'
            if event.key == K_a:
                #jogador move para esquerda
                jogador.speed_x -= 20
            #se a tecla for 'W'
            if event.key == K_w:
                #jogador move para cima
                jogador.speed_y -= 20
            #se a tecla for 'S'
            if event.key == K_s:
                #jogador move para baixo
                jogador.speed_y += 20
            #se a tecla for 'SPAÇO'
            if event.key == K_SPACE:
                #jogador atira
                jogador.shoot()
                atira = True

        # se o evento for 'soltar a tecla'
        if event.type == pygame.KEYUP:
            #se a tecla for D
            if event.key == K_d:
                #para o movimento da direita
                jogador.speed_x = 0
            #se a tecla for A
            if event.key == K_a:
                #para o movimento da esquerda
                jogador.speed_x = 0
            #se a tecla for W
            if event.key == K_w:
                #para o movimento para cima
                jogador.speed_y = 0
            #se a tecla for S
            if event.key == K_s:
                #para o movimento para baixo
                jogador.speed_y = 0
            if event.key == K_SPACE:
                atira = False
        
        if atira:
            jogador.shoot()