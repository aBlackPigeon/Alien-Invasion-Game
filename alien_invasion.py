import sys

import pygame
from settings import Settings

class AlienInvasion:
    # It will contain all the main attributes and behaviour

    def __init__(self):
        pygame.init() # intializing the pygame setting
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height)) #creates tuple of height & width
        pygame.display.set_caption("Alien Invasion")

    
    def  run_game(self):
        #running main loop of the game
        while True:
            # any mouse and keyboard activity
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw screen during each pass
            self.screen.fill(self.settings.bg_color)
            
            pygame.display.flip() # refreshes for any change in event

if __name__ == '__main__':
    # making game instance and running it
    ai = AlienInvasion()
    ai.run_game()

