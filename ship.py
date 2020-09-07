import pygame
class Ship:
    """Class that represents the ship object"""
    def __init__(self,ai_game):
        """Intializing the ship and set its starting positions"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #Start each new ship from the middle bottom of the screen
        self.rect.midbottom= self.screen_rect.midbottom
    def blitme(self):
        self.screen.blit(self.image,self.rect)

