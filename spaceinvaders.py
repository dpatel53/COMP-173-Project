import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.SysFont("Arial", 30)

# Clock and Timer
clock = pygame.time.Clock()
start_time = time.time()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -7

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

# Game loop function
def game_loop():
    player = Player()
    player_group = pygame.sprite.Group(player)
    bullet_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    score = 0
    lives = 3
    game_over = False
    timer_duration = 60

    enemy_spawn_event = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_spawn_event, 800)

    while True:
        screen.fill(BLACK)

        if game_over:
            draw_text("Game Over", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 60)
            draw_text(f"Score: {score}", font, WHITE, screen, WIDTH // 2, HEIGHT // 2)
            draw_text("Press R to Play Again or Q to Quit", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 60)
            pygame.display.flip()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if keys[pygame.K_r]:
                return game_loop()
            if keys[pygame.K_q]:
                pygame.quit()
                sys.exit()
            continue

        # Timer
        elapsed_time = int(time.time() - start_time)
        time_left = max(timer_duration - elapsed_time, 0)
        if time_left == 0 or lives <= 0:
            game_over = True

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet_group.add(Bullet(player.rect.centerx, player.rect.top))
            if event.type == enemy_spawn_event:
                x_pos = random.randint(0, WIDTH - 40)
                enemy_group.add(Enemy(x_pos, -30))

        # Update
        player_group.update(keys)
        bullet_group.update()
        enemy_group.update()

        # Collision
        hits = pygame.sprite.groupcollide(bullet_group, enemy_group, True, True)
        score += len(hits)

        player_hits = pygame.sprite.spritecollide(player, enemy_group, True)
        if player_hits:
            lives -= 1

        # Draw
        player_group.draw(screen)
        bullet_group.draw(screen)
        enemy_group.draw(screen)

        draw_text(f"Score: {score}", font, WHITE, screen, WIDTH // 2, 30)
        draw_text(f"Time Left: {time_left}s", font, WHITE, screen, WIDTH // 2, 70)
        draw_text(f"Lives: {lives}", font, WHITE, screen, WIDTH // 2, 110)

        pygame.display.flip()
        clock.tick(60)

# Start the game
game_loop()
