#!python
# Let's import libraries
import pygame
from pygame.locals import *
#import cars
#import weapons
#import land

# Let's startthe game engine
pygame.init()
width, height = 900, 507
player_position = [220,180]
keys = [False, False, False, False]

# initalize the screen
screen=pygame.display.set_mode((width, height))

# Load our character sprite
player = pygame.image.load("files/sprites/5.png")
level = pygame.image.load("files/tileset/level1.png")

# The main game loop
while 1:
  # let's wipe the screen so we can draw on it
  screen.fill(0)

  screen.blit(level,(0,0))
  # Draw our player at these coordinates
  screen.blit(player,player_position)

  # update the screen
  pygame.display.flip()

  # loop through all of our events
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      pygame.quit()
      exit(0)
    # If we're pressing keys - WASD
    if event.type == pygame.KEYDOWN:
        if event.key==K_w:
            keys[0]=True
        elif event.key==K_a:
            keys[1]=True
        elif event.key==K_s:
            keys[2]=True
        elif event.key==K_d:
            keys[3]=True
    if event.type == pygame.KEYUP:
        if event.key==pygame.K_w:
            keys[0]=False
        elif event.key==pygame.K_a:
            keys[1]=False
        elif event.key==pygame.K_s:
            keys[2]=False
        elif event.key==pygame.K_d:
            keys[3]=False
    #move our guy around
    if keys[0]:
        player_position[1]-=5
    elif keys[2]:
        player_position[1]+=5
    if keys[1]:
        player_position[0]-=5
    elif keys[3]:
        player_position[0]+=5
