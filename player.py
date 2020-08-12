# import package
import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, image_name, scale, pos):
		super().__init__()
		# get the image
		self.image = pygame.image.load(image_name)
		# get the rect
		self.rect = self.image.get_rect()
		# scale the image
		self.image = pygame.transform.scale(self.image, (int(scale*self.rect.width), int(scale*self.rect.height)))
		# scale the rect
		self.rect = self.image.get_rect()
		#setup player's position
		self.reset(pos)
		self.speed = pygame.math.Vector2 (0,0)

	def reset(self, pos):
		self.rect.center = pos

	def move_player(self):
		self.rect.move_ip(self.speed)
		#left bound
		if self.rect.left < -10:
			self.rect.left = -10
		#top bound
		if self.rect.top < 0:
			self.rect.top = 0
		#bottom bound
		if self.rect.bottom > 600:
			self.rect.bottom = 600