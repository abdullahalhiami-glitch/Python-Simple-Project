import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
PINK = (255, 182, 193)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Maze layout (1 = wall, 0 = path, 2 = pellet, 3 = power pellet, 4 = empty)
MAZE = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,1],
    [1,3,1,1,1,2,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,2,1,1,2,2,1,1,2,2,1,1,1,1,1,2,1,3,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1],
    [1,2,2,2,2,2,1,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,1,2,2,1],
    [1,1,1,1,1,2,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,2,1,1,2,2,1,1,2,2,1,1,1,1,1,2,1,1,1],
    [0,0,0,0,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,0],
    [1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1],
    [0,0,0,0,0,2,0,2,2,2,2,2,2,0,0,2,2,2,2,2,2,2,2,2,2,2,2,0,0,2,2,2,2,2,2,2,2,0,0,0],
    [1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1],
    [0,0,0,0,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,0],
    [1,1,1,1,1,2,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,2,1,1,2,2,1,1,2,2,1,1,1,1,1,2,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,3,1,1,1,2,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,2,1,1,2,2,1,1,2,2,1,1,1,1,1,2,1,3,1],
    [1,2,1,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,1,2,1],
    [1,2,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1],
    [1,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,1],
    [1,1,1,1,1,2,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,2,1,1,2,2,1,1,2,2,1,1,1,1,1,2,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = RIGHT
        self.next_dir = RIGHT
        self.speed = 2

    def move(self):
        # Try to change direction
        if self.can_move(self.next_dir):
            self.dir = self.next_dir
        if self.can_move(self.dir):
            self.x += self.dir[0] * self.speed
            self.y += self.dir[1] * self.speed
            # Wrap around
            if self.x < 0:
                self.x = SCREEN_WIDTH - BLOCK_SIZE
            elif self.x >= SCREEN_WIDTH:
                self.x = 0
            # Check pellet
            grid_x = int(self.x // BLOCK_SIZE)
            grid_y = int(self.y // BLOCK_SIZE)
            if MAZE[grid_y][grid_x] == 2:
                MAZE[grid_y][grid_x] = 0
            elif MAZE[grid_y][grid_x] == 3:
                MAZE[grid_y][grid_x] = 0
                # Power pellet effect

    def can_move(self, dir):
        new_x = self.x + dir[0] * BLOCK_SIZE
        new_y = self.y + dir[1] * BLOCK_SIZE
        grid_x = int(new_x // BLOCK_SIZE)
        grid_y = int(new_y // BLOCK_SIZE)
        if 0 <= grid_x < len(MAZE[0]) and 0 <= grid_y < len(MAZE):
            return MAZE[grid_y][grid_x] != 1
        return False

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (int(self.x + BLOCK_SIZE//2), int(self.y + BLOCK_SIZE//2)), BLOCK_SIZE//2)

class Ghost:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.dir = random.choice([UP, DOWN, LEFT, RIGHT])
        self.speed = 1

    def move(self):
        dirs = [UP, DOWN, LEFT, RIGHT]
        random.shuffle(dirs)
        for d in dirs:
            if self.can_move(d):
                self.dir = d
                break
        if self.can_move(self.dir):
            self.x += self.dir[0] * self.speed
            self.y += self.dir[1] * self.speed

    def can_move(self, dir):
        new_x = self.x + dir[0] * BLOCK_SIZE
        new_y = self.y + dir[1] * BLOCK_SIZE
        grid_x = int(new_x // BLOCK_SIZE)
        grid_y = int(new_y // BLOCK_SIZE)
        if 0 <= grid_x < len(MAZE[0]) and 0 <= grid_y < len(MAZE):
            return MAZE[grid_y][grid_x] != 1
        return False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x + BLOCK_SIZE//2), int(self.y + BLOCK_SIZE//2)), BLOCK_SIZE//2)

def draw_maze(screen):
    for y in range(len(MAZE)):
        for x in range(len(MAZE[y])):
            if MAZE[y][x] == 1:
                pygame.draw.rect(screen, WHITE, (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            elif MAZE[y][x] == 2:
                pygame.draw.circle(screen, WHITE, (x*BLOCK_SIZE + BLOCK_SIZE//2, y*BLOCK_SIZE + BLOCK_SIZE//2), 2)
            elif MAZE[y][x] == 3:
                pygame.draw.circle(screen, WHITE, (x*BLOCK_SIZE + BLOCK_SIZE//2, y*BLOCK_SIZE + BLOCK_SIZE//2), 5)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pac-Man")
    clock = pygame.time.Clock()

    pacman = Pacman(1*BLOCK_SIZE, 1*BLOCK_SIZE)
    ghosts = [
        Ghost(18*BLOCK_SIZE, 9*BLOCK_SIZE, RED),
        Ghost(19*BLOCK_SIZE, 9*BLOCK_SIZE, PINK),
        Ghost(20*BLOCK_SIZE, 9*BLOCK_SIZE, CYAN),
        Ghost(21*BLOCK_SIZE, 9*BLOCK_SIZE, ORANGE)
    ]

    running = True
    while running:
        screen.fill(BLACK)
        draw_maze(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pacman.next_dir = UP
                elif event.key == pygame.K_DOWN:
                    pacman.next_dir = DOWN
                elif event.key == pygame.K_LEFT:
                    pacman.next_dir = LEFT
                elif event.key == pygame.K_RIGHT:
                    pacman.next_dir = RIGHT

        pacman.move()
        for ghost in ghosts:
            ghost.move()

        pacman.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()