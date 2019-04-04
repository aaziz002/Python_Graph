import pygame, sys
from pygame import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))

while True: # main game loop
	for event in pygame.event.get(): # event handling loop
		if event.type == QUIT:
			sys.terminate()
		elif event.type == MOUSEBUTTONDOWN:
			print(pygame.mouse.get_pressed())
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
					print(0)
			elif event.key == K_ESCAPE:
				sys.terminate()
