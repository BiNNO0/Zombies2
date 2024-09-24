import pygame, const, math
from load_images import *

pygame.init()
game = pygame.display.set_mode((const.anchow, const.altow))
pygame.display.set_caption("Main")

#set vars
life = 3







running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    
    key = pygame.key.get_pressed()
    
    rect_player = idle.get_rect(center=(240, 180))  
    
    player_x, player_y = rect_player.center
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    angulo = math.degrees(math.atan2(mouse_y - player_y, mouse_x - player_x))
    
    imagen_rotada = pygame.transform.rotate(idle, -angulo)
    
    rect_imagen_rotada = imagen_rotada.get_rect(center=rect_player.center)
    


    
    game.fill((100,100,100))
    game.blit(bg,[-10,-25])
    game.blit(imagen_rotada, rect_imagen_rotada.topleft)
    pygame.display.flip()

pygame.quit()
