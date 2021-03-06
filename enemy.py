#Enemy class by Stephan Green
#Inherits from pygame's sprite class
#Used for creating enemy objects for pygame
#8/12/2021
import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, i, size):
        super().__init__()
        self.sprite = pygame.transform.scale(pygame.image.load(i),(size,size))
        self.image = self.sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
    #simple movement. takes in x and y velocity and the sprite will move
    #accordingly in pixels. currently, y value is not required.
    def movement(self, velocity_x, velocity_y=0):
        self.rect.x += velocity_x
        self.rect.y += velocity_y
