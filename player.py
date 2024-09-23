import pygame, const

class Player():
    def __init__(self,x,y,image):
        self.image = image
        self.forma = pygame.draw.rect(0,0,const.w_player,
                                      const.h_player)
        self.forma.center = (x,y)
    
    def movement(self, delta_x, delta_y):
        self.forma.x += delta_x
        self.forma.y += delta_y