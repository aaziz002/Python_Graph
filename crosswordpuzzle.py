import pygame, sys
#import WordCrapes
from pygame.locals import *

# Dummy function
def doNothing():
    x = None

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((800, 600))
    
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONDOWN:
                #print(pygame.mouse.get_pressed())
                button(pygame.mouse.get_pressed())
            elif event.type == MOUSEMOTION: #tracks the  mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                position = (mouse_x, mouse_y)
            elif event.type == KEYDOWN:
                button(event.key)

#This function can be keyed to anything we desire.
def button(key):
    #keyboard section
    if (key == K_LEFT or key == K_a):
        doNothing()
    elif (key == K_RIGHT or key == K_d):
        doNothing()
    elif (key == K_UP or key == K_w):
        doNothing()
    elif (key == K_DOWN or key == K_s):
        doNothing()
    elif (key == K_LALT or K_RALT): # section for key combinations
        all_keys = pygame.key.get_pressed()
        if all_keys[pygame.K_RETURN]:
            print("screen change")
    elif (key == K_q):
        doNothing()
    elif (key == K_e):
        doNothing()
    elif (key == K_r):
        doNothing()
    elif (key == K_t):
        doNothing()
    elif (key == K_y):
        doNothing()
    elif (key == K_u):
        doNothing()
    elif (key == K_i):
        doNothing()
    elif (key == K_o):
        doNothing()
    elif (key == K_p):
        doNothing()
    elif (key == K_f):
        doNothing()
    elif (key == K_g):
        doNothing()
    elif (key == K_h):
        doNothing()
    elif (key == K_j):
        doNothing()
    elif (key == K_k):
        doNothing()
    elif (key == K_l):
        doNothing()
    elif (key == K_z):
        doNothing()
    elif (key == K_x):
        doNothing()
    elif (key == K_c):
        doNothing()
    elif (key == K_v):
        doNothing()
    elif (key == K_b):
        doNothing()
    elif (key == K_n):
        doNothing()
    elif (key == K_m):
        doNothing()
    elif (key == K_q):
        doNothing()
    elif (key == K_1 or key == K_2 or key == K_3 or
          key == K_4 or key == K_5 or key == K_6 or
          key == K_7 or key == K_8 or key == K_9 or
          key == K_0 or key == K_INSERT or key == K_HOME or
          key == K_PAGEUP or key == K_PAGEDOWN or key == K_DELETE or
          key == K_END or key == K_NUMLOCK or key == K_TAB
          ):
        doNothing()  #invalid key section until we need them for something
    elif key == K_ESCAPE:
        terminate()
    elif (key == (1,0,0)): #Mouse section
        doNothing() #left click
    elif (key == (0,0,1)):
        doNothing() #right click
    elif (key == (0,1,0)):
        doNothing() #middle click
 #   elif event.type == MOUSEBUTTONDOWN: #Mouse section
  #        print(pygame.mouse.get_pressed())

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
