import pygame
class Ship:
	def __init__(self, ai_game):
		self.screen = ai_game.screen

		self.settings=ai_game.settings

		self.screen_rect = ai_game.screen.get_rect()

		self.image = pygame.image.load('images/ship.bmp')

		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom

		self.x = float(self.rect.x)

		self.moving_right = False #movement flag for continuous movement
		self.moving_left= False
		self.moving_up = False
		self.moving_down = False
	def update(self):
		#if self.moving_right:
		#	self.x += self.settings.ship_speed
		#if self.moving_left:
			#self.x -= self.settings.ship_speed
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:  #or we can use self.screen_rect.right
			self.x -= self.settings.ship_speed
		self.rect.x=self.x
	#	if self.moving_up:
	#		self.rect.y -=1
	#	if self.moving_down:
	#		self.rect.y +=1
	def center_ship(self):
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
	def blitme(self):
		self.screen.blit(self.image, self.rect)
