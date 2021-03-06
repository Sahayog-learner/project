import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.image = pygame.image.load('images/air_ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)    
        #movement of flags
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """update the ship position based on movement flags"""
        #update the  ship's center value, not the rect 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and  self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor
        #update rect object from self.center
        self.rect.centerx = self.center
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def center_ship(self):
        """center the ship on the screen"""
        self.center = self.screen_rect.centerx