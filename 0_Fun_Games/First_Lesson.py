import pygame
import sys
import random

# Game Constants
WIDTH, HEIGHT = 400, 600
FPS = 60
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_GAP = 150
PIPE_WIDTH = 60
PIPE_SPEED = 3

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

class Bird:
	def __init__(self):
		self.x = 80
		self.y = HEIGHT // 2
		self.radius = 20
		self.vel = 0
	def update(self):
		self.vel += GRAVITY
		self.y += self.vel
	def flap(self):
		self.vel = FLAP_STRENGTH
	def draw(self):
		pygame.draw.circle(screen, (255, 255, 0), (int(self.x), int(self.y)), self.radius)
	def get_rect(self):
		return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)

class Pipe:
	def __init__(self, x):
		self.x = x
		self.height = random.randint(50, HEIGHT - PIPE_GAP - 50)
		self.passed = False
	def update(self):
		self.x -= PIPE_SPEED
	def draw(self):
		# Top pipe
		pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, PIPE_WIDTH, self.height))
		# Bottom pipe
		pygame.draw.rect(screen, (0, 255, 0), (self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT - self.height - PIPE_GAP))
	def get_top_rect(self):
		return pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
	def get_bottom_rect(self):
		return pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT - self.height - PIPE_GAP)

def draw_text(text, x, y):
	img = font.render(text, True, (255, 255, 255))
	screen.blit(img, (x, y))

def main():
	bird = Bird()
	pipes = [Pipe(WIDTH + 100)]
	score = 0
	running = True
	game_over = False
	while running:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and not game_over:
					bird.flap()
				if event.key == pygame.K_r and game_over:
					main()
					return

		if not game_over:
			bird.update()
			# Pipes logic
			for pipe in pipes:
				pipe.update()
				if not pipe.passed and pipe.x + PIPE_WIDTH < bird.x:
					pipe.passed = True
					score += 1
			# Remove off-screen pipes
			pipes = [p for p in pipes if p.x + PIPE_WIDTH > 0]
			# Add new pipes
			if pipes[-1].x < WIDTH - 200:
				pipes.append(Pipe(WIDTH))
			# Collision
			bird_rect = bird.get_rect()
			for pipe in pipes:
				if bird_rect.colliderect(pipe.get_top_rect()) or bird_rect.colliderect(pipe.get_bottom_rect()):
					game_over = True
			if bird.y - bird.radius < 0 or bird.y + bird.radius > HEIGHT:
				game_over = True

		# Draw
		screen.fill((0, 0, 255))
		for pipe in pipes:
			pipe.draw()
		bird.draw()
		draw_text(f"Score: {score}", 10, 10)
		if game_over:
			draw_text("Game Over!", WIDTH//2 - 100, HEIGHT//2 - 40)
			draw_text("Press R to Restart", WIDTH//2 - 140, HEIGHT//2 + 10)
		pygame.display.flip()

if __name__ == "__main__":
	main()
