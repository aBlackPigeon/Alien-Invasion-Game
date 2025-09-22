class Settings:
    # stores all the settings for alien invasion

    def __init__(self):
        #intialize the game settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_limit = 3

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        #alien settings
        self.fleet_drop_speed = 50
        
        #how quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        #initialize settings that change throghout the game
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # 1 means right ; -1 means left
        self.fleet_direction = 1

    def increase_speed(self):
        #increase speed settings
        self.ship_speed *= self.speedup_scale()
        self.bullet_speed *= self.speedup_scale()
        self.alien_speed *= self.speedup_scale()
    
    




