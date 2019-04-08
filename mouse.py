
#DUMMY FILE FOR TESTING METHODS
import pygame, sys
from pygame import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))

while True: # main game loop
	for event in pygame.event.get(): # event handling loop
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			print(pygame.mouse.get_pressed())
		elif event.type == KEYDOWN:
			if (event.key == K_LEFT or event.key == K_a)
				print(event.key)
			elif (event.key == K_RIGHT or event.key == K_d)
				print(event.key)
			elif (event.key == K_UP or event.key == K_w)
				print(event.key)
			elif (event.key == K_DOWN or event.key == K_s)
				print(event.key)
			elif (event.key == K_n):
				all_keys = pygame.key.get_pressed()
				if all_keys[pygame.K_d] and all_keys[pygame.K_a]:
					print(all_keys)
			elif event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
'''
pygame.mouse.get_pressed	—	get the state of the mouse buttons
pygame.mouse.get_pos	—	get the mouse cursor position
pygame.mouse.get_rel	—	get the amount of mouse movement
pygame.mouse.set_pos	—	set the mouse cursor position
pygame.mouse.set_visible	—	hide or show the mouse cursor
pygame.mouse.get_focused	—	check if the display is receiving mouse input
pygame.mouse.set_cursor	—	set the image for the system mouse cursor
pygame.mouse.get_cursor	—	get the image for the system mouse cursor
'''
