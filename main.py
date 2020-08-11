# import packages
import random
import pygame
# import all important constants from pygame.locals
from pygame.locals import * 

# start pygame
pygame.init()

# setting up the screen
screen_info = pygame.display.Info()
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
color = (0, 0, 0)

# setting up the clock
clock = pygame.time.Clock()

# setting up background
background_image = pygame.image.load("clouds.gif")
background_rect = background_image.get_rect()
# reisizing image
background_image = pygame.transform.scale(background_image,(width, height))
background_rect = background_image.get_rect()

def main():
	while True:
		# setting the frame ate
		clock.tick(60)
		# filling in background color
		screen.fill(color)
		# drawing backdrop
		screen.blit(background_image, background_rect)
		# update the screen
		pygame.display.flip()

main()