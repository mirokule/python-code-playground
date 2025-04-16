import pygame
import random

# 初始化 Pygame
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 设置游戏窗口大小
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("飞机大战")

# 玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH - self.rect.width) // 2
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 10
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites_list.add(bullet)
        bullet_list.add(bullet)

# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.y < 0:
            self.kill()

# 敌机类
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.y > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 4)

# 创建精灵组
all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

# 创建玩家飞机
player = Player()
all_sprites_list.add(player)

# 创建敌机
for i in range(5):
    enemy = Enemy()
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)

# 游戏主循环
clock = pygame.time.Clock()
running = True
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
            elif event.key == pygame.K_SPACE:
                player.shoot()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0

    # 更新所有精灵
    all_sprites_list.update()

    # 检测子弹和敌机的碰撞
    for bullet in bullet_list:
        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
        for enemy in enemy_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            new_enemy = Enemy()
            all_sprites_list.add(new_enemy)
            enemy_list.add(new_enemy)
        if bullet.rect.y < 0:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # 检测玩家飞机和敌机的碰撞
    enemy_hit_player = pygame.sprite.spritecollide(player, enemy_list, False)
    if enemy_hit_player:
        running = False

    # 绘制屏幕
    screen.fill(BLACK)
    all_sprites_list.draw(screen)

    # 显示分数
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", 1, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    