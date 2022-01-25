class Settings():
    def initialize_dynamic_settings(self):
        self.screen_width = 1200
        self.screen_height =800
        self.bgcolor = (255,255,255)
        self.ship_speed_factor = 1.5
        self.ship_limit = 1
        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
    def __init__(self):
        #how quickly  the game speeds up
        self.speedup_scale =1.1

        self.score_scale = 1.5

        self.initialize_dynamic_settings()
        #fleet direction of 1 is right and -1 is left 
        self.fleet_direction = 1
        #scoring
        self.alien_points = 50
    
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points* self.score_scale)
        print(self.align_points)

    


