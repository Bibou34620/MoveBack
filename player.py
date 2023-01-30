import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_forward = pygame.image.load("images/player_high.png")
        self.player_left = pygame.image.load("images/player_left.png")
        self.player_back = pygame.image.load("images/player_back.png")
        self.player_right = pygame.image.load("images/player_right.png")
        
        self.actualPlayerRenderer = self.player_forward
        
        self.playerRect = self.actualPlayerRenderer.get_rect()
        
        