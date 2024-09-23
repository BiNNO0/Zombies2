import pygame, const, load_images


pygame.init()
menu = pygame.display.set_mode((const.anchow, const.altow))
pygame.display.set_caption("Main")

corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                corriendo = False
                pygame.quit()
                pygame.time.delay(2000)
                exec(open("game.py").read())
                    



    
    menu.fill((100,100,100))
    menu.blit(load_images.menu,[-10,-25])
    pygame.display.flip()


pygame.quit()
