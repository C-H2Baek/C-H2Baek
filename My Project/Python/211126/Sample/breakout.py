import sys
from random import randint
from pgtools import *

try:
    import pygame as pg
except ModuleNotFoundError:
    print("ModuleError: you should install pg")
    sys.exit(1)

pg.init()

FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MINT = (0, 255, 255)
YELLOW = (255, 255, 0)
MAX_WIDTH, MAX_HEIGHT = 600, 400

fpscheck = pg.time.Clock()
screen = pg.display.set_mode((MAX_WIDTH, MAX_HEIGHT))  # main surface
pg.display.set_caption("Breakout Game")

# bat group
bat_D = Bat(screen, 100, 15, MAX_WIDTH / 2, MAX_HEIGHT - 30, MINT)
bat_D.k_up, bat_D.k_down = None, None
bats = pg.sprite.Group()
bats.add(bat_D)

# brick group
def makeBricks(n, m, color=None):
    bricks = pg.sprite.Group()
    for y in range(n):
        for x in range(m):
            bricks.add(Bat(screen, 40, 15, MAX_WIDTH * (x + 1) / (m + 1), MAX_HEIGHT * (y + 1) / (n + 5), color))
    return bricks


bricks = makeBricks(1, 5)

for brick in bricks:
    print(brick.rect.center)

# ball group
balls = pg.sprite.Group()
ball = Ball(screen, 10, MAX_WIDTH / 2, MAX_HEIGHT / 2, randint(-10, 10), -10, RED)
balls.add(ball)

# endline group
verLines = pg.sprite.Group()
horLines = pg.sprite.Group()
leftEnd = EndLine(screen, "vertical", 0)
rightEnd = EndLine(screen, "vertical", MAX_WIDTH - 1)
topEnd = EndLine(screen, "horizontal", 0)
bottomEnd = EndLine(screen, "horizontal", MAX_HEIGHT - 1)
verLines.add(leftEnd, rightEnd)
horLines.add(topEnd, bottomEnd)

fpstick = FPS * 8
game_run = True
score_left, score_right = 0, 0
font = pg.font.SysFont("Ink Free", 50)

while 1:
    screen.fill(BLACK)
    for event in pg.event.get():
        # pressing exit
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    if pg.key.get_pressed()[pg.K_SPACE]:
        balls = pg.sprite.Group()
        ball = Ball(screen, 10, MAX_WIDTH / 2, MAX_HEIGHT / 2, randint(-5, 5), -10, RED)
        balls.add(ball)
        bricks = makeBricks(3, 10)
        fpstick = FPS * 8
        game_run = True
    if len(bricks) == 0:
        text_win = font.render("You win!!!", True, GREEN, BLUE)
        text_winRect = text_win.get_rect()
        text_winRect.center = (MAX_WIDTH / 2, MAX_HEIGHT / 2)
        screen.blit(text_win, text_winRect)
        pg.display.update()
        fpscheck.tick(FPS)
        game_run = False
        continue
    if game_run:
        fpstick -= 1
        if fpstick < 0:
            for brick in bricks:
                brick.rect.move_ip(0, 50)
                if brick.rect.bottom > MAX_HEIGHT:
                    game_run = False
                    continue
            fpstick = FPS * 8
        for ball in balls:
            balls.remove(ball)
            ball.inelasticCollide(verLines, y=False)
            endCheck = ball.inelasticCollide(horLines, x=False) or []
            if bottomEnd in endCheck:
                print("left")
            else:
                ball.inelasticCollide(bricks, kill=True, x=False)
                for bat in bats:
                    ball.specialCollide(bat, x=False, sensitivity=10)
                ball.update()
                balls.add(ball)

    bats.update()

    # drawing
    bottomEnd.draw(screen)
    bricks.draw(screen)
    bats.draw(screen)
    balls.draw(screen)
    pg.display.update()
    fpscheck.tick(FPS)
