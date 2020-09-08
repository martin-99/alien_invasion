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

         #Getting instance of game settings
        self.settings = ai_game.settings

        #Start each new ship from the middle bottom of the screen
        self.rect.midbottom= self.screen_rect.midbottom

        self.x = float(self.rect.x)
       

        #Moving flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        #Update ship's position based on the moving flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x
    def blitme(self):
        self.screen.blit(self.image,self.rect)

