import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	"""The class of the Game Alien Invasion"""

	def __init__(self):
		"""Initialize the game"""
		pygame.init()
		self.settings = Settings()

		# set the screen size
		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

		# set the caption
		pygame.display.set_caption("Alien Invasion")

		# set the background color
		self.bg_color = (self.settings.bg_color)

		# initialize ship
		self.ship = Ship(self)

	def run_game(self):
		"""Run the game"""
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# redraw the screen during each pass of the loop
			self.screen.fill(self.bg_color)
			self.ship.blitme()

			# make the most recently drawn screen visible
			pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()