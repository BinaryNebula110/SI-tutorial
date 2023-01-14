import pygame
import random

# initialise pygame
pygame.init()

# create the screen 
resolution = (720, 960)
screen = pygame.display.set_mode((resolution[0], resolution[1]))

# title and icon
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load("assets\logo.png"))

# player
playerImg = pygame.image.load("assets\playerIcon.png").convert_alpha()
iconWidth = 64
playerX = (resolution[0] - iconWidth)/2
playerY = 836
playerXChange = 0

def player(x, y):
    screen.blit(playerImg, (x, y))
    
# enemy
enemyImg = pygame.image.load("assets\enemyIcon.png").convert_alpha()
enemyX, enemyY = 100, 100
enemyXChange = 0.1

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# laser
laserImg = pygame.image.load("assets\\laser.png").convert_alpha()
laserX = 0
laserY = -64
laserYChange = -9
laserStatus = "Ready"

def shootLaser(x):
    global laserStatus
    laserStatus = "Firing"
    global laserX
    laserX = playerX
    global laserY
    laserY = 836

def laser(x, y):
    screen.blit(laserImg, (x+16,y))


# background
background = pygame.image.load("assets\\background.png").convert()

# game loop
running = True 
while running: 
    # clock
    dt = pygame.time.Clock().tick(60)
  
    for event in pygame.event.get():
        
        # quit
        if event.type == pygame.QUIT:
            running = False
            pygame.quit
            
        # player movement + shooting
        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_a:
                playerXChange = playerXChange - 0.3
            if  event.key == pygame.K_d:
                playerXChange = playerXChange + 0.3
            if event.key == pygame.K_SPACE and laserStatus == "Ready":
                shootLaser(playerX)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                playerXChange = playerXChange + 0.3
            if  event.key == pygame.K_d:
                playerXChange = playerXChange - 0.3
    # background 
    screen.fill((0,0,0))       
    screen.blit(background, (0, 0))
    
    # player
    playerX += playerXChange*dt
    if playerX >= resolution[0]-iconWidth:
        playerX = resolution[0]-iconWidth
    elif playerX <= 0:
        playerX = 0
    player(playerX, playerY)
    
    # enemy 
    enemyX += enemyXChange*dt
    if enemyX >= resolution[0]-iconWidth:
        enemyX = resolution[0]-iconWidth
        enemyXChange = enemyXChange * -1
        enemyY = enemyY + 20
    elif enemyX <= 0:
        enemyX = 0
        enemyXChange = enemyXChange * -1
        enemyY = enemyY + 32
    enemy(enemyX, enemyY)
    
    #laser
    if laserStatus == "Firing":
        laserY = laserY + laserYChange
        laser(laserX, laserY)
    if laserY <= 0:
        laserStatus = "Ready"
    
    # update
    pygame.display.update()