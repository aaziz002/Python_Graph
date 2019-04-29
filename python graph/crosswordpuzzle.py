import pygame, sys
from WordCrapes import *
from pygame.locals import *

#global variables for animations and background
FPS = 15
WINDOWWIDTH = 1024
WINDOWHEIGHT = 1000
OPTION_LETTERS = 60
FOUND_LETTERS = 100
BOARDWIDTH = 2
BOARDHEIGHT = 3
BGCOLOR= (100, 100, 100)


# Dummy function
def doNothing():
    x = None

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Word Puzzle Game')
    mainboard = GetRandomizedBoard(DISPLAYSURF,0)

    pygame.display.update()
    
    introMenu(DISPLAYSURF,FPSCLOCK)
    DISPLAYSURF.fill((12,0,128))
    
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

        pygame.display.update()
        FPSCLOCK.tick(FPS)

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
        fullscreen = False
        all_keys = pygame.key.get_pressed()
        if all_keys[pygame.K_RETURN]:
            print("screen change")
            if (not(fullscreen)):  # if not fullscreen then switch to fullscreen
                #pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.FULLSCREEN)
                pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                fullscreen = True
                pygame.display.update()
            else:   # if fullscreen the switch to not fullscreen
                pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                fullscreen = False
                pygame.display.update()
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

def drawPressKeyMsg():
    MILDWHITE = (128,128,128)
    wordFont = pygame.font.SysFont('monospace', 12)
    pressKeySurf = wordFont.render('Press a key to play.', True, MILDWHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (0,0)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def introMenu(DISPLAYSURF, FPSCLOCK):
    word1 = "CROSSWORD"
    word2 = ["P","U","Z","Z","L","E"]
    WHITE = (255,255,255)
    
    FONTSIZE = int((WINDOWHEIGHT*0.08)*1.5)
    LETTERPOSY = [0,FONTSIZE,FONTSIZE*2,FONTSIZE*3,FONTSIZE*4,FONTSIZE*5,FONTSIZE*6]
    WORDLENGTH = 9
    
    BGCOLOR = (0,0,0)
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        wordFont = pygame.font.SysFont('monospace', FONTSIZE, True)
        wordSurf = wordFont.render(word1, True, WHITE)	
        wordRect = wordSurf.get_rect()    
        DISPLAYSURF.blit(wordSurf,wordRect)

        wordIncr = 0
        posIncr = 1
        for letter in word2:
            wordRect.topleft = (5, LETTERPOSY[posIncr])
            wordSurf = wordFont.render('     ' + word2[wordIncr], True, WHITE)
            DISPLAYSURF.blit(wordSurf,wordRect)
            posIncr += 1
            wordIncr += 1

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def GetRandomizedBoard(DISPLAYSURF,index):
    color = (0,200,0,0.75)
    word = WordSet()
    board = []
    icons = word.words[index]
    random.shuffle(icons)
    for x in range (len(word.words[index])):
        font = pygame.font.SysFont('monospace', 35, True)
        printer = font.render(word.words[index][x],True,color)
        rectangle = printer.get_rect()
        rectangle.topleft = (x*25,30)
        DISPLAYSURF.blit(printer,rectangle)


    return board

if __name__ == '__main__':
    main()
