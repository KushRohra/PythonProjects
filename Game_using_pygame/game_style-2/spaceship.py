class Spaceship():
	def __init__(self, health, max_bullets):
		self.health = health
		self.max_bullets = max_bullets
		self.bullets = []

	def get_bullets(self):
		return self.bullets

	def append_to_bullets(self, bullet):
		self.bullets.append(bullet)

	def get_health(self):
		return self.health

	def dec_health(self):
		self.health -= 1