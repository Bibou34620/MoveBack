import pygame

class PlayButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.playButton = pygame.image.load("images/playButton.png")
        
        self.playButtonRect = self.playButton.get_rect()