# import package
import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, image_name, scale):
		# get the image
		self.image = pygame.image.load(image_name)
		# get the rect
		self.rect = self.image.get_rect()
		# scale the image
		self.image = pygame.transform.scale(self.image, (int(scale*self.rect.width), int(scale*self.rect.height)))
		# scale the rect
		self.rect = self.image.get_rect()