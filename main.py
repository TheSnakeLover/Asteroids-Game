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
color = (8, 39, 157)

# setting up the clock
clock = pygame.time.Clock()

# setting up the sprite
sprite_image = pygame.image.load("Shark.png")
sprite_rect = sprite_image.get_rect()
sprite_image = pygame.transform.scale(sprite_image,(int(0.5*sprite_rect.width), int(0.5*sprite_rect.height)))
sprite_rect = sprite_image.get_rect()
# centering the sprite on the screen
sprite_rect.center = (width // 2, height // 2)

# setting up speed of sprite
speed = pygame.math.Vector2(0, 10)
rotation = random.randint(0, 360)
speed.rotate_ip(rotation)

def move_sprite():
	sprite_rect.move_ip(speed)
	if sprite_rect.right > width or sprite_rect.left < 0:
		speed[0] *= -1
	if sprite_rect.top < -30 or sprite_rect.bottom > height + 40:
		speed[1] *= -1

def main():
	while True:
		# setting the frame rate
		clock.tick(60) 
		# move the sprite
		move_sprite()
		# filling the background
		screen.fill(color)
		# draw the sprite to the screen
		screen.blit(sprite_image, sprite_rect)
		# updating the display
		pygame.display.flip()

main()