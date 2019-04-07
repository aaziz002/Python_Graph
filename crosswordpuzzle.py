import pygame
from pygame import *
'''
def main():    
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif (event.key == K_n):
                    all_keys = pygame.key.get_pressed()
                    if all_keys[pygame.K_d] and all_keys[pygame.K_a]:
                        #modTools.easterEgg()
                        #modTools.setNewSpeed("UP",modTools.getSpeedIncrement())
                        # print(modTools.currentSpeedModifier)
                elif event.key == K_ESCAPE:
                    terminate()
                    '''
help(pygame)
pygame.init()
for event in pygame.event.get():
    help(pygame)
    print(KEYDOWN)
    print(event.key)
    print(event)

