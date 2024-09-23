import pygame, load_images, const

pygame.init()
menu = pygame.display.set_mode((const.anchow, const.altow))
pygame.display.set_caption("Main")

corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
       




    
    menu.fill((100,100,100))
    menu.blit(load_images.bg,[-10,-25])
    pygame.display.flip()

pygame.quit()
