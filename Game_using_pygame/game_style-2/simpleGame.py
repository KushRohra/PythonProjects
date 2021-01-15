import pygame
import os

pygame.font.init()
pygame.mixer.init()

from variables import *
from spaceship import Spaceship

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

BORDER = pygame.Rect(WIDTH//2 - BORDER_WIDTH//2, 0, BORDER_WIDTH, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'explosion.mp3')) 
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'fire.mp3'))

red_spaceship_object = Spaceship(10, MAX_BULLETS)
yellow_spaceship_object = Spaceship(10, MAX_BULLETS)

def draw_window(red, yellow):
	WIN.blit(SPACE, (0,0))
	pygame.draw.rect(WIN, BLACK, BORDER)

	red_health_text = HEALTH_FONT.render("Health: " + str(red_spaceship_object.get_health()), 1, WHITE)
	yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_spaceship_object.get_health()), 1, WHITE)
	WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - PADDING_RIGHT, PADDING_TOP))
	WIN.blit(yellow_health_text, (PADDING_RIGHT, PADDING_TOP))

	WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
	WIN.blit(RED_SPACESHIP, (red.x, red.y))
	for bullet in red_spaceship_object.get_bullets():
		pygame.draw.rect(WIN, RED, bullet)
	for bullet in yellow_spaceship_object.get_bullets():
		pygame.draw.rect(WIN, YELLOW, bullet)
	pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
	if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > 0: #LEFT
			yellow.x -= VELOCITY
	if keys_pressed[pygame.K_d] and yellow.x + VELOCITY + yellow.width < BORDER.x: #RIGHT
		yellow.x += VELOCITY
	if keys_pressed[pygame.K_w] and yellow.y - VELOCITY > 0: #UP
		yellow.y -= VELOCITY
	if keys_pressed[pygame.K_s] and yellow.y + VELOCITY + yellow.height < HEIGHT - 15: #DOWN
		yellow.y += VELOCITY

def red_handle_movement(keys_pressed, red):
	if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY > BORDER.x + BORDER.width: #LEFT
			red.x -= VELOCITY
	if keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY + red.width < WIDTH: #RIGHT
		red.x += VELOCITY
	if keys_pressed[pygame.K_UP] and red.y - VELOCITY > 0: #UP
		red.y -= VELOCITY
	if keys_pressed[pygame.K_DOWN] and red.y + VELOCITY + red.height < HEIGHT - 15: #DOWN
		red.y += VELOCITY

def handle_bullets(red, yellow):
	for bullet in yellow_spaceship_object.get_bullets():
		bullet.x += BULLET_VELOCITY
		if red.colliderect(bullet):
			pygame.event.post(pygame.event.Event(RED_HIT))
			yellow_spaceship_object.bullets.remove(bullet)
		elif bullet.x > WIDTH:
			yellow_spaceship_object.bullets.remove(bullet)
	for bullet in red_spaceship_object.get_bullets():
		bullet.x -= BULLET_VELOCITY
		if yellow.colliderect(bullet):
			pygame.event.post(pygame.event.Event(YELLOW_HIT))
			red_spaceship_object.bullets.remove(bullet)
		elif bullet.x < 0:
			red_spaceship_object.bullets.remove(bullet)

def draw_winner(winner_text):
	draw_winner_text = WINNER_FONT.render(winner_text, 1, WHITE)
	WIN.blit(draw_winner_text, (WIDTH//2 - draw_winner_text.get_width()//2, HEIGHT//2 - draw_winner_text.get_height()//2))
	pygame.display.update()
	pygame.time.delay(5000)

def main():
	clock = pygame.time.Clock()

	yellow = pygame.Rect(SPACESHIP_POSITION_PADDING - SPACESHIP_WIDTH, HEIGHT//2 - SPACESHIP_HEIGHT//2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
	red = pygame.Rect(WIDTH - SPACESHIP_POSITION_PADDING, HEIGHT//2 - SPACESHIP_HEIGHT//2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

	run = True   
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LCTRL and len(yellow_spaceship_object.bullets) < yellow_spaceship_object.max_bullets:
					bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - BULLET_HEIGHT//2, BULLET_WIDTH, BULLET_HEIGHT)
					yellow_spaceship_object.append_to_bullets(bullet)
					BULLET_FIRE_SOUND.play()
				if event.key == pygame.K_RCTRL and len(red_spaceship_object.bullets) < red_spaceship_object.max_bullets:
					bullet = pygame.Rect(red.x, red.y + red.height//2 - BULLET_HEIGHT//2, BULLET_WIDTH, BULLET_HEIGHT)
					red_spaceship_object.append_to_bullets(bullet)
					BULLET_FIRE_SOUND.play()
		
			if event.type == RED_HIT:
				red_spaceship_object.dec_health()
				BULLET_HIT_SOUND.play()
			if event.type == YELLOW_HIT:
				yellow_spaceship_object.dec_health()
				BULLET_HIT_SOUND.play()
	
		winner_text = ""
		if red_spaceship_object.get_health() <= 0:
			winner_text = "YELLOW WINS!"
		if yellow_spaceship_object.get_health() <= 0:
			winner_text = "RED WINS!"
		if red_spaceship_object.get_health() <=0 and yellow_spaceship_object.get_health() <= 0:
			winner_text = "TIE!"

		if winner_text != "":
			draw_winner(winner_text)
			break

		keys_pressed = pygame.key.get_pressed()
		yellow_handle_movement(keys_pressed, yellow)
		red_handle_movement(keys_pressed, red)

		handle_bullets(red, yellow)

		draw_window(red, yellow)

	main()

if __name__ == "__main__":
	main()
