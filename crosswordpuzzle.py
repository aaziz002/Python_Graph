import pygame
from pygame import *

pygame.init()

# Dummy function
def hello():
    print("hello")

def main():
    direction = None
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
                        hello()
                elif event.key == K_ESCAPE:
                    terminate()

main()
