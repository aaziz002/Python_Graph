import pygame, sys
from pygame.locals import *

# Dummy function
def hello():
    print("hello")

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((800, 600))
    
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pressed())
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                position = (mouse_x, mouse_y)
                print(position)
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a):
                    hello()
                elif (event.key == K_RIGHT or event.key == K_d):
                    hello()
                elif (event.key == K_UP or event.key == K_w):
                    hello()
                elif (event.key == K_DOWN or event.key == K_s):
                    hello()
                elif (event.key == K_n):
                    all_keys = pygame.key.get_pressed()
                    if all_keys[pygame.K_d] and all_keys[pygame.K_a]:
                        hello()
                elif event.key == K_ESCAPE:
                    terminate()

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
