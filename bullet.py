import pygame
import random
from variables import *
from instantiate import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.bullet = pygame.image.load("images/bullets.png")
        
        self.bulletRect = self.bullet.get_rect()
        
        self.randomPosition = random.randint(0, 62)
        
        self.x = self.bulletRect.x
        
        self.y = self.bulletRect.y
        
        

    def spawnRandomBullets(self):
        if self.randomPosition == 0 and isBullet1Collided == False:
            self.bulletRect.x = 5
            self.bulletRect.y = 5

        elif self.randomPosition == 1 and isBullet1Collided == False:
            self.bulletRect.x = 63
            self.bulletRect.y = 5

        elif self.randomPosition == 2 and isBullet1Collided == False:
            self.bulletRect.x = 121
            self.bulletRect.y = 5

        elif self.randomPosition == 3 and isBullet1Collided == False:
            self.bulletRect.x = 179
            self.bulletRect.y = 5

        elif self.randomPosition == 4 and isBullet1Collided == False:
            self.bulletRect.x = 234
            self.bulletRect.y = 5

        elif self.randomPosition == 5 and isBullet1Collided == False:
            self.bulletRect.x = 290
            self.bulletRect.y = 5

        elif self.randomPosition == 6 and isBullet1Collided == False:
            self.bulletRect.x = 346
            self.bulletRect.y = 5

        elif self.randomPosition == 7 and isBullet1Collided == False:
            self.bulletRect.x = 404
            self.bulletRect.y = 5

        elif self.randomPosition == 8 and isBullet1Collided == False:
            self.bulletRect.x = 5
            self.bulletRect.y = 59

        elif self.randomPosition == 9 and isBullet1Collided == False:
                self.bulletRect.x = 63
                self.bulletRect.y = 59

        elif self.randomPosition == 10 and isBullet1Collided == False:
                self.bulletRect.x = 121
                self.bulletRect.y = 59

        elif self.randomPosition == 11 and isBullet1Collided == False:
                self.bulletRect.x = 179
                self.bulletRect.y = 59

        elif self.randomPosition == 12 and isBullet1Collided == False:
                self.bulletRect.x = 234
                self.bulletRect.y = 59

        elif self.randomPosition == 13 and isBullet1Collided == False:
                self.bulletRect.x = 290
                self.bulletRect.y = 59

        elif self.randomPosition == 14 and isBullet1Collided == False:
                self.bulletRect.x = 346
                self.bulletRect.y = 59

        elif self.randomPosition == 15 and isBullet1Collided == False:
                self.bulletRect.x = 404
                self.bulletRect.y = 59

        elif self.randomPosition == 16 and isBullet1Collided == False:
                self.bulletRect.x = 5
                self.bulletRect.y = 112

        elif self.randomPosition == 17 and isBullet1Collided == False:
                self.bulletRect.x = 63
                self.bulletRect.y = 112

        elif self.randomPosition == 18 and isBullet1Collided == False:
                self.bulletRect.x = 121
                self.bulletRect.y = 112

        elif self.randomPosition == 19 and isBullet1Collided == False:
                self.bulletRect.x = 179
                self.bulletRect.y = 112

        elif self.randomPosition == 20 and isBullet1Collided == False:
                self.bulletRect.x = 234
                self.bulletRect.y = 112

        elif self.randomPosition == 21 and isBullet1Collided == False:
                self.bulletRect.x = 290
                self.bulletRect.y = 112

        elif self.randomPosition == 22 and isBullet1Collided == False:
                self.bulletRect.x = 346
                self.bulletRect.y = 112

        elif self.randomPosition == 23 and isBullet1Collided == False:
                self.bulletRect.x = 404
                self.bulletRect.y = 112

        elif self.randomPosition == 24 and isBullet1Collided == False:
                self.bulletRect.x = 5
                self.bulletRect.y = 165

        elif self.randomPosition == 25 and isBullet1Collided == False:
                self.bulletRect.x = 63
                self.bulletRect.y = 165

        elif self.randomPosition == 26 and isBullet1Collided == False:
                self.bulletRect.x = 121
                self.bulletRect.y = 165

        elif self.randomPosition == 27 and isBullet1Collided == False:
                self.bulletRect.x = 179
                self.bulletRect.y = 165

        elif self.randomPosition == 28 and isBullet1Collided == False:
                self.bulletRect.x = 234
                self.bulletRect.y = 165

        elif self.randomPosition == 29 and isBullet1Collided == False:
                self.bulletRect.x = 290
                self.bulletRect.y = 165

        elif self.randomPosition == 30 and isBullet1Collided == False:
                self.bulletRect.x = 346
                self.bulletRect.y = 165

        elif self.randomPosition == 31 and isBullet1Collided == False:
                self.bulletRect.x = 404
                self.bulletRect.y = 165

        elif self.randomPosition == 32 and isBullet1Collided == False:
                self.bulletRect.x = 5
                self.bulletRect.y = 219

        elif self.randomPosition == 33 and isBullet1Collided == False:
                self.bulletRect.x = 60
                self.bulletRect.y = 219

        elif self.randomPosition == 34 and isBullet1Collided == False:
                self.bulletRect.x = 118
                self.bulletRect.y = 219

        elif self.randomPosition == 35 and isBullet1Collided == False:
                self.bulletRect.x = 177
                self.bulletRect.y = 219

        elif self.randomPosition == 36 and isBullet1Collided == False:
                self.bulletRect.x = 232
                self.bulletRect.y = 219

        elif self.randomPosition == 37 and isBullet1Collided == False:
                self.bulletRect.x = 287
                self.bulletRect.y = 219

        elif self.randomPosition == 38 and isBullet1Collided == False:
                self.bulletRect.x = 345
                self.bulletRect.y = 219

        elif self.randomPosition == 39 and isBullet1Collided == False:
                self.bulletRect.x = 404
                self.bulletRect.y = 219

        elif self.randomPosition == 40 and isBullet1Collided == False:
                self.bulletRect.x = 5
                self.bulletRect.y = 271

        elif self.randomPosition == 41 and isBullet1Collided == False:
                self.bulletRect.x = 63
                self.bulletRect.y = 271

        elif self.randomPosition == 42 and isBullet1Collided == False:
                self.bulletRect.x = 121
                self.bulletRect.y = 271

        elif self.randomPosition == 43 and isBullet1Collided == False:
                self.bulletRect.x = 179
                self.bulletRect.y = 271

        elif self.randomPosition == 44 and isBullet1Collided == False:
                self.bulletRect.x = 234
                self.bulletRect.y = 271

        elif self.randomPosition == 45 and isBullet1Collided == False:
                self.bulletRect.x = 290
                self.bulletRect.y = 271

        elif self.randomPosition == 46 and isBullet1Collided == False:
                self.bulletRect.x = 346
                self.bulletRect.y = 271

        elif self.randomPosition == 47 and isBullet1Collided == False:
                self.bulletRect.x = 404
                self.bulletRect.y = 271

        elif self.randomPosition == 48 and isBullet1Collided == False:
                self.bulletRect.x = 5
                self.bulletRect.y = 324

        elif self.randomPosition == 49 and isBullet1Collided == False:
                self.bulletRect.x = 63
                self.bulletRect.y = 324

        elif self.randomPosition == 50 and isBullet1Collided == False:
                self.bulletRect.x = 179
                self.bulletRect.y = 324

        elif self.randomPosition == 51 and isBullet1Collided == False:
                self.bulletRect.x = 234
                self.bulletRect.y = 324

        elif self.randomPosition == 52 and isBullet1Collided == False:
                self.bulletRect.x = 290
                self.bulletRect.y = 324

        elif self.randomPosition == 53 and isBullet1Collided == False:
                self.bulletRect.x = 346
                self.bulletRect.y = 324

        elif self.randomPosition == 54 and isBullet1Collided == False:
                self.bulletRect.x = 404
                self.bulletRect.y = 324

        elif self.randomPosition == 55 and isBullet1Collided == False:
                self.bulletRect.x = 5
                self.bulletRect.y = 373

        elif self.randomPosition == 56 and isBullet1Collided == False:
                self.bulletRect.x = 63
                self.bulletRect.y = 373

        elif self.randomPosition == 57 and isBullet1Collided == False:
                self.bulletRect.x = 121
                self.bulletRect.y = 373

        elif self.randomPosition == 58 and isBullet1Collided == False:
                self.bulletRect.x = 179
                self.bulletRect.y = 373

        elif self.randomPosition == 59 and isBullet1Collided == False:
                self.bulletRect.x = 234
                self.bulletRect.y = 373

        elif self.randomPosition == 60 and isBullet1Collided == False:
                self.bulletRect.x = 290
                self.bulletRect.y = 373

        elif self.randomPosition == 61 and isBullet1Collided == False:
                self.bulletRect.x = 346
                self.bulletRect.y = 373

        elif self.randomPosition == 62 and isBullet1Collided == False:
                self.bulletRect.x = 404
                self.bulletRect.y = 373
                

    