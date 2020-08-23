import pygame

class Ship:
	"""The class for ship"""

	def __init__(self, ai_game):
		"""initialize the ship"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# load the image for the ship and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.midbottom = self.screen_rect.midbottom

		# set x-axis of the ship
		self.x = float(self.rect.x)

		self.moving_right = False
		self.moving_left = False
		self.ship_speed = 1.5
	
	def update(self):
		"""update the position of the ship"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.ship_speed
		self.rect.x = self.x

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)