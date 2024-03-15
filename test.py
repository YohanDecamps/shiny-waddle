import json
import pygame
from operator import itemgetter

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

data_name = input("give me the name of the data\n")

with open(data_name) as f:
   data = json.load(f)

data_param = input("give me the parameter to sort the data\n")

sorted_data = sorted(data, key=lambda x: x[data_param])

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()