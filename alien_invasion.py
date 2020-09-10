import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (0,0),pygame.FULLSCREEN
        )
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        
      
    def run_game(self):
        """Start the main loop of the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_alien()
            self._update_screen()
           
    def _check_events(self):
        """Respond to mouse and keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                

    def _check_keydown_events(self,event):
        """Respond to keypresess."""
        if event.key ==pygame.K_RIGHT:
                    self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        
        
    
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    
    def _fire_bullet(self):
        if len(self.bullets) <self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        #Update bullet 
        self.bullets.update()

        #Remove the bullets that have dissapiared from the screen
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

    def _create_alien(self,alien_number,row_number):
            """Create alien and place it in the row"""
            alien = Alien(self)
            alien_width,alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width *alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien_height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)
    
    def _update_alien(self):
        self._check_flee_edges()
        self.aliens.update()


    def _check_flee_edges(self):
        """Respond if any alien has reach the edge """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_flee_diraction()
                break
    def _change_flee_diraction(self):
        """Drop the entire flee and change the direction """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.flee_drop_speed
        self.settings.fleet_direction*=-1
    def _create_fleet(self):
        """ Create fleet of aliens """

        #Instance of new Alien()
        alien = Alien(self)
        self.aliens.add(alien)

        alien_width,alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens_x = available_space_x // (2 * alien_width)

        #Determine the number of rows of aliens that fit into the screen

        ship_height =self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        #Create the first row of aliens
        for row_number in range(number_rows+1):
            for alien_number in range(number_of_aliens_x+2):
                self._create_alien(alien_number,row_number )
       

    def _update_screen(self):
        """on every change update the screen"""
        self.screen.fill(self.settings.bg_color)
        #Drawing the ship
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)
        """ Make the most recently drawn screen visible"""
        pygame.display.flip()



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai =AlienInvasion()
    ai.run_game()
