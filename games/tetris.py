import pygame
import random

# 初始化 Pygame
pygame.init()

# 定义常量
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
ROWS = HEIGHT // BLOCK_SIZE
COLS = WIDTH // BLOCK_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# 定义形状
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

COLORS = [CYAN, YELLOW, MAGENTA, GREEN, RED, BLUE, ORANGE]


class Block:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS)

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def rotate(self):
        self.shape = list(map(list, zip(*self.shape[::-1])))


def draw_grid(screen):
    for i in range(ROWS):
        pygame.draw.line(screen, WHITE, (0, i * BLOCK_SIZE), (WIDTH, i * BLOCK_SIZE))
    for j in range(COLS):
        pygame.draw.line(screen, WHITE, (j * BLOCK_SIZE, 0), (j * BLOCK_SIZE, HEIGHT))


def draw_block(screen, block):
    for i in range(len(block.shape)):
        for j in range(len(block.shape[0])):
            if block.shape[i][j] == 1:
                pygame.draw.rect(screen, block.color,
                                 (block.x * BLOCK_SIZE + j * BLOCK_SIZE, block.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                  BLOCK_SIZE, BLOCK_SIZE))


def is_collision(block, grid):
    for i in range(len(block.shape)):
        for j in range(len(block.shape[0])):
            if block.shape[i][j] == 1:
                new_x = block.x + j
                new_y = block.y + i
                if new_x < 0 or new_x >= COLS or new_y >= ROWS or (
                        new_y >= 0 and grid[new_y][new_x]):
                    return True
    return False


def merge_block(block, grid):
    for i in range(len(block.shape)):
        for j in range(len(block.shape[0])):
            if block.shape[i][j] == 1:
                grid[block.y + i][block.x + j] = 1


def clear_lines(grid):
    full_lines = []
    for i in range(ROWS):
        if all(grid[i]):
            full_lines.append(i)
    for line in full_lines:
        del grid[line]
        grid = [[0] * COLS] + grid
    return grid, len(full_lines)


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    grid = [[0] * COLS for _ in range(ROWS)]
    current_block = Block(COLS // 2 - len(SHAPES[0][0]) // 2, 0, random.choice(SHAPES))
    game_over = False
    score = 0
    font = pygame.font.Font(None, 36)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_block = Block(current_block.x - 1, current_block.y, current_block.shape)
                    if not is_collision(new_block, grid):
                        current_block.move_left()
                if event.key == pygame.K_RIGHT:
                    new_block = Block(current_block.x + 1, current_block.y, current_block.shape)
                    if not is_collision(new_block, grid):
                        current_block.move_right()
                if event.key == pygame.K_DOWN:
                    new_block = Block(current_block.x, current_block.y + 1, current_block.shape)
                    if not is_collision(new_block, grid):
                        current_block.move_down()
                if event.key == pygame.K_UP:
                    new_shape = list(map(list, zip(*current_block.shape[::-1])))
                    new_block = Block(current_block.x, current_block.y, new_shape)
                    if not is_collision(new_block, grid):
                        current_block.rotate()

        new_block = Block(current_block.x, current_block.y + 1, current_block.shape)
        if is_collision(new_block, grid):
            merge_block(current_block, grid)
            grid, cleared_lines = clear_lines(grid)
            score += cleared_lines * 100
            current_block = Block(COLS // 2 - len(SHAPES[0][0]) // 2, 0, random.choice(SHAPES))
            if is_collision(current_block, grid):
                game_over = True
        else:
            current_block.move_down()

        screen.fill(BLACK)
        draw_grid(screen)
        draw_block(screen, current_block)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    pygame.draw.rect(screen, WHITE,
                                     (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        clock.tick(3)

    pygame.quit()


if __name__ == "__main__":
    main()
    