import pygame
from options import Options
from instantiate import *
from variables import *

pygame.init()

running = True
ui = pygame.image.load("images/mapAndUi.png")

turnSound = pygame.mixer.Sound("sounds/turn.wav")
noMoves = pygame.mixer.Sound("sounds/noMoves.Wav")
walking = pygame.mixer.Sound("sounds/walking.wav")
takeBullet = pygame.mixer.Sound("sounds/takeBullet.wav")

uiFont = pygame.font.SysFont("Poppins-Medium.ttf", 55)


turnSound.set_volume(0.05)
noMoves.set_volume(0.05)
walking.set_volume(0.05)
takeBullet.set_volume(0.07)

moves = 5

while running:
    
    movesRemains = uiFont.render(str(moves), True, (0, 0, 0))
    movesRemainsRect = movesRemains.get_rect()
    
    movesRemainsRect.x = 600
    movesRemainsRect.y = 12.5 
    
    op.screen.blit(ui, (0, 0))
    op.screen.blit(movesRemains, movesRemainsRect)
    op.screen.blit(player.actualPlayerRenderer, (player.playerRect.x, player.playerRect.y))
    
    if isBullet1Collided == False:
        op.screen.blit(bullet.bullet, (bullet.bulletRect.x, bullet.bulletRect.y))
        
    if isBullet2Collided == False:
        op.screen.blit(secondBullet.bullet, (secondBullet.bulletRect.x, secondBullet.bulletRect.y))
    
    print(player.playerRect.x," " , player.playerRect.y)
    
    bullet.spawnRandomBullets()
    secondBullet.spawnRandomBullets()
        
    print(isBullet1Collided)
    
            
            
    pygame.display.flip()
        
        
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
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
                player.playerRect.x = player.playerRect.x + 57
                moves -= 1
                walking.play()
                
                if player.playerRect.x > 399:
                    player.playerRect.x = 0
                    moves += 1
                    walking.play()
                
            if event.key == pygame.K_SPACE and isOnRight == True and moves > 0:
                player.playerRect.x = player.playerRect.x - 57
                moves -= 1
                walking.play()
                
                if player.playerRect.x < 0:
                    player.playerRect.x = 399
                    moves += 1
                    walking.play()
                
            if event.key == pygame.K_SPACE and isBack == True and moves > 0:
                player.playerRect.y = player.playerRect.y - 52
                moves -= 1
                walking.play()
                
                if player.playerRect.y < 0:
                    player.playerRect.y = 364
                    moves += 1
                    walking.play()
                
            if event.key == pygame.K_SPACE and isForward == True and moves > 0:
                player.playerRect.y = player.playerRect.y + 52
                moves -= 1
                walking.play()
                
                if player.playerRect.y > 364:
                    player.playerRect.y = 0
                    moves += 1
                    walking.play()
                
            if event.key == pygame.K_SPACE and moves == 0:
                noMoves.play()
                
            if event.key == pygame.K_SPACE and player.playerRect.colliderect(bullet.bulletRect) and isBullet1Collided == False:
                moves += 3
                takeBullet.play()
                isBullet1Collided = True
                
            if event.key == pygame.K_SPACE and player.playerRect.colliderect(secondBullet.bulletRect) and isBullet2Collided == False:
                moves += 3
                takeBullet.play()
                isBullet2Collided = True
                
            