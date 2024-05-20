inimigo.shoot()               
    #atualiza o estado do grupo 'todas as sprites'
    todas_sprites.update()
    # "imprime" na tela o jogador (imagem dele e seu retangulo, para possibilitar movimento)
    #tela.blit(jogador.image,jogador.rect)
    #tela.blit(bala.image,bala.rect)
    todas_sprites.draw(tela)
     if pygame.sprite.spritecollide(inimigo,todos_tiros,False):
                            #texto  antiserrilhado cor
        texto = fonte.render('BOOM',False,(255,0,0))
        tela.blit(texto,(10,10))
    
#}


    #atualização das infos dentro do jogo
    pygame.display.flip()