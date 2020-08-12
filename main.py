# import packages
import random
import pygame
# import all important constants from pygame.locals
from pygame.locals import * 
# import classes
from player import Player
from enemy import Enemy
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
# resizing image
background_image = pygame.transform.scale(background_image,(width, height))
# resizing the rect
background_rect = background_image.get_rect()
# centering the sprite on the screen
background_rect.center = (width // 2, height // 2)

# set up the player
player = Player(image_name = "balloon.png", scale = 0.5, pos = (50, 100))

enemies = pygame.sprite.Group()
level = 1
for i in range(level+2):
	# set up the player
	enemy = Enemy(image_name = "spike.png", scale = 0.65)
	enemies.add(enemy)

def main():
	while True:
		# setting the frame rate
		clock.tick(60)
		
		# How the player moves
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_DOWN:
					player.speed[1] = 10
				if event.key == K_UP:
					player.speed[1] = -10
				if event.key == K_LEFT:
					player.speed[0] = -10
				if event.key == K_RIGHT:
					player.speed[0] = 10
			if event.type == KEYUP:
				if event.key == K_DOWN or event.key == K_UP:
					player.speed[1] = 0
				if event.key == K_LEFT or event.key == K_RIGHT:
					player.speed[0] = 0
		#move player by speed	
		player.move_player()
		# Update enemies
		enemies.update()
		# check if player is hit
		hits = player.sprite.spritecollide(player, enemies, False)
		if hits:
			player.reset(50,100)
		# filling in background color
		screen.fill(color)
		# drawing backdrop
		screen.blit(background_image, background_rect)
		# draw enemies
		enemies.draw(screen)
		# draw the player
		screen.blit(player.image, player.rect)
		# update the screen
		pygame.display.flip()
main()