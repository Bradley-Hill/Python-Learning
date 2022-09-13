
import pygame

#Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("SideShooter")
icon = pygame.image.load('pythonProject\spaceship.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("pythonProject\spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y): 
    screen.blit(playerImg, (x, y))

#Game Loop
running = True
while running:
    #RGB - Red, Green, Blue
    screen.fill((0, 200, 245))
    playerX += 0.01
    playerY -= 0.02 * 0.5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               print('Left arrow presed')
            if event.key == pygame.K_RIGHT:
               print('Right arrow presed')
    
    player(playerX, playerY)
    
    pygame.display.update()