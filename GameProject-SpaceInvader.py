import pygame
from pygame import mixer
import math
import random

# Initialise Pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("battleship.png")
PlayerX = 370
PlayerY = 520
PlayerX_Change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("extraterrestrial.png"))
    enemyX.append(random.randint(0,750))
    enemyY.append(random.randint(20, 120))
    enemyX_Change.append(0.1)
    enemyY_Change.append(40)

# Bullet
#Ready means: non--visible
#Fire means: bullet visible
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 520
bulletX_Change = 0
bulletY_Change = 0.5
bullet_state = 'ready'

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('game_over.ttf', 128)

def show_score(x,y):
    score = font.render('Score : ' + str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))
    
def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255,255,255))
    screen.blit(over_text, (240, 280))

def Player(x,y):
    screen.blit(playerImg, (PlayerX, PlayerY))
    
def Enemy(x,y, i):
    screen.blit(enemyImg[i],(enemyX[i], enemyY[i]))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+16,y+10))
    
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+ (math.pow(enemyY-bulletY,2)))
    if distance < 25:
        return True
    else:
        return False


# Game loop
running = True
while running:

    # RGB-Background
    screen.fill((75, 117, 117))
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        #If keystroke pressed check whether is right or left
        if event.type == pygame.KEYDOWN:
            print('Key is pressed')
            if event.key == pygame.K_LEFT:
                PlayerX_Change = -0.2
            if event.key == pygame.K_RIGHT:
                PlayerX_Change = 0.2
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_Sound = mixer.Sound('laser_pew.wav')
                    bullet_Sound.play()
                    bulletX = PlayerX
                    fire_bullet(PlayerX, bulletY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                PlayerX_Change = 0
            
    # Checking boundaries of screen
    PlayerX += PlayerX_Change
    if PlayerX <=0:
        PlayerX = 0
    elif PlayerX >= 730:
        PlayerX = 730
        
    # Enemy Movement
    for i in range(num_of_enemies):
        
        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        
        enemyX[i] += enemyX_Change[i]
        if enemyX[i] <=0:
            enemyX_Change[i] = 0.1
            enemyY[i] += enemyY_Change[i]
        elif enemyX[i] >= 730:
            enemyX_Change[i] = -0.1
            enemyY[i] += enemyY_Change[i]

# Collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 520
            bullet_state = 'ready'
            score_value += 1
            print('Score is ', score_value)
            enemyX[i] = random.randint(0,729)
            enemyY[i] = random.randint(20, 120)

        Enemy(enemyX[i],enemyY[i], i)

    # Bullet Movement
    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_Change
    if bulletY <= 0:
        bulletY=520
        bullet_state = 'ready'
        
    
        

    Player(PlayerX, PlayerY)
    show_score(textX,textY)
    pygame.display.update()
