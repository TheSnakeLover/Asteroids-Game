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
start = (50, 100)
player = Player(image_name = "balloon.png", scale = 0.2, pos = start)

# set up enemies as a group
enemies = pygame.sprite.Group()

def makeEnemies(level):
	# clear old enemies
	enemies.empty()
	for i in range(level+2):
	# set up new enemies
		enemy = Enemy(image_name = "spike.png", scale = 0.65)
		enemies.add(enemy)

def main():
	level = 1
	speed = 10
	death = 0
	makeEnemies(level)
	
	# initializing the font for the win screen
	pygame.font.init()
	FONT1 = pygame.font.SysFont(None, 55)
	FONT2 = pygame.font.SysFont(None, 72)

	while True:
		# setting the frame rate
		clock.tick(60)
		
		# How the player moves
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					speed += 5
				if event.key == K_DOWN:
					player.speed[1] = speed
				if event.key == K_UP:
					player.speed[1] = -speed
				if event.key == K_LEFT:
					player.speed[0] = -speed
				if event.key == K_RIGHT:
					player.speed[0] = speed
				
				# Go back a level
				if event.key == K_q:
					level -= 1
					if level < 1:
						level = 1
					death += 1
					lower_level = 0
					player.reset((start))
					makeEnemies(level)
				
				# Skip a level 
				if event.key == K_e:
					level += 1
					death += 20
					lower_level = 0
					player.reset((start))
					makeEnemies(level)

			if event.type == KEYUP:
				if event.key == K_DOWN or event.key == K_UP:
					player.speed[1] = 0
				if event.key == K_LEFT or event.key == K_RIGHT:
					player.speed[0] = 0
				if event.key == K_SPACE:
					speed -= 5
		
		#move player by speed	
		player.move_player()
		# Update enemies
		enemies.update()
		
		# check if player is hit
		hits = pygame.sprite.spritecollide(player, enemies, False)
		if hits:
			death += 1
			lower_level = random.randint(1,10)
			if (lower_level > 8):
				level -= 1
				if level < 1:
						level = 1
			lower_level = 0
			player.reset((start))

		# Level completed
		if player.rect.left > width:
			player.reset(start)
			level += 3
			makeEnemies(level)

		# Lose game
		if (death >= 300):
			WIN = 0
			break

		# Win game
		if (level >= 20):
			WIN = 1
			break
	
		# filling in background color
		screen.fill(color)
	
		# drawing backdrop
		screen.blit(background_image, background_rect)
	
		# draw enemies
		enemies.draw(screen)

		# draw the player
		screen.blit(player.image, player.rect)
		
		# death counter
		screen.blit(FONT1.render(f"Deaths: {death}", True, (0,0,0)), (10, 10))

		# level counter
		screen.blit(FONT1.render(f"Level {level}", True, (0,0,0)), (640, 10))
	
		# update the screen
		pygame.display.flip()
		
	# displaying the win screen
	if WIN == 1:
		while True:
			clock.tick(60)
			screen.fill(color)
			screen.blit(FONT2.render("You win!", True, (255,255,255)), (280, 270))
			pygame.display.flip()
	else:
		while True:
			clock.tick(60)
			lose = (205, 55, 55)
			screen.fill(lose)
			screen.blit(FONT2.render("You Lose!", True, (0,0,0)), (275, 270))
			pygame.display.flip()

main()