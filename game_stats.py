class GameStats():
    """track for alien invasion"""
    def __init__(self,ai_settings):
        """initialize the status"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #start game in inactive status
        self.game_active = False

    def reset_stats(self):
        """initialize statics that can change during the game"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
