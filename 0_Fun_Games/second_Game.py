import pygame
import random
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space War")

# Load images (simple colored rectangles for demo, replace with real images for realism)
PLAYER_IMG = pygame.Surface((60, 48), pygame.SRCALPHA)
pygame.draw.polygon(PLAYER_IMG, (0, 255, 255), [(0, 48), (30, 0), (60, 48)])

ENEMY_IMG = pygame.Surface((50, 40), pygame.SRCALPHA)
pygame.draw.polygon(ENEMY_IMG, (255, 0, 0), [(0, 40), (25, 0), (50, 40)])

BULLET_IMG = pygame.Surface((8, 20), pygame.SRCALPHA)
pygame.draw.rect(BULLET_IMG, (255, 255, 0), (0, 0, 8, 20))

# Background
STAR_COLOR = (255, 255, 255)
stars = [[random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 3)] for _ in range(100)]

# Player class
class Player:
	def __init__(self):
		self.image = PLAYER_IMG
		self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 60))
		self.speed = 7
		self.cooldown = 0

	def move(self, dx):
		self.rect.x += dx * self.speed
		self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))

	def draw(self, surface):
		surface.blit(self.image, self.rect)

	def shoot(self):
		if self.cooldown == 0:
			bullets.append(Bullet(self.rect.centerx, self.rect.top))
			self.cooldown = 15

	def update(self):
		if self.cooldown > 0:
			self.cooldown -= 1

# Bullet class
class Bullet:
	def __init__(self, x, y):
		self.image = BULLET_IMG
		self.rect = self.image.get_rect(center=(x, y))
		self.speed = -12

	def update(self):
		self.rect.y += self.speed
		return self.rect.bottom > 0

	def draw(self, surface):
		surface.blit(self.image, self.rect)

# Enemy class
class Enemy:
	def __init__(self):
		self.image = ENEMY_IMG
		self.rect = self.image.get_rect(center=(random.randint(50, WIDTH-50), -40))
		self.speed = random.randint(2, 5)
		self.hp = 2

	def update(self):
		self.rect.y += self.speed
		return self.rect.top < HEIGHT

	def draw(self, surface):
		surface.blit(self.image, self.rect)

# Game variables
player = Player()
bullets = []
enemies = []
score = 0
font = pygame.font.SysFont('consolas', 28)
game_over = False

# Main game loop
clock = pygame.time.Clock()
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 900)

def draw_background():
	screen.fill((10, 10, 30))
	for star in stars:
		pygame.draw.circle(screen, STAR_COLOR, (star[0], star[1]), star[2])
		star[1] += star[2]
		if star[1] > HEIGHT:
			star[0] = random.randint(0, WIDTH)
			star[1] = 0

def reset_game():
	global bullets, enemies, score, game_over
	bullets = []
	enemies = []
	score = 0
	player.rect.center = (WIDTH // 2, HEIGHT - 60)
	game_over = False

while True:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == SPAWN_EVENT and not game_over:
			enemies.append(Enemy())
		if event.type == pygame.KEYDOWN and game_over:
			if event.key == pygame.K_r:
				reset_game()

	keys = pygame.key.get_pressed()
	if not game_over:
		dx = 0
		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			dx -= 1
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			dx += 1
		player.move(dx)
		if keys[pygame.K_SPACE]:
			player.shoot()
		player.update()

	# Update bullets
	bullets = [b for b in bullets if b.update()]

	# Update enemies
	enemies = [e for e in enemies if e.update()]

	# Collision detection
	for bullet in bullets[:]:
		for enemy in enemies[:]:
			if bullet.rect.colliderect(enemy.rect):
				enemy.hp -= 1
				if enemy.hp <= 0:
					enemies.remove(enemy)
					score += 10
				if bullet in bullets:
					bullets.remove(bullet)
				break

	# Enemy hits player
	for enemy in enemies:
		if enemy.rect.colliderect(player.rect):
			game_over = True

	# Draw everything
	draw_background()
	for bullet in bullets:
		bullet.draw(screen)
	for enemy in enemies:
		enemy.draw(screen)
	player.draw(screen)

	# Score
	score_text = font.render(f"Score: {score}", True, (255,255,255))
	screen.blit(score_text, (10, 10))

	if game_over:
		over_text = font.render("GAME OVER! Press R to Restart", True, (255, 80, 80))
		screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2))

	pygame.display.flip()
