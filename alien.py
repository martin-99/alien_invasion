import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,ai_game):
        """ Initialize the alien and set its starting location"""
        super().__init__()
        self.screen = ai_game.screen

        #Loading the image and getting its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Create each new alien at the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 

        #Storing the exact horizontal position of the alien
        self.x = float(self.rect.x)
        