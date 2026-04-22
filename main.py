import pygame as pg
import random

# Window setup
width, height = 700, 950
pg.init()
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

# ================= PLAYER =================
class Player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

        self.speed = 0
        self.gravity = 2000
        self.jump_force = -600

    def jump(self):
        self.speed = self.jump_force

    def update(self, dt):
        self.speed += self.gravity * dt
        self.y += self.speed * dt

    def get_rect(self):
        return pg.Rect(self.x, self.y, self.size, self.size)

    def draw(self, surface):
        pg.draw.rect(surface, (255, 255, 255),
                     (self.x, int(self.y), self.size, self.size))


# ================= PIPES =================
class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 60
        self.gap = 200
        self.speed = 300

        self.reset()

    def reset(self):
        self.top_height = random.randint(150, 500)
        self.bottom_y = self.top_height + self.gap

    def update(self, dt):
        self.x -= self.speed * dt

        if self.x < -self.width:
            self.x = width
            self.reset()

    def get_rects(self):
        top_rect = pg.Rect(self.x, 0, self.width, self.top_height)
        bottom_rect = pg.Rect(self.x, self.bottom_y,
                              self.width, height - self.bottom_y)
        return top_rect, bottom_rect

    def draw(self, surface):
        top_rect, bottom_rect = self.get_rects()
        pg.draw.rect(surface, (0, 200, 0), top_rect)
        pg.draw.rect(surface, (0, 200, 0), bottom_rect)


# ================= INIT =================
bird = Player(width // 3, height // 2, 40)

pipes = [
    Pipe(width),
    Pipe(width + 300),
    Pipe(width + 600)
]

font_big = pg.font.SysFont(None, 80)
font_small = pg.font.SysFont(None, 40)

game_over = False
running = True

# ================= LOOP =================
while running:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if not game_over:
                if event.key == pg.K_SPACE:
                    bird.jump()
            else:
                if event.key == pg.K_r:
                    # Restart game
                    bird = Player(width // 3, height // 2, 40)
                    pipes = [Pipe(width), Pipe(width + 300), Pipe(width + 600)]
                    game_over = False

    screen.fill((0, 0, 0))

    # ===== UPDATE =====
    if not game_over:
        bird.update(dt)

        for pipe in pipes:
            pipe.update(dt)

        # ===== COLLISION =====
        bird_rect = bird.get_rect()

        if bird.y < 0 or bird.y > height:
            game_over = True

        for pipe in pipes:
            top_rect, bottom_rect = pipe.get_rects()

            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
                game_over = True

    # ===== DRAW =====
    for pipe in pipes:
        pipe.draw(screen)

    bird.draw(screen)

    if game_over:
        text = font_big.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (width // 2 - 180, height // 2 - 60))

        restart_text = font_small.render("Press R to Restart", True, (255, 255, 255))
        screen.blit(restart_text, (width // 2 - 170, height // 2 + 20))

    pg.display.flip()

pg.quit()