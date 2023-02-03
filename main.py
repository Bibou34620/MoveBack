import pygame
from options import Options
from instantiate import *
from variables import *
import random

pygame.init()

running = True
ui = pygame.image.load("images/mapAndUi.png")
endScreenUi = pygame.image.load("images/endScreenUi.png")

turnSound = pygame.mixer.Sound("sounds/turn.wav")
noMoves = pygame.mixer.Sound("sounds/noMoves.Wav")
walking = pygame.mixer.Sound("sounds/walking.wav")
takeBullet = pygame.mixer.Sound("sounds/takeBullet.wav")
lvlUpSound = pygame.mixer.Sound("sounds/lvlUp.wav")
statusUpdateSound = pygame.mixer.Sound("sounds/statusUpdate.wav")

uiFont = pygame.font.SysFont("Poppins-Medium.ttf", 55)
statusFont = pygame.font.SysFont("Poppins-Medium.ttf", 35)
endScoreFont = pygame.font.SysFont("Poppins-Medium.ttf", 55)
bestScoreFont = pygame.font.SysFont("Poppins-Medium.ttf", 35)

bestScoreRead = open('etc/bestScore.txt', 'r')
bestScoreWrite = open('etc/bestScore.txt', 'a')

print(bestScoreRead.read())

turnSound.set_volume(0.05)
noMoves.set_volume(0.05)
walking.set_volume(0.05)
takeBullet.set_volume(0.07)
lvlUpSound.set_volume(0.07)

moves = 5
level = 0

movesRedLevel = 0

redLvlUpLevel = 0
greenLvlUp = 0

player.playerRect.x = 15
player.playerRect.y = 5

while running:
    
    if moves > 0:
        currentStatus = "Nothing to report"
        
    if moves == 0:
        currentStatus = "        Press R"
        
    if moves < 3:
        movesRedLevel = 200
        
    else:
        movesRedLevel = 0
        
    if level > 9:
        blueLvlUpLevel = 255
        greenLvlUp = 255
        
    if isOnGame:
    
        movesRemains = uiFont.render(str(moves), True, (movesRedLevel, 0, 0))
        movesRemainsRect = movesRemains.get_rect()

        levelText = uiFont.render(str(level), True, (redLvlUpLevel, greenLvlUp, 51))
        levelTextRect = levelText.get_rect()

        status = statusFont.render(currentStatus, True, (0, 0 ,0))
        statusRect = status.get_rect()

        movesRemainsRect.x = 600
        movesRemainsRect.y = 12.5 

        levelTextRect.x = 575
        levelTextRect.y = 74

        statusRect.x = 467
        statusRect.y = 180

        op.screen.blit(ui, (0, 0))
        op.screen.blit(movesRemains, movesRemainsRect)
        op.screen.blit(levelText, levelTextRect)
        op.screen.blit(levelText, levelTextRect)
        op.screen.blit(status, statusRect)
        op.screen.blit(player.actualPlayerRenderer, (player.playerRect.x, player.playerRect.y))

        if isBullet1Collided == False:
            op.screen.blit(bullet.bullet, (bullet.bulletRect.x, bullet.bulletRect.y))

        if isBullet2Collided == False:
            op.screen.blit(secondBullet.bullet, (secondBullet.bulletRect.x, secondBullet.bulletRect.y))

        if isLvlUpCollided == False:
            op.screen.blit(lvlUp.lvlUp, (lvlUp.lvlUpRect.x, lvlUp.lvlUpRect.y))
    
    
        print(player.playerRect.x," " , player.playerRect.y)

        bullet.spawnRandomBullets()
        secondBullet.spawnRandomBullets()
        lvlUp.spawnRandomBullets()

        print(isBullet1Collided)
        
    if isOnEndScreen:
        op.screen.blit(endScreenUi, (0, 0))
        
        endScoreText = endScoreFont.render(str(level), True, (176.9, 161.6, 57.2))
        endScoreTextRect = endScoreText.get_rect()
        
        endScoreTextRect.x = 405
        endScoreTextRect.y = 81
        
        op.screen.blit(endScoreText, endScoreTextRect)
        
        bestScoreText = bestScoreFont.render(str(bestScoreRead.read()), True, (176.9, 161.6, 57.2))
        bestScoreTextRect = bestScoreText.get_rect()
        
        endScoreTextRect.x = 405
        endScoreTextRect.y = 130
        
        op.screen.blit(bestScoreText, bestScoreTextRect)
        
        
        
    
            
            
    pygame.display.flip()
        
        
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
        if event.type == pygame.KEYDOWN and isOnGame:
            if event.key == pygame.K_LEFT:
                player.actualPlayerRenderer = player.player_left
                turnSound.play()
                isOnLeft = True
                isOnRight = False
                isForward = False
                isBack = False
                
            if event.key == pygame.K_RIGHT:
                player.actualPlayerRenderer = player.player_right
                turnSound.play()
                isOnRight = True
                isOnLeft = False
                isForward = False
                isBack = False
                
            if event.key == pygame.K_DOWN:
                player.actualPlayerRenderer = player.player_forward
                turnSound.play()
                isOnRight = False
                isOnLeft = False
                isForward = False
                isBack = True
                
            if event.key == pygame.K_UP:
                player.actualPlayerRenderer = player.player_back
                turnSound.play()
                isOnRight = False
                isOnLeft = False
                isForward = True
                isBack = False
                
            if event.key == pygame.K_SPACE and isOnLeft == True and moves > 0:
                player.playerRect.x = player.playerRect.x + 56
                moves -= 1
                walking.play()
                
                if player.playerRect.x > 430:
                    player.playerRect.x = 15
                    moves += 1
                    walking.play()
                
            if event.key == pygame.K_SPACE and isOnRight == True and moves > 0:
                player.playerRect.x = player.playerRect.x - 56
                moves -= 1
                walking.play()
                
                if player.playerRect.x < 0:
                    player.playerRect.x = 410
                    moves += 1
                    walking.play()
                
            if event.key == pygame.K_SPACE and isBack == True and moves > 0:
                player.playerRect.y = player.playerRect.y - 53
                moves -= 1
                walking.play()
                
                if player.playerRect.y < 0:
                    player.playerRect.y = 376
                    moves += 1
                    walking.play()
                
            if event.key == pygame.K_SPACE and isForward == True and moves > 0:
                player.playerRect.y = player.playerRect.y + 53
                moves -= 1
                walking.play()
                
                if player.playerRect.y > 390:
                    player.playerRect.y = 5
                    moves += 1
                    walking.play()
                
            if event.key == pygame.K_SPACE and moves == 0:
                noMoves.play()
                
            if event.key == pygame.K_r and moves == 0:
                isOnGame = False
                isOnEndScreen = True
                
                
            if event.key == pygame.K_SPACE and player.playerRect.colliderect(bullet.bulletRect) and isBullet1Collided == False:
                moves += 4
                takeBullet.play()
                isBullet1Collided = True
                
            if event.key == pygame.K_SPACE and player.playerRect.colliderect(secondBullet.bulletRect) and isBullet2Collided == False:
                moves += 4
                takeBullet.play()
                isBullet2Collided = True
                
            if event.key == pygame.K_SPACE and player.playerRect.colliderect(lvlUp.lvlUpRect) and isLvlUpCollided == False:
                moves += 1
                bullet.randomPosition = random.randint(0, 62)
                secondBullet.randomPosition = random.randint(0, 62)
                lvlUp.randomPosition = random.randint(0, 62)
                lvlUpSound.play()
                isBullet1Collided = False
                isBullet2Collided = False
                level += 1