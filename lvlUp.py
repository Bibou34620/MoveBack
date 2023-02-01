import pygame
import random
from variables import *

class LvlUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.lvlUp = pygame.image.load("images/lvlUp.png")
        
        self.lvlUpRect = self.lvlUp.get_rect()
        
        self.randomPosition = random.randint(0, 62)
        
        
    def spawnRandomBullets(self):
        if self.randomPosition == 0 and isLvlUpCollided == False:
            self.lvlUpRect.x = 5 - 4
            self.lvlUpRect.y = 5 - 2

        elif self.randomPosition == 1 and isLvlUpCollided == False:
            self.lvlUpRect.x = 63 - 4
            self.lvlUpRect.y = 5 - 2

        elif self.randomPosition == 2 and isLvlUpCollided == False:
            self.lvlUpRect.x = 121 - 4
            self.lvlUpRect.y = 5 - 2

        elif self.randomPosition == 3 and isLvlUpCollided == False:
            self.lvlUpRect.x = 179 - 4
            self.lvlUpRect.y = 5 - 2

        elif self.randomPosition == 4 and isLvlUpCollided == False:
            self.lvlUpRect.x = 234 - 4
            self.lvlUpRect.y = 5 - 2

        elif self.randomPosition == 5 and isLvlUpCollided == False:
            self.lvlUpRect.x = 290 - 4
            self.lvlUpRect.y = 5 - 2

        elif self.randomPosition == 6 and isLvlUpCollided == False:
            self.lvlUpRect.x = 346 - 4
            self.lvlUpRect.y = 5 - 2

        elif self.randomPosition == 7 and isLvlUpCollided == False:
            self.lvlUpRect.x = 404 - 4
            self.lvlUpRect.y = 5 - 2

        elif self.randomPosition == 8 and isLvlUpCollided == False:
            self.lvlUpRect.x = 5 - 4
            self.lvlUpRect.y = 59 - 2

        elif self.randomPosition == 9 and isLvlUpCollided == False:
                self.lvlUpRect.x = 63 - 4
                self.lvlUpRect.y = 59 - 2

        elif self.randomPosition == 10 and isLvlUpCollided == False:
                self.lvlUpRect.x = 121 - 4
                self.lvlUpRect.y = 59 - 2

        elif self.randomPosition == 11 and isLvlUpCollided == False:
                self.lvlUpRect.x = 179 - 4
                self.lvlUpRect.y = 59 - 2

        elif self.randomPosition == 12 and isLvlUpCollided == False:
                self.lvlUpRect.x = 234 - 4
                self.lvlUpRect.y = 59 - 2

        elif self.randomPosition == 13 and isLvlUpCollided == False:
                self.lvlUpRect.x = 290 - 4
                self.lvlUpRect.y = 59 - 2

        elif self.randomPosition == 14 and isLvlUpCollided == False:
                self.lvlUpRect.x = 346 - 4
                self.lvlUpRect.y = 59 - 2

        elif self.randomPosition == 15 and isLvlUpCollided == False:
                self.lvlUpRect.x = 404 - 4
                self.lvlUpRect.y = 59 - 2

        elif self.randomPosition == 16 and isLvlUpCollided == False:
                self.lvlUpRect.x = 5 - 4
                self.lvlUpRect.y = 112 - 2

        elif self.randomPosition == 17 and isLvlUpCollided == False:
                self.lvlUpRect.x = 63 - 4
                self.lvlUpRect.y = 112 - 2

        elif self.randomPosition == 18 and isLvlUpCollided == False:
                self.lvlUpRect.x = 121 - 4
                self.lvlUpRect.y = 112 - 2

        elif self.randomPosition == 19 and isLvlUpCollided == False:
                self.lvlUpRect.x = 179 - 4
                self.lvlUpRect.y = 112 - 2

        elif self.randomPosition == 20 and isLvlUpCollided == False:
                self.lvlUpRect.x = 234 - 4
                self.lvlUpRect.y = 112 - 2

        elif self.randomPosition == 21 and isLvlUpCollided == False:
                self.lvlUpRect.x = 290 - 4
                self.lvlUpRect.y = 112 - 2

        elif self.randomPosition == 22 and isLvlUpCollided == False:
                self.lvlUpRect.x = 346 - 4
                self.lvlUpRect.y = 112 - 2

        elif self.randomPosition == 23 and isLvlUpCollided == False:
                self.lvlUpRect.x = 404 - 4
                self.lvlUpRect.y = 112 - 2

        elif self.randomPosition == 24 and isLvlUpCollided == False:
                self.lvlUpRect.x = 5 - 4
                self.lvlUpRect.y = 165 - 2

        elif self.randomPosition == 25 and isLvlUpCollided == False:
                self.lvlUpRect.x = 63 - 4
                self.lvlUpRect.y = 165 - 2

        elif self.randomPosition == 26 and isLvlUpCollided == False:
                self.lvlUpRect.x = 121 - 4
                self.lvlUpRect.y = 165 - 2

        elif self.randomPosition == 27 and isLvlUpCollided == False:
                self.lvlUpRect.x = 179 - 4
                self.lvlUpRect.y = 165 - 2

        elif self.randomPosition == 28 and isLvlUpCollided == False:
                self.lvlUpRect.x = 234 - 4
                self.lvlUpRect.y = 165 - 2

        elif self.randomPosition == 29 and isLvlUpCollided == False:
                self.lvlUpRect.x = 290 - 4
                self.lvlUpRect.y = 165 - 2

        elif self.randomPosition == 30 and isLvlUpCollided == False:
                self.lvlUpRect.x = 346 - 4
                self.lvlUpRect.y = 165 - 2

        elif self.randomPosition == 31 and isLvlUpCollided == False:
                self.lvlUpRect.x = 404 - 4
                self.lvlUpRect.y = 165 - 2

        elif self.randomPosition == 32 and isLvlUpCollided == False:
                self.lvlUpRect.x = 5 - 4
                self.lvlUpRect.y = 219 - 2

        elif self.randomPosition == 33 and isLvlUpCollided == False:
                self.lvlUpRect.x = 60 - 4
                self.lvlUpRect.y = 219 - 2

        elif self.randomPosition == 34 and isLvlUpCollided == False:
                self.lvlUpRect.x = 118 - 4
                self.lvlUpRect.y = 219 - 2

        elif self.randomPosition == 35 and isLvlUpCollided == False:
                self.lvlUpRect.x = 177 - 4
                self.lvlUpRect.y = 219 - 2

        elif self.randomPosition == 36 and isLvlUpCollided == False:
                self.lvlUpRect.x = 232 - 4
                self.lvlUpRect.y = 219 - 2

        elif self.randomPosition == 37 and isLvlUpCollided == False:
                self.lvlUpRect.x = 287 - 4
                self.lvlUpRect.y = 219 - 2

        elif self.randomPosition == 38 and isLvlUpCollided == False:
                self.lvlUpRect.x = 345 - 4
                self.lvlUpRect.y = 219 - 2

        elif self.randomPosition == 39 and isLvlUpCollided == False:
                self.lvlUpRect.x = 404 - 4
                self.lvlUpRect.y = 219 - 2

        elif self.randomPosition == 40 and isLvlUpCollided == False:
                self.lvlUpRect.x = 5 - 4
                self.lvlUpRect.y = 271 - 2

        elif self.randomPosition == 41 and isLvlUpCollided == False:
                self.lvlUpRect.x = 63 - 4
                self.lvlUpRect.y = 271 - 2

        elif self.randomPosition == 42 and isLvlUpCollided == False:
                self.lvlUpRect.x = 121 - 4
                self.lvlUpRect.y = 271 - 2

        elif self.randomPosition == 43 and isLvlUpCollided == False:
                self.lvlUpRect.x = 179 - 4
                self.lvlUpRect.y = 271 - 2

        elif self.randomPosition == 44 and isLvlUpCollided == False:
                self.lvlUpRect.x = 234 - 4
                self.lvlUpRect.y = 271 - 2

        elif self.randomPosition == 45 and isLvlUpCollided == False:
                self.lvlUpRect.x = 290 - 4
                self.lvlUpRect.y = 271 - 2

        elif self.randomPosition == 46 and isLvlUpCollided == False:
                self.lvlUpRect.x = 346 - 4
                self.lvlUpRect.y = 271 - 2

        elif self.randomPosition == 47 and isLvlUpCollided == False:
                self.lvlUpRect.x = 404 - 4
                self.lvlUpRect.y = 271 - 2

        elif self.randomPosition == 48 and isLvlUpCollided == False:
                self.lvlUpRect.x = 5 - 4
                self.lvlUpRect.y = 324 - 2

        elif self.randomPosition == 49 and isLvlUpCollided == False:
                self.lvlUpRect.x = 63 - 4
                self.lvlUpRect.y = 324 - 2

        elif self.randomPosition == 50 and isLvlUpCollided == False:
                self.lvlUpRect.x = 179 - 4
                self.lvlUpRect.y = 324 - 2

        elif self.randomPosition == 51 and isLvlUpCollided == False:
                self.lvlUpRect.x = 234 - 4
                self.lvlUpRect.y = 324 - 2

        elif self.randomPosition == 52 and isLvlUpCollided == False:
                self.lvlUpRect.x = 290 - 4
                self.lvlUpRect.y = 324 - 2

        elif self.randomPosition == 53 and isLvlUpCollided == False:
                self.lvlUpRect.x = 346 - 4
                self.lvlUpRect.y = 324 - 2

        elif self.randomPosition == 54 and isLvlUpCollided == False:
                self.lvlUpRect.x = 404 - 4
                self.lvlUpRect.y = 324 - 2

        elif self.randomPosition == 55 and isLvlUpCollided == False:
                self.lvlUpRect.x = 5 - 4
                self.lvlUpRect.y = 373 - 2

        elif self.randomPosition == 56 and isLvlUpCollided == False:
                self.lvlUpRect.x = 63 - 4
                self.lvlUpRect.y = 373 - 2

        elif self.randomPosition == 57 and isLvlUpCollided == False:
                self.lvlUpRect.x = 121 - 4
                self.lvlUpRect.y = 373 - 2

        elif self.randomPosition == 58 and isLvlUpCollided == False:
                self.lvlUpRect.x = 179 - 4
                self.lvlUpRect.y = 373 - 2

        elif self.randomPosition == 59 and isLvlUpCollided == False:
                self.lvlUpRect.x = 234 - 4
                self.lvlUpRect.y = 373 - 2

        elif self.randomPosition == 60 and isLvlUpCollided == False:
                self.lvlUpRect.x = 290 - 4
                self.lvlUpRect.y = 373 - 2

        elif self.randomPosition == 61 and isLvlUpCollided == False:
                self.lvlUpRect.x = 346 - 4
                self.lvlUpRect.y = 373 - 2

        elif self.randomPosition == 62 and isLvlUpCollided == False:
                self.lvlUpRect.x = 404 - 4
                self.lvlUpRect.y = 373 - 2