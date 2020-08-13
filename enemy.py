import pygame
import random
class Enemy(pygame.sprite.Sprite):
	def __init__(self, image_name, scale):
		super().__init__()
		self.image = pygame.image.load(image_name)
		# get the rect
		self.rect = self.image.get_rect()
		# scale the image
		self.image = pygame.transform.scale(self.image, (int(scale*self.rect.width), int(scale*self.rect.height)))
		# scale the rect
		self.rect = self.image.get_rect()
		# positioning enemy
		x = random.randint(200,700)
		y = random.randint(100,500)

		self.rect.center = (x,y)
	

		# setting up speed of sprite
		self.speed = pygame.math.Vector2(0, 3)
		self.rotation = random.randint(0, 360)
		self.speed.rotate_ip(self.rotation)

	def update(self):
		self.rect.move_ip(self.speed)
		# bouncing off walls
		if self.rect.right > 800 or self.rect.left < 150:
			self.speed[0] *= -1
		if self.rect.top < 0 or self.rect.bottom > 600:
			self.speed[1] *= -1
