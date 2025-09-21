class Settings:
    # stores all the settings for alien invasion

    def __init__(self):
        #intialize the game settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        #alien settings
        self.alien_speed = 0.25
        self.fleet_drop_speed = 50
        # 1 means right ; -1 means left
        self.fleet_direction = 1



