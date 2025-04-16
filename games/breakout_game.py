import pygame
import random

# 初始化 Pygame
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 设置游戏窗口大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("打砖块游戏")

# 挡板类
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([100, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH - self.rect.width) // 2
        self.rect.y = SCREEN_HEIGHT - 20
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

# 球的类
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed_x = random.choice([-3, 3])
        self.speed_y = -3

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.speed_x = -self.speed_x
        if self.rect.y < 0:
            self.speed_y = -self.speed_y

# 砖块类
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([70, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# 创建精灵组
all_sprites_list = pygame.sprite.Group()
ball_list = pygame.sprite.Group()
brick_list = pygame.sprite.Group()

# 创建挡板
paddle = Paddle()
all_sprites_list.add(paddle)

# 创建球
ball = Ball()
all_sprites_list.add(ball)
ball_list.add(ball)

# 创建砖块
for i in range(10):
    for j in range(3):
        brick = Brick(i * 80 + 10, j * 30 + 20)
        all_sprites_list.add(brick)
        brick_list.add(brick)

# 游戏主循环
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                paddle.speed_x = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle.speed_x = 0

    # 更新所有精灵
    all_sprites_list.update()

    # 检测球和挡板的碰撞
    if pygame.sprite.spritecollide(paddle, ball_list, False):
        ball.speed_y = -ball.speed_y

    # 检测球和砖块的碰撞
    brick_hit_list = pygame.sprite.spritecollide(ball, brick_list, True)
    for brick in brick_hit_list:
        ball.speed_y = -ball.speed_y

    # 检测球是否掉落到底部
    if ball.rect.y > SCREEN_HEIGHT:
        running = False

    # 绘制屏幕
    screen.fill(BLACK)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    