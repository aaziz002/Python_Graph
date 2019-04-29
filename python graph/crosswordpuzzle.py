import pygame, sys
from WordCrapes import *
from pygame.locals import *

#global variables for animations and background
FPS = 15
WINDOWWIDTH   = 1024
WINDOWHEIGHT  = 1000
OPTION_LETTERS = 60
FOUND_LETTERS = 100
BOARDWIDTH    = 2
BOARDHEIGHT   = 3
BGCOLOR       = (100, 100, 100)
LIGHTWHITE    = (128,128,128)

# Dummy function
def doNothing():
    x = None
    
# High Score File functionality
def scorefile_reset():
    numberList = ["0\n","0\n","0\n"]
    file = open("highscore.txt", "w+")
    file.writelines(numberList)
    file.close()

def validFileCheck():
    try:
        file = open("highscore.txt", "r")
        file.close()
    except IOError:
        scorefile_reset()

# load highscore list from highscore.txt and display top 3 scores to start screen
    
def drawHighScore(DISPLAYSURF, WINDOWWIDTH, WINDOWHEIGHT):
    FONTSIZE = int((WINDOWHEIGHT*0.06)*1.5), int(WINDOWHEIGHT*0.06)
    SCORELENGTH = None
    SCOREPOSY = [0,FONTSIZE[0],FONTSIZE[0]*2]
    NUMBEROFSCORES = 3
    
    validFileCheck()
    highScore_file = open("highscore.txt", "r")
    scoreList = highScore_file.readlines()
    SCORELENGTH = len(scoreList[0])
    highScore_file.close()
    
    highScoreFont = pygame.font.SysFont('monospace', FONTSIZE[0]), pygame.font.SysFont('monospace', FONTSIZE[1])
    
    for score in range(NUMBEROFSCORES):
        if score == 0:
            highScoreSurf = highScoreFont[0].render(scoreList[score].rstrip('\n'), True, LIGHTWHITE)
        else:
            highScoreSurf = highScoreFont[1].render(scoreList[score].rstrip('\n'), True, LIGHTWHITE)
        
        highScoreRect = highScoreSurf.get_rect()
        highScoreRect.topright = (WINDOWWIDTH-SCORELENGTH,SCOREPOSY[score])
        DISPLAYSURF.blit(highScoreSurf,highScoreRect)

# if new high score
# 	update highscore list with new highscore

def loadHighScoreList():
    validFileCheck()
    scoreList = []
    file = open("highscore.txt", "r")
    scoreList.append(file.readline())
    scoreList.append(file.readline())
    scoreList.append(file.readline())
    file.close()

def updateNewHighScoreAndPos(self, score, pos):
    newScorePos = [score,(pos-1)]

def getNewScoreAndPosition():
    return newScorePos

def updateHighScoreList(scoreList):
    newScore, position = getNewScoreAndPosition()
    scoreList[position] = str(newScore) + "\n"
    file = open("highscore.txt", "w+")
    file.writelines(scoreList)
    file.close()
    
def isHighScore(newScore, scoreList):
    loadHighScoreList()
    topScore = int(scoreList[0])
    middleScore = int(scoreList[1])
    bottomScore = int(scoreList[2])
    
    if not(
        newScore == topScore or
        newScore == middleScore or
        newScore == bottomScore
    ):
        if newScore > topScore:
            updateNewHighScoreAndPos(newScore, 1)
            updateHighScoreList(scoreList)
            return True
        elif newScore > middleScore:
            updateNewHighScoreAndPos(newScore, 2)
            updateHighScoreList(scoreList)
            return True
        elif newScore > bottomScore:
            updateNewHighScoreAndPos(newScore, 3)
            updateHighScoreList(scoreList)
            return True
        else:
            return False
    else:
        return False
    


def main():
    validFileCheck()
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
                button(pygame.mouse.get_pressed())
            elif event.type == MOUSEMOTION: #tracks the  mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                position = (mouse_x, mouse_y)
            elif event.type == KEYDOWN:
                button(event.key)

        didWin = False
        gameOver(DISPLAYSURF, FPSCLOCK, didWin)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        main()

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

def gameOver(DISPLAYSURF, FPSCLOCK, didWin):
    word1 = "GAME"
    word2 = "OVER"
    word3 = "YOU"
    word4 = "WIN!"
    WHITE = (255,255,255)
    
    FONTSIZE = int((WINDOWHEIGHT*0.08)*1.5)
    LETTERPOSY = [0,FONTSIZE,FONTSIZE*2,FONTSIZE*3,FONTSIZE*4,FONTSIZE*5,FONTSIZE*6]
    WORDLENGTH = 9
    
    BGCOLOR = (0,0,0)
    while True:
        if not(didWin):
            DISPLAYSURF.fill(BGCOLOR)
            wordFont = pygame.font.SysFont('monospace', FONTSIZE, True)
            wordSurf = wordFont.render(word1, True, WHITE)	
            wordRect = wordSurf.get_rect()    
            DISPLAYSURF.blit(wordSurf,wordRect)

            wordFont = pygame.font.SysFont('monospace', FONTSIZE, True)
            wordSurf = wordFont.render("         " + word2, True, WHITE)	
            wordRect = wordSurf.get_rect()
            wordRect.topleft = (0,LETTERPOSY[3])    
            DISPLAYSURF.blit(wordSurf,wordRect)
        else:
            DISPLAYSURF.fill(BGCOLOR)
            wordFont = pygame.font.SysFont('monospace', FONTSIZE, True)
            wordSurf = wordFont.render(word3, True, WHITE)	
            wordRect = wordSurf.get_rect()
            DISPLAYSURF.blit(wordSurf,wordRect)

            wordFont = pygame.font.SysFont('monospace', FONTSIZE, True)
            wordSurf = wordFont.render("         " + word4, True, WHITE)	
            wordRect = wordSurf.get_rect()    
            wordRect.topleft = (0,LETTERPOSY[3])
            DISPLAYSURF.blit(wordSurf,wordRect)
        
        drawPressKeyMsg()
        drawHighScore(DISPLAYSURF, WINDOWWIDTH, WINDOWHEIGHT)

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
